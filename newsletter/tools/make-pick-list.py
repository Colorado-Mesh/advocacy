#!/usr/bin/env python3
"""
make-pick-list.py — Stage 1 of the lifecycle. Turn triaged candidates
(candidates JSON from triage-stage2.py) into an admin-facing PICK-LIST.md:
a curated, sectioned list with a checkbox per item so admins choose what goes
in the issue BEFORE we compose. See LIFECYCLE.md (Stage 1 / Gate 1).

    ./make-pick-list.py issues/2026-10/data/candidates.json \
        --out issues/2026-10/PICK-LIST.md --month "October 2026"

Curated (capped per section, richest candidates first) so it's decision-ready
rather than an overwhelming dump; the full pool stays in the candidates JSON.
"""
import argparse
import json
import re

SEC_TITLES = {
    "news": "General News", "events": "Events & Meetups", "mt": "Meshtastic",
    "mc": "MeshCore", "rns": "Reticulum", "gear": "Gear & Firmware", "market": "For Sale & Wanted",
    "cta": "Call to Action", "spot": "Community Spotlight", "web": "Around the Web",
    "story": "Story of the Month candidates",
}
ORDER = ["news", "events", "mt", "mc", "rns", "gear", "market", "cta", "spot", "web", "story"]
CAP = {"mt": 12, "mc": 12, "rns": 9, "gear": 10, "spot": 8, "events": 8, "news": 8,
       "cta": 6, "market": 5, "web": 5, "story": 4}


def dedup(items):
    seen, out = set(), []
    for it in items:
        k = (it.get("headline", "")[:40]).lower()
        if k not in seen:
            seen.add(k); out.append(it)
    return out


def score(it):
    s = len(it.get("detail", ""))
    if it.get("people"):
        s += 40
    if re.search(r"https?://", it.get("detail", "") + it.get("source", "")):
        s += 30
    return s


def main():
    ap = argparse.ArgumentParser(description="Build an admin pick-list from triaged candidates.")
    ap.add_argument("candidates", help="candidates JSON from triage-stage2.py")
    ap.add_argument("--out", required=True)
    ap.add_argument("--month", required=True, help='e.g. "October 2026"')
    args = ap.parse_args()

    g = json.load(open(args.candidates, encoding="utf-8"))
    L = [f"# Newsletter Pick List — {args.month}\n",
         "Admins: this is a **curated candidate pool** triaged from the month's Discord",
         "activity + the wiki. Tick what you want, ignore the rest, add anything we missed.",
         "We compose the newsletter from your picks (LIFECYCLE.md, Gate 1).\n",
         "- [ ] blank = skip · [x] = include · edit the text freely\n",
         "_Sections are best-effort; if something's mis-filed just note it — we'll re-file._",
         "_Top candidates per section shown; the full pool is in the candidates JSON._\n"]

    shown = 0
    for sec in ORDER:
        items = sorted(dedup(g.get(sec, [])), key=score, reverse=True)[: CAP.get(sec, 10)]
        if not items:
            continue
        L.append(f"\n## {SEC_TITLES[sec]}\n")
        for it in items:
            shown += 1
            det = re.sub(r"\s+", " ", it.get("detail", "")).strip()
            meta = " · ".join(x for x in [", ".join(it.get("people", [])[:3]),
                                          it.get("source", "")] if x)
            L.append(f"- [ ] **{it.get('headline', '').strip()}** — {det}"
                     + (f"  _({meta})_" if meta else ""))
        L.append("- [ ] _add one:_ ")

    L += ["\n---\n## Recurring / fixed (auto-included unless you say otherwise)",
          "- [x] **Get the Mesh Client** reminder (Joey NV0N's cross-protocol app)",
          "- [x] **Weekly Net reminder** (Thursdays, post to Public)",
          "- [x] **Photo of the Month**",
          "- [x] **The Prize**",
          "- [x] **Nerd Joke of the Month**, **Cold open**, **Sources** (auto-built)",
          "\n## Anything big we missed? Add it here:", "- [ ] "]

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"wrote {args.out} ({shown} candidates shown)")


if __name__ == "__main__":
    main()
