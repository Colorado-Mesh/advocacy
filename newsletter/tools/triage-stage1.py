#!/usr/bin/env python3
"""
triage-stage1.py — mechanical (no-LLM) pre-filter for the newsletter.

Reads the raw messages JSONL from gather-discord.py and scores every message
with a deterministic, fully-explainable formula, then writes the top-N as a
shortlist for the LLM stage (and a human-readable report).

    ./triage-stage1.py issues/2026-09/data/raw-messages.jsonl \
        --authority authority.json --top 400 \
        --out issues/2026-09/data/shortlist.jsonl

Scoring signals (all transparent):
  - author authority weight (curated operators.json: owner/admin/rep/operator)
  - message posted in an authoritative channel (announcements, *-updates, etc.)
  - reactions (community signal)
  - contains links to wiki / tools / repos / maps (substance)
  - has attachments (builds, screenshots, photos)
  - newsletter keyword hits ("new repeater", "up on the air", "switched to"...)
  - length sweet-spot (very short = low, substantial = higher, wall-of-text capped)
  - light penalties for pure-noise patterns (single emoji, "lol", gif links)

Why mechanical first: 24k messages is too many + too expensive to hand to an LLM
raw. This cuts to a few hundred high-signal candidates the LLM can actually
reason over, and every score is auditable.
"""
import argparse
import json
import re
import sys
from collections import defaultdict

# ---- keyword signals ----------------------------------------------------------
NEWS_PATTERNS = [
    r"\bnew repeater\b", r"\bup on the air\b", r"\bonline\b", r"\bwent live\b",
    r"\bdeployed?\b", r"\bswitch(?:ed|ing)? to\b", r"\bchangeover\b",
    r"\brelease[sd]?\b", r"\bannounc\w+", r"\bnow (?:live|available|supported)\b",
    r"\bgot .* (?:up|working|running)\b", r"\bfirst (?:contact|message|hop)\b",
    r"\bmilestone\b", r"\bcoverage\b", r"\bbridg(?:e|ed|ing)\b", r"\bobserver\b",
    r"\bmqtt\b", r"\bfirmware\b", r"\bwiki\b", r"\bnaming convention\b",
    r"\bmediumfast\b", r"\bnet\b", r"\bevent\b", r"\bmeeting\b", r"\bhamfest\b",
    r"\bpresentation\b", r"\bdonat\w+", r"\bmap\b", r"\btower\b", r"\bsolar\b",
]
NEWS_RE = re.compile("|".join(NEWS_PATTERNS), re.I)

SUBSTANCE_URL_RE = re.compile(
    r"(wiki\.coloradomesh|tools\.meshcore|analyzer\.|map\.|github\.com|"
    r"coloradomesh\.org|meshcore\.io|meshtastic\.|substack\.com|rangecheck\.)", re.I)

NOISE_RE = re.compile(r"^(lol|lmao|haha|nice|yep|yeah|ok|okay|thanks?|ty|\+1|"
                      r"same|this|\W*)$", re.I)
GIF_RE = re.compile(r"(klipy\.com|tenor\.com|giphy\.com|\.gif)", re.I)


def load_authority(path):
    with open(path, encoding="utf-8") as f:
        a = json.load(f)
    weights = a["_weights_legend"]
    ops = {}
    for name, meta in a["operators"].items():
        ops[name.strip()] = weights.get(meta["role"], 1.0)
    return {
        "op_weight": ops,
        "auth_channels": set(a.get("authoritative_channels", [])),
        "regional_channels": set(a.get("regional_channels", [])),
        "baseline": weights.get("baseline", 1.0),
        "active_weight": weights.get("active_contributor", 1.3),
    }


