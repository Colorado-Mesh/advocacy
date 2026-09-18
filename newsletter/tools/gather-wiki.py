#!/usr/bin/env python3
"""
gather-wiki.py — pull recent activity from wiki.coloradomesh.org into a
newsletter items list. Read-only, no credentials, standard library only.

Usage:
    ./gather-wiki.py [--since YYYY-MM-DD] [--items <items-list.md>]

    --since   Only include changes on/after this date (UTC). Default: ~1 month ago.
    --items   Items-list file to inject into. Default: newest
              issues/*/items-list.md; if none exists, prints to stdout.

What it does:
    - Queries the MediaWiki API for main-namespace recent changes (edits + new
      pages) since the cutoff, following continuation.
    - Groups by page. New pages get a "NEW" marker; edited pages get an edit
      count and the latest edit summary.
    - Injects markdown bullets between the <!-- WIKI-ITEMS-START --> /
      <!-- WIKI-ITEMS-END --> anchors in the items list (idempotent).

Bot etiquette: read-only GETs, descriptive User-Agent, paged query.
"""
import argparse
import datetime as dt
import glob
import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://wiki.coloradomesh.org/api.php"
WIKI_BASE = "https://wiki.coloradomesh.org/wiki"
UA = "ColoradoMeshNewsletter/1.0 (https://wiki.coloradomesh.org; letark) gather-wiki.py"


def api_get(params):
    params = dict(params, format="json", action="query")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_changes(rcstart):
    """Return all main-namespace edits/new pages on/after rcstart (ISO Z).

    With rcdir=newer, MediaWiki enumerates oldest->newest: rcstart is the OLDER
    bound (where enumeration begins) and rcend the newer bound (omitted = now).
    """
    changes = []
    cont = None
    while True:
        params = {
            "list": "recentchanges",
            "rcprop": "title|timestamp|user|comment|sizes|flags|ids",
            "rctype": "edit|new",
            "rcnamespace": 0,
            "rcdir": "newer",       # oldest -> newest within window
            "rcstart": rcstart,     # older bound (inclusive)
            "rclimit": 500,
        }
        if cont:
            params["rccontinue"] = cont
        data = api_get(params)
        changes.extend(data.get("query", {}).get("recentchanges", []))
        cont = data.get("continue", {}).get("rccontinue")
        if not cont:
            break
    return changes


def build_bullets(changes):
    """Group changes by page and render markdown bullets."""
    pages = {}
    for c in changes:
        title = c["title"]
        p = pages.setdefault(title, {
            "title": title, "is_new": False, "edits": 0,
            "last_ts": "", "last_comment": "", "users": set(),
        })
        if c.get("type") == "new":
            p["is_new"] = True
        elif c.get("type") == "edit":
            p["edits"] += 1
        ts = c.get("timestamp", "")
        if ts > p["last_ts"]:
            p["last_ts"] = ts
            p["last_comment"] = c.get("comment", "") or ""
        if c.get("user"):
            p["users"].add(c["user"])

    # New pages first, then by amount of activity, then title.
    ordered = sorted(
        pages.values(),
        key=lambda p: (not p["is_new"], -(p["edits"] + (1 if p["is_new"] else 0)), p["title"]),
    )

    lines = []
    for p in ordered:
        link = f"{WIKI_BASE}/{p['title'].replace(' ', '_')}"
        date = p["last_ts"].split("T")[0] if p["last_ts"] else "?"
        users = ", ".join(sorted(p["users"])) or "?"
        if p["is_new"]:
            head = f"**NEW page:** [{p['title']}]({link})"
        else:
            n = p["edits"]
            suffix = f" ({n} edit{'s' if n != 1 else ''})" if n else ""
            head = f"Updated: [{p['title']}]({link}){suffix}"
        line = f"- [ ] {head} — _wiki, {date}_ by {users}"
        comment = p["last_comment"].replace("\n", " ").strip()
        if comment:
            line += f"\n      \u21b3 _{comment}_"
        lines.append(line)
    return "\n".join(lines) if lines else "_(no wiki changes in this window)_"


def inject(items_path, block):
    with open(items_path, encoding="utf-8") as f:
        text = f.read()
    start = "<!-- WIKI-ITEMS-START -->"
    end = "<!-- WIKI-ITEMS-END -->"
    if start not in text or end not in text:
        raise SystemExit(f"Anchors not found in {items_path}")
    pre = text.split(start)[0]
    post = text.split(end, 1)[1]
    new = pre + block + post
    with open(items_path, "w", encoding="utf-8") as f:
        f.write(new)


def main():
    ap = argparse.ArgumentParser(description="Gather wiki changes for the newsletter.")
    ap.add_argument("--since", help="YYYY-MM-DD (UTC). Default ~1 month ago.")
    ap.add_argument("--items", help="items-list.md to inject into.")
    args = ap.parse_args()

    if args.since:
        since = args.since
    else:
        since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=30)).strftime("%Y-%m-%d")
    rcstart = f"{since}T00:00:00Z"

    print(f"Gathering wiki changes since {since} ...", file=sys.stderr)
    changes = fetch_changes(rcstart)
    print(f"  fetched {len(changes)} change(s)", file=sys.stderr)
    bullets = build_bullets(changes)

    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    block = (
        "<!-- WIKI-ITEMS-START -->\n"
        f"_Gathered {today} — wiki changes since {since}. Promote the good ones above._\n\n"
        f"{bullets}\n"
        "<!-- WIKI-ITEMS-END -->"
    )

    items = args.items
    if not items:
        _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        candidates = sorted(glob.glob(os.path.join(_root, "issues/*/items-list.md")),
                            key=os.path.getmtime, reverse=True)
        items = candidates[0] if candidates else None

    if not items or not os.path.isfile(items):
        print("No items-list file found; printing gathered block to stdout.", file=sys.stderr)
        print(block)
        return

    inject(items, block)
    print(f"Injected wiki items into {items}", file=sys.stderr)


if __name__ == "__main__":
    main()
