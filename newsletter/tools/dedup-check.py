#!/usr/bin/env python3
"""
dedup-check.py — flag near-duplicate sentences/facts repeated across the
newsletter, so we don't write the same thing twice in different sections.

    ./dedup-check.py issues/2026-09/draft.md
    ./dedup-check.py issues/2026-09/draft.md --threshold 0.5

How: splits the draft into sections (## headings), then into sentences, and
compares every sentence pair across DIFFERENT sections using token Jaccard
similarity (stdlib only, no ML). Pairs above the threshold are reported for a
human to merge/cut. Cross-references to the same URL are also flagged.

Exit code 1 if duplicates are found (so it can gate a build), 0 if clean.
"""
import argparse
import re
import sys
from collections import defaultdict

STOP = set("a an the and or but of to in on at for with from by is are was were "
           "be been being this that these those it its we our you your they their "
           "as so if then than into out up down over under new now got get can will "
           "has have had do does did not no yes i he she them his her — - · also".split())


def sections(md):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
    md = md.replace("--- [message break] ---", "")
    out = []
    cur_head, cur_lines = "(intro)", []
    for line in md.splitlines():
        h = re.match(r"^#{1,3}\s+(.*)", line)
        if h:
            if cur_lines:
                out.append((cur_head, "\n".join(cur_lines)))
            cur_head, cur_lines = h.group(1).strip(), []
        else:
            cur_lines.append(line)
    if cur_lines:
        out.append((cur_head, "\n".join(cur_lines)))
    return out


def sentences(text):
    # strip markdown, bullets, links-to-text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*`>#]", "", text)
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
    text = text.replace("\n", " ")
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if len(p.strip()) > 25]


def tokens(s):
    return set(w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# distinctive tokens = proper-noun-ish / numeric / place-like content words.
# Sharing several of these signals "same fact" even when phrasing differs.
def distinctive(sentence):
    toks = set()
    for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]+", sentence):
        wl = w.lower()
        if wl in STOP or len(w) < 3:
            continue
        # keep capitalized words, mixed-case (callsigns/handles), and anything with a digit
        if w[0].isupper() or any(c.isdigit() for c in w) or not w.islower():
            toks.add(wl)
    return toks


def urls(text):
    return set(re.findall(r"https?://[^\s)\]]+", text))


def main():
    ap = argparse.ArgumentParser(description="Flag repeated facts across the newsletter.")
    ap.add_argument("draft")
    ap.add_argument("--threshold", type=float, default=0.5,
                    help="Jaccard similarity to flag (0-1, default 0.5).")
    ap.add_argument("--min-shared", type=int, default=3,
                    help="Flag if two sentences share >= this many distinctive "
                    "content words (proper nouns/numbers), catching reworded facts (default 3).")
    args = ap.parse_args()

    md = open(args.draft, encoding="utf-8").read()
    secs = sections(md)

    # The Sources / Further Reading section references everything by design —
    # exclude it from cross-section comparison so it doesn't false-positive.
    def is_sources(h):
        return bool(re.search(r"source|further reading|reference", h, re.I))

    # build (section, sentence, tokenset, distinctive-set)
    entries = []
    url_map = defaultdict(list)
    for head, body in secs:
        if is_sources(head):
            continue
        for u in urls(body):
            url_map[u].append(head)
        for s in sentences(body):
            entries.append((head, s, tokens(s), distinctive(s)))

    dupes = []
    for i in range(len(entries)):
        h1, s1, t1, d1 = entries[i]
        for j in range(i + 1, len(entries)):
            h2, s2, t2, d2 = entries[j]
            if h1 == h2:
                continue  # same section — repetition there is the author's call
            sim = jaccard(t1, t2)
            shared_key = d1 & d2
            # flag if phrasing is similar (Jaccard) OR they share >=3 distinctive
            # content words (same fact reworded — e.g. DIA/I-76/Nebraska)
            if sim >= args.threshold or len(shared_key) >= args.min_shared:
                dupes.append((max(sim, len(shared_key) / 10), h1, s1, h2, s2, shared_key))

    dupes.sort(reverse=True, key=lambda x: x[0])

    print(f"Dedup check: {args.draft}\n" + "=" * 60)
    if dupes:
        print(f"\n⚠  {len(dupes)} possible repeated fact(s) across sections:\n")
        for score, h1, s1, h2, s2, shared in dupes:
            print(f"  «{h1}»  vs  «{h2}»"
                  + (f"   [shared: {', '.join(sorted(shared))}]" if shared else ""))
            print(f"      A: {s1[:100]}")
            print(f"      B: {s2[:100]}\n")

    # URLs appearing in more than one non-Sources section
    url_dupes = {u: hs for u, hs in url_map.items()
                 if len([h for h in hs if "source" not in h.lower()]) > 1}
    if url_dupes:
        print("ℹ  Same link cited in multiple sections (ok if intentional):")
        for u, hs in url_dupes.items():
            print(f"   {u}\n     in: {', '.join(hs)}")
        print()

    if not dupes and not url_dupes:
        print("\n✓ No cross-section duplicates found.")
        return 0
    print("Review the pairs above — merge or cut the weaker mention.")
    return 1 if dupes else 0


if __name__ == "__main__":
    sys.exit(main())