def score_message(m, auth, behavioral_authors):
    content = m.get("content", "") or ""
    n = len(content)
    reasons = []
    score = 0.0

    # --- base content value by length ---
    if n < 15:
        base = 0.3
    elif n < 60:
        base = 1.0
    elif n < 400:
        base = 2.0
    else:
        base = 2.2  # long but capped; walls of text aren't proportionally better
    score += base

    # --- author authority multiplier ---
    author = (m.get("author") or "").strip()
    w = auth["op_weight"].get(author)
    if w is None and author in behavioral_authors:
        w = auth["active_weight"]
        reasons.append("posts-in-auth-channel")
    if w is None:
        w = auth["baseline"]
    if w > 1.0:
        reasons.append(f"author×{w}")
    score *= w

    # --- authoritative channel bump ---
    if m.get("channel") in auth["auth_channels"]:
        score += 3.0
        reasons.append("auth-channel")

    # --- reactions (community signal), diminishing ---
    r = m.get("reactions", 0)
    if r:
        rb = min(r, 12) * 0.6
        score += rb
        reasons.append(f"reacts+{r}")

    # --- substance links ---
    urls = m.get("urls", [])
    if any(SUBSTANCE_URL_RE.search(u) for u in urls):
        score += 1.5
        reasons.append("substance-link")

    # --- attachments (builds/photos/screenshots) ---
    if m.get("attachments", 0):
        score += 0.8
        reasons.append("attach")

    # --- newsletter keywords ---
    hits = len(set(x.lower() for x in NEWS_RE.findall(content)))
    if hits:
        kb = min(hits, 4) * 0.8
        score += kb
        reasons.append(f"kw×{hits}")

    # --- noise penalties ---
    if NOISE_RE.match(content.strip()):
        score -= 2.0
        reasons.append("noise")
    if urls and all(GIF_RE.search(u) for u in urls) and n < 40:
        score -= 1.5
        reasons.append("gif")

    return round(score, 2), reasons


def main():
    ap = argparse.ArgumentParser(description="Stage-1 mechanical triage.")
    ap.add_argument("raw", help="raw-messages.jsonl")
    ap.add_argument("--authority", default="authority.json")
    ap.add_argument("--top", type=int, default=400)
    ap.add_argument("--per-author-channel", type=int, default=8,
                    help="Max shortlist items per (author, channel) pair, to stop "
                    "one prolific poster flooding from one channel (default 8).")
    ap.add_argument("--out", required=True, help="shortlist JSONL out")
    ap.add_argument("--report", help="human-readable md report (optional)")
    args = ap.parse_args()

    auth = load_authority(args.authority)

    msgs = []
    with open(args.raw, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                msgs.append(json.loads(line))
    print(f"loaded {len(msgs)} raw messages", file=sys.stderr)

    # behavioral authority: anyone who posted in an authoritative channel
    behavioral_authors = set()
    for m in msgs:
        if m.get("channel") in auth["auth_channels"]:
            a = (m.get("author") or "").strip()
            if a:
                behavioral_authors.add(a)
    print(f"behavioral authorities (posted in auth channels): {len(behavioral_authors)}",
          file=sys.stderr)

    scored = []
    for m in msgs:
        s, reasons = score_message(m, auth, behavioral_authors)
        m2 = dict(m)
        m2["_score"] = s
        m2["_reasons"] = reasons
        scored.append(m2)

    scored.sort(key=lambda x: x["_score"], reverse=True)

    # Diversity cap: keep at most --per-author-channel top items per
    # (author, channel) so one prolific person (e.g. an owner posting release
    # candidates) can't flood the shortlist from a single channel. We still get
    # their highest-signal posts, just not 200 near-duplicate dev pings.
    seen = defaultdict(int)
    diversified = []
    overflow = []
    for m in scored:
        key = (m.get("author"), m.get("channel"))
        if seen[key] < args.per_author_channel:
            seen[key] += 1
            diversified.append(m)
        else:
            overflow.append(m)
    # fill up to --top from diversified first, then overflow if short
    top = diversified[: args.top]
    if len(top) < args.top:
        top += overflow[: args.top - len(top)]
    top.sort(key=lambda x: x["_score"], reverse=True)

    with open(args.out, "w", encoding="utf-8") as f:
        for m in top:
            f.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"wrote top {len(top)} to {args.out} "
          f"(score {top[-1]['_score']}..{top[0]['_score']})", file=sys.stderr)

    # per-channel distribution of the shortlist
    bych = defaultdict(int)
    for m in top:
        bych[m["channel"]] += 1
    print("shortlist by channel (top 12):", file=sys.stderr)
    for ch, c in sorted(bych.items(), key=lambda x: -x[1])[:12]:
        print(f"   {c:>4}  #{ch}", file=sys.stderr)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(f"# Stage-1 triage report — top {len(top)} of {len(msgs)}\n\n")
            for m in top:
                snip = (m.get("content", "")[:180]).replace("\n", " ")
                f.write(f"- **{m['_score']}** [#{m['channel']}] {m['author']} "
                        f"({m['ts'][:10]}): {snip}  \n  _{', '.join(m['_reasons'])}_\n")
        print(f"wrote report to {args.report}", file=sys.stderr)


if __name__ == "__main__":
    main()
