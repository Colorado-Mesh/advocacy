#!/usr/bin/env python3
"""
gather-discord.py — pull messages from EVERY readable Colorado Mesh Discord
channel into a newsletter items list, with persistent per-channel state so
nothing is ever missed or double-counted across months.

Read-only, standard library only. The token is NEVER stored — paste it fresh
each run via DISCORD_TOKEN (preferred) or --token.

    export DISCORD_TOKEN='...'                 # this shell only
    # First run — deep backfill (conversations may predate this month):
    ./gather-discord.py --backfill-days 120
    # Every run after — pulls only what's new since last time (high-water mark):
    ./gather-discord.py

HOW IT WORKS
  - Auto-discovers all guilds the token is in, and all text channels it can
    read (VIEW_CHANNEL + READ_MESSAGE_HISTORY). No manual channel list.
  - Keeps a high-water mark (last-seen message ID) per channel in state.json.
    Each run fetches everything AFTER that mark, so a thread that started two
    months ago is still captured on its first run and never re-pulled after.
  - --backfill-days N sets how far back to reach for channels we've never seen
    before (the big first run). Channels with existing state ignore it and just
    resume from their mark.
  - Writes markdown between the <!-- DISCORD-ITEMS-START/END --> anchors of the
    current issue's items list (or stdout if none found).

TOKEN TYPE: user token (sent raw) or bot token (prefix "Bot "). A read-only bot
invited to the server is the ToS-clean option, and permission detection is exact
for a bot. Reading with a personal *user* token is self-botting — for a user
token we just try each channel and skip 403s.

FLAGS
  --backfill-days N   how far back for never-seen channels (default 45)
  --exclude FILE      channel IDs (one per line, # comments) to always skip
  --include-bots      include bot messages (off by default)
  --min-len N         ignore messages shorter than N chars (default 40)
  --react-flag N      reactions >= N flag a message 🔥 (default 3)
  --guild ID          restrict to one guild (default: all readable)
  --state FILE        state file (default: state.json next to this script)
  --items FILE        items-list.md to inject into (default: newest issue)
  --dry-run           don't write state.json (preview only)

PRIVACY: only reads guild text channels the token can already see. Never DMs.
Review the gathered output before promoting anything into the newsletter.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://discord.com/api/v10"
UA = "ColoradoMeshNewsletter (https://coloradomesh.org, v1.0)"
DISCORD_EPOCH = 1420070400000

# Permission bits
PERM_VIEW_CHANNEL = 1 << 10
PERM_READ_HISTORY = 1 << 16
PERM_ADMINISTRATOR = 1 << 3
# Text-bearing channel types worth reading
TEXT_TYPES = {0, 5}  # GUILD_TEXT, GUILD_ANNOUNCEMENT


def snowflake_for(ts_ms):
    return (int(ts_ms) - DISCORD_EPOCH) << 22


def ts_of_snowflake(sf):
    return ((int(sf) >> 22) + DISCORD_EPOCH) / 1000.0


def auth_header(token):
    t = token.strip()
    if t.lower().startswith("bot "):
        return "Bot " + t[4:].strip()
    return t


def api_get(path, token, params=None, allow_403=False):
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Authorization": auth_header(token), "User-Agent": UA})
    while True:
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                retry = float(e.headers.get("Retry-After", "1"))
                print(f"    rate limited, sleeping {retry}s", file=sys.stderr)
                time.sleep(retry + 0.5)
                continue
            if e.code in (403, 401) and allow_403:
                return None
            body = e.read().decode("utf-8", "replace")[:200]
            raise SystemExit(f"Discord API {e.code} on {path}: {body}")


# ---------------------------------------------------------------- discovery ---
def get_me(token):
    return api_get("/users/@me", token)


def list_guilds(token):
    return api_get("/users/@me/guilds", token) or []


def is_bot_token(token):
    return token.strip().lower().startswith("bot ")


def can_read(channel, guild, me_id, token):
    """Best-effort check that the token can view + read history of channel.

    For bot tokens, compute permissions from @everyone + the bot member's
    role overwrites. For user tokens, permission data isn't fully available,
    so return True and let the message fetch skip on 403.
    """
    if not is_bot_token(token):
        return True
    # bot: fetch our member to get roles
    member = api_get(f"/guilds/{guild['id']}/members/{me_id}", token, allow_403=True)
    roles = set(member.get("roles", [])) if member else set()
    everyone_id = guild["id"]  # @everyone role id == guild id

    guild_roles = {r["id"]: int(r["permissions"]) for r in guild.get("_roles", [])}
    base = guild_roles.get(everyone_id, 0)
    for rid in roles:
        base |= guild_roles.get(rid, 0)
    if base & PERM_ADMINISTRATOR:
        return True

    perms = base
    ows = {o["id"]: o for o in channel.get("permission_overwrites", [])}
    # @everyone overwrite
    if everyone_id in ows:
        o = ows[everyone_id]
        perms = (perms & ~int(o["deny"])) | int(o["allow"])
    # role overwrites (type 0)
    allow = deny = 0
    for rid in roles:
        if rid in ows and ows[rid].get("type") == 0:
            allow |= int(ows[rid]["allow"]); deny |= int(ows[rid]["deny"])
    perms = (perms & ~deny) | allow
    # member overwrite (type 1)
    if me_id in ows and ows[me_id].get("type") == 1:
        o = ows[me_id]
        perms = (perms & ~int(o["deny"])) | int(o["allow"])
    return bool(perms & PERM_VIEW_CHANNEL) and bool(perms & PERM_READ_HISTORY)


def discover_channels(token, allowed_guilds, excludes):
    """Return list of dicts: {id, name, guild_name}.

    allowed_guilds is a REQUIRED set of guild IDs — discovery only ever touches
    those servers, so a personal account in many unrelated guilds is never
    scraped. Passing an empty set discovers nothing (safe default).
    """
    me = get_me(token)
    me_id = me["id"]
    guilds = list_guilds(token)
    guilds = [g for g in guilds if g["id"] in allowed_guilds]
    if not guilds:
        raise SystemExit("No allowed guilds matched. Set --guild or discord-guilds.txt.")
    found = []
    for g in guilds:
        gname = g.get("name", g["id"])
        # roles needed for bot permission math
        if is_bot_token(token):
            g["_roles"] = api_get(f"/guilds/{g['id']}/roles", token, allow_403=True) or []
        channels = api_get(f"/guilds/{g['id']}/channels", token, allow_403=True)
        if not channels:
            print(f"  guild {gname}: no channel access", file=sys.stderr)
            continue
        n = 0
        for ch in channels:
            if ch.get("type") not in TEXT_TYPES:
                continue
            if ch["id"] in excludes:
                continue
            if not can_read(ch, g, me_id, token):
                continue
            found.append({"id": ch["id"], "name": ch.get("name", ch["id"]),
                          "guild_name": gname})
            n += 1
        print(f"  guild {gname}: {n} readable text channel(s) "
              f"({len(excludes)} excluded globally)", file=sys.stderr)
    return found


# ----------------------------------------------------------------- fetching ---
def fetch_messages(token, cid, after_sf, cap):
    msgs = []
    after = after_sf
    while len(msgs) < cap:
        batch = api_get(f"/channels/{cid}/messages", token,
                        {"after": after, "limit": 100}, allow_403=True)
        if not batch:
            break
        batch.reverse()  # oldest-first for forward paging
        msgs.extend(batch)
        after = batch[-1]["id"]
        if len(batch) < 100:
            break
        time.sleep(0.3)
    return msgs


def clean(text):
    return re.sub(r"\s+", " ", text.replace("\n", " ")).strip()


# -------------------------------------------------------------------- state ---
def load_state(path):
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"channels": {}}


def save_state(path, state):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, sort_keys=True)
    os.replace(tmp, path)


# ------------------------------------------------------------------ compose ---
def build_channel_block(ch, msgs, min_len, include_bots, react_flag):
    picked = []
    for m in msgs:
        if m.get("author", {}).get("bot") and not include_bots:
            continue
        content = clean(m.get("content", ""))
        reacts = sum(r.get("count", 0) for r in m.get("reactions", []))
        has_attach = bool(m.get("attachments"))
        if len(content) < min_len and reacts < react_flag and not has_attach:
            continue
        picked.append((m, content, reacts, has_attach))
    picked.sort(key=lambda x: (x[2], x[0]["id"]), reverse=True)

    title = f"### #{ch['name']}  ·  _{ch['guild_name']}_  ({len(picked)} notable)"
    lines = [title]
    if not picked:
        lines.append("_(nothing notable in window)_")
    for m, content, reacts, has_attach in picked:
        author = m.get("author", {}).get("global_name") \
            or m.get("author", {}).get("username", "?")
        date = m.get("timestamp", "")[:10]
        snippet = content[:220] + ("…" if len(content) > 220 else "")
        flag = " 🔥" if reacts >= react_flag else ""
        attach = " 📎" if has_attach else ""
        meta = f"_{author}, {date}_"
        if reacts:
            meta += f" · {reacts} reaction{'s' if reacts != 1 else ''}"
        lines.append(f"- [ ]{flag}{attach} {snippet or '(attachment/embed only)'} — {meta}")
    return "\n".join(lines)


def inject(items_path, block):
    with open(items_path, encoding="utf-8") as f:
        text = f.read()
    start, end = "<!-- DISCORD-ITEMS-START -->", "<!-- DISCORD-ITEMS-END -->"
    if start not in text or end not in text:
        raise SystemExit(f"Anchors not found in {items_path}")
    pre = text.split(start)[0]
    post = text.split(end, 1)[1]
    with open(items_path, "w", encoding="utf-8") as f:
        f.write(pre + block + post)


def load_excludes(path):
    ex = set()
    if path and os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if line:
                    ex.add(line.split()[0])
    return ex


def main():
    ap = argparse.ArgumentParser(description="Gather ALL readable Discord channels for the newsletter.")
    ap.add_argument("--token")
    ap.add_argument("--backfill-days", type=int, default=45,
                    help="How far back for never-seen channels (default 45).")
    ap.add_argument("--exclude", help="File of channel IDs to skip.",
                    default=os.path.join(os.path.dirname(__file__), "discord-exclude.txt"))
    ap.add_argument("--guild", help="Comma-separated guild ID(s) to cover. "
                    "Overrides discord-guilds.txt. REQUIRED (directly or via file) "
                    "so unrelated servers are never touched.")
    ap.add_argument("--guilds-file",
                    default=os.path.join(os.path.dirname(__file__), "discord-guilds.txt"),
                    help="File of allowed guild IDs (one per line).")
    ap.add_argument("--include-bots", action="store_true")
    ap.add_argument("--min-len", type=int, default=40)
    ap.add_argument("--react-flag", type=int, default=3)
    ap.add_argument("--max-per-channel", type=int, default=2000,
                    help="Cap messages fetched per channel per run (default 2000). "
                    "Raise for a deep first backfill of very active channels.")
    ap.add_argument("--raw-out",
                    help="Also dump every fetched message as JSONL to this file "
                    "(for role-weighting + LLM triage). Appended if it exists.")
    ap.add_argument("--state", default=os.path.join(os.path.dirname(__file__), "state.json"))
    ap.add_argument("--items")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    token = args.token or os.environ.get("DISCORD_TOKEN")
    if not token:
        raise SystemExit("No token. Set DISCORD_TOKEN or pass --token.")

    excludes = load_excludes(args.exclude)

    # Build the REQUIRED guild allow-list (never scan every server the token is in).
    if args.guild:
        allowed = {g.strip() for g in args.guild.split(",") if g.strip()}
    else:
        allowed = load_excludes(args.guilds_file)  # same one-ID-per-line parser
    if not allowed:
        raise SystemExit(
            "No allowed guilds. Pass --guild <id[,id...]> or add IDs to "
            f"{args.guilds_file}. This is required so unrelated servers are never scraped.")

    state = load_state(args.state)
    chan_state = state.setdefault("channels", {})

    print(f"Discovering readable channels in {len(allowed)} allowed guild(s) ...",
          file=sys.stderr)
    channels = discover_channels(token, allowed, excludes)
    if not channels:
        raise SystemExit("No readable channels discovered.")
    print(f"  {len(channels)} channel(s) total", file=sys.stderr)

    # --- Channel inventory diff: detect NEW and DELETED/renamed channels -------
    # Compare what discovery found now against what state.json remembers seeing.
    discovered_ids = {ch["id"] for ch in channels}
    known_ids = set(chan_state.keys())
    new_ids = discovered_ids - known_ids
    # A channel in state but no longer discovered = deleted, renamed to a new id,
    # newly excluded, or permission revoked. Skip ones we deliberately excluded now.
    gone_ids = known_ids - discovered_ids - excludes

    name_by_id = {ch["id"]: ch["name"] for ch in channels}
    changes = []
    for cid in sorted(new_ids):
        changes.append(f"- [ ] ➕ **New channel discovered:** #{name_by_id.get(cid, cid)} "
                       f"(`{cid}`) — backfilling {args.backfill_days}d")
    for cid in sorted(gone_ids):
        old = chan_state.get(cid, {})
        changes.append(f"- [ ] ➖ **Channel gone:** #{old.get('name', cid)} (`{cid}`) — "
                       "deleted, renamed, excluded, or access revoked. "
                       "Left in state.json; remove it if it's truly gone.")
    if changes:
        print(f"  channel changes: {len(new_ids)} new, {len(gone_ids)} gone", file=sys.stderr)
    else:
        print("  channel inventory unchanged since last run", file=sys.stderr)

    backfill_floor_sf = snowflake_for(
        (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.backfill_days)).timestamp() * 1000)

    blocks = []
    total_msgs = 0
    raw_fh = None
    if args.raw_out:
        os.makedirs(os.path.dirname(os.path.abspath(args.raw_out)), exist_ok=True)
        raw_fh = open(args.raw_out, "a", encoding="utf-8")
        print(f"  writing raw messages to {args.raw_out}", file=sys.stderr)
    for ch in channels:
        cid = ch["id"]
        prev = chan_state.get(cid, {})
        hwm = prev.get("last_id")
        after_sf = int(hwm) if hwm else backfill_floor_sf
        origin = "since last run" if hwm else f"backfill {args.backfill_days}d"
        print(f"  #{ch['name']} ({ch['guild_name']}) — {origin}", file=sys.stderr)

        msgs = fetch_messages(token, cid, after_sf, args.max_per_channel)
        total_msgs += len(msgs)
        blocks.append(build_channel_block(ch, msgs, args.min_len,
                                          args.include_bots, args.react_flag))

        # Persist raw messages for downstream triage (role-weighting, LLM pass).
        if raw_fh is not None:
            for m in msgs:
                if m.get("author", {}).get("bot") and not args.include_bots:
                    continue
                author = m.get("author", {}) or {}
                atts = m.get("attachments", []) or []
                # keep the real image attachment URLs (+ dims) so we can pull
                # candidate photos per issue. Non-image attachments are ignored.
                images = [
                    {"url": a.get("url"), "w": a.get("width"), "h": a.get("height"),
                     "name": a.get("filename")}
                    for a in atts
                    if (a.get("content_type", "") or "").startswith("image/")
                    or re.search(r"\.(png|jpe?g|gif|webp)(\?|$)", a.get("filename", ""), re.I)
                ]
                rec = {
                    "id": m.get("id"),
                    "channel_id": cid,
                    "channel": ch["name"],
                    "guild": ch["guild_name"],
                    "ts": m.get("timestamp", ""),
                    "author_id": author.get("id"),
                    "author": author.get("global_name") or author.get("username", "?"),
                    "content": (m.get("content") or "").strip(),
                    "reactions": sum(r.get("count", 0) for r in m.get("reactions", [])),
                    "attachments": len(atts),
                    "images": images,
                    "urls": re.findall(r"https?://[^\s<>\"']+", m.get("content") or ""),
                    "reply_to": (m.get("referenced_message") or {}).get("id"),
                }
                raw_fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

        # advance high-water mark to newest message id we saw
        if msgs:
            newest = max(int(m["id"]) for m in msgs)
            chan_state[cid] = {"name": ch["name"], "guild": ch["guild_name"],
                               "last_id": str(newest),
                               "last_seen": dt.datetime.now(dt.timezone.utc).isoformat()}
        else:
            # No new messages. Advance the mark to NOW (a snowflake for the
            # current instant) so we don't rescan the same empty window next
            # run. Preserve an existing real mark if one is already higher.
            now_sf = snowflake_for(dt.datetime.now(dt.timezone.utc).timestamp() * 1000)
            prev_last = int(prev.get("last_id", 0))
            chan_state[cid] = {"name": ch["name"], "guild": ch["guild_name"],
                               "last_id": str(max(prev_last, now_sf)),
                               "last_seen": dt.datetime.now(dt.timezone.utc).isoformat()}

    if raw_fh is not None:
        raw_fh.close()

    print(f"  fetched {total_msgs} message(s) across {len(channels)} channel(s)", file=sys.stderr)

    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    body = "\n\n".join(blocks) if blocks else "_(no channels)_"
    changes_section = ""
    if changes:
        changes_section = ("### 🔀 Channel changes since last run\n"
                           + "\n".join(changes) + "\n\n")
    block = (
        "<!-- DISCORD-ITEMS-START -->\n"
        f"_Gathered {today} — all readable channels, incremental since last run "
        f"(never-seen channels backfilled {args.backfill_days}d). 🔥 = high "
        "engagement, 📎 = attachment. Raw signal; promote the good ones above._\n\n"
        f"{changes_section}"
        f"{body}\n"
        "<!-- DISCORD-ITEMS-END -->"
    )

    if not args.dry_run:
        save_state(args.state, state)
        print(f"State saved to {args.state}", file=sys.stderr)
    else:
        print("Dry run — state.json NOT written.", file=sys.stderr)

    items = args.items
    if not items:
        cands = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "issues/*/items-list.md")),
                       key=os.path.getmtime, reverse=True)
        items = cands[0] if cands else None
    if not items or not os.path.isfile(items):
        print("No items-list file found; printing gathered block to stdout.", file=sys.stderr)
        print(block)
        return
    inject(items, block)
    print(f"Injected Discord items into {items}", file=sys.stderr)


if __name__ == "__main__":
    main()
