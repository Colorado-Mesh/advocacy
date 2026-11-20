#!/usr/bin/env python3
"""Convert a newsletter draft (markdown) into clean, wrapped plain text.

The plain-text version is for pasting into Discord, email, mailing lists, or
anywhere markdown will not render. No dependencies.

Usage:
    ./md-to-text.py issues/2026-11/draft.md                 # writes next to the draft
    ./md-to-text.py issues/2026-11/draft.md -o out.txt
    ./md-to-text.py issues/2026-11/draft.md --width 100

What it does:
  - drops HTML comments (editorial notes)
  - H1 becomes an upper-case title with "=" underline, H2 an upper-case
    heading with "-" underline
  - removes bold/italic/code markers
  - [text](url) becomes "text (url)"; a bare link stays as the url
  - images become "[Image: alt text]" (the file is not embedded in text)
  - wraps paragraphs and bullets at --width columns (default 78)
"""
import argparse
import os
import re
import textwrap


def strip_inline(s: str) -> str:
    # images first, so the "!" form does not become a link
    s = re.sub(r"!\[([^\]]*)\]\([^)]*\)", lambda m: f"[Image: {m.group(1)}]" if m.group(1) else "[Image]", s)
    # links: [text](url) -> text (url), or just url when text is the url
    def link(m):
        text, url = m.group(1).strip(), m.group(2).strip()
        return url if text == url or not text else f"{text} ({url})"
    s = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"<(https?://[^>]+)>", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", s)
    s = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    return s


def convert(md: str, width: int) -> str:
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    out, para = [], []

    def flush():
        if para:
            text = strip_inline(" ".join(p.strip() for p in para))
            out.append(textwrap.fill(text, width=width, break_long_words=False, break_on_hyphens=False))
            out.append("")
            para.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            title = strip_inline(m.group(2)).strip()
            if len(m.group(1)) == 1:
                title = title.upper()
                out += [title, "=" * min(len(title), width), ""]
            else:
                title = title.upper()
                out += [title, "-" * min(len(title), width), ""]
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            flush()
            text = strip_inline(m.group(1))
            out.append(textwrap.fill(text, width=width, initial_indent="- ", subsequent_indent="  ",
                                     break_long_words=False, break_on_hyphens=False))
            out.append("")
            continue
        m = re.match(r"^>\s?(.*)$", line)
        if m:
            para.append(m.group(1))
            continue
        para.append(line)
    flush()
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft", help="Path to the markdown draft.")
    ap.add_argument("-o", "--out", help="Output .txt path (default: next to the draft).")
    ap.add_argument("--width", type=int, default=78)
    a = ap.parse_args()
    with open(a.draft, encoding="utf-8") as f:
        text = convert(f.read(), a.width)
    out = a.out or os.path.splitext(a.draft)[0] + ".txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {out} ({len(text):,} chars, {text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
