#!/usr/bin/env python3
"""
build-pdf.py — turn a composed newsletter draft (markdown) into a visually
designed PDF, rendered by the homelab Browserless headless Chromium.

    ./build-pdf.py issues/2026-09/draft-SAMPLE.md
    ./build-pdf.py issues/2026-09/draft.md -o issues/2026-09/newsletter.pdf

Pipeline:  draft.md --(parse)--> styled HTML (pdf-template.html) --> Browserless /pdf --> PDF

Notes:
  - Standard library only. Ships its own small markdown->HTML converter so there
    are no pip deps.
  - Strips <!-- comment blocks --> (and any legacy "--- [message break] ---"
    markers, harmlessly, in case an old draft still has them).
    (those are only for the Discord post, not the PDF).
  - Maps each "## <emoji> Section" heading to a styled card + colored badge.
  - Highlights [CONFIRM: ...] markers so reviewers can't miss them.
  - Browserless config is read from env with homelab defaults:
        BROWSERLESS_URL   (default https://browser.cat-compute.com)
        BROWSERLESS_TOKEN (default kiro-browser-2026)
"""
import argparse
import base64
import datetime as dt
import html
import json
import os
import re
import ssl
import sys
import urllib.request

from icons import icon_for, masthead_icon

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "pdf-template.html")
DRAFT_DIR = HERE  # set to the draft's directory in main(); relative image paths resolve here


def _logo_data_uri():
    """Embed the official logo (brand/logo_256.png) as a data URI so the PDF is
    self-contained. Prefer PNG (small, reliable) over the 525KB SVG. Falls back
    to an empty string if the asset is missing."""
    for name in ("brand/logo_256.png", "brand/logo_400.png"):
        p = os.path.join(HERE, name)
        if os.path.isfile(p):
            with open(p, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{b64}"
    return ""


BROWSERLESS_URL = os.environ.get("BROWSERLESS_URL", "https://browser.cat-compute.com")
BROWSERLESS_TOKEN = os.environ.get("BROWSERLESS_TOKEN", "kiro-browser-2026")

# Each rule: (keywords, css_class, icon, zone, kind)
#   zone:  "full"    = full-width row (General News, protocol leads, Story)
#          "col"     = pairs into the 2-column flow (mid sections)
#          "signoff" | "cite"
#   kind:  "normal" | "photo" | "signoff" | "citations"
# Order matters — most specific first. Matches DESIGN.md §4 taxonomy.
SECTION_CLASSES = [
    (("general news",),                     "s-news",   "📰", "full", "normal"),
    (("event", "meetup"),                   "s-events", "📅", "col",  "normal"),
    (("photo", "video"),                    "s-photo",  "📸", "col",  "photo"),
    (("mesh client", "mesh-client"),        "s-client", "💻", "col",  "normal"),
    (("meshtastic",),                       "s-mt",     "📶", "full", "normal"),
    (("meshcore",),                         "s-mc",     "🔗", "full", "normal"),
    (("reticulum",),                        "s-rns",    "🛰️", "full", "normal"),
    (("for sale", "wanted", "classified", "market"), "s-market", "🛒", "col", "normal"),
    (("call to action", "call-to-action", "cta"), "s-cta", "📣", "col", "normal"),
    (("spotlight",),                        "s-spot",   "🌟", "col",  "normal"),
    (("new on the wiki", "wiki"),           "s-wiki",   "📖", "col",  "normal"),
    (("around the web", "web"),             "s-web",    "🌐", "col",  "normal"),
    (("story of the month", "story"),       "s-story",  "📗", "full", "normal"),
    (("sources", "citations", "further reading", "references"),
                                            "s-cite",   "🔖", "cite", "citations"),
    (("until next", "signoff", "goodbye"),  "s-bye",    "👋", "signoff", "signoff"),
    (("general", "news"),                   "s-news",   "📰", "full", "normal"),
]


def classify(heading):
    low = heading.lower()
    for keys, cls, icon, zone, kind in SECTION_CLASSES:
        if any(k in low for k in keys):
            return cls, icon, zone, kind
    return "s-news", "📰", "col", "normal"


# ----------------------------------------------------------- inline markdown ---
def inline_md(text):
    text = html.escape(text)
    # bold, italic, code
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # masked links [text](url)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    # bare urls -> links
    text = re.sub(r'(?<!["\'>])(https?://[^\s<]+)', r'<a href="\1">\1</a>', text)
    # confirm markers
    text = re.sub(r"\[CONFIRM:([^\]]*)\]",
                  r'<span class="confirm">CONFIRM:\1</span>', text)
    return text


def strip_noise(md):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
    md = md.replace("--- [message break] ---", "")
    return md


def parse_sections(md):
    """Split the body into (heading, class, icon, inner_html) cards.

    Everything before the first ## goes into the cold-open (from a > blockquote)
    plus the H1 title (used for the month).
    """
    md = strip_noise(md)
    lines = md.splitlines()

    month = ""
    coldopen = []
    sections = []
    cur = None  # (heading, buffer[])

    def flush():
        if cur:
            sections.append((cur[0], render_block(cur[1]), list(cur[1])))

    pre_first_section = True
    for line in lines:
        h1 = re.match(r"^#\s+(.*)", line)
        h2 = re.match(r"^##\s+(.*)", line)
        if h1:
            title = h1.group(1)
            m = re.search(r"—\s*(.+)$", title)
            month = m.group(1).strip() if m else title
            continue
        if h2:
            flush()
            cur = (h2.group(1).strip(), [])
            pre_first_section = False
            continue
        if pre_first_section:
            bq = re.match(r"^>\s?(.*)", line)
            if bq:
                coldopen.append(bq.group(1))
        else:
            cur[1].append(line)
    flush()
    return month, " ".join(coldopen).strip(), sections


def _embed_image(src):
    """Return an <img>-ready src: a local path becomes a base64 data URI (so the
    PDF is self-contained and Browserless can render it); http(s)/data pass through."""
    if not src.lower().startswith(("http://", "https://", "data:")):
        path = src if os.path.isabs(src) else os.path.join(DRAFT_DIR, src)
        if not os.path.isfile(path):
            path = os.path.join(HERE, src)
        if os.path.isfile(path):
            ext = os.path.splitext(path)[1].lstrip(".").lower()
            mime = "jpeg" if ext in ("jpg", "jpeg") else ext
            with open(path, "rb") as f:
                return f"data:image/{mime};base64,{base64.b64encode(f.read()).decode()}"
    return src


# a markdown image on its own line: ![credit/caption](path-or-url)
_FIG_RE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")


def render_block(lines):
    """Render a section's body lines (lists, paragraphs, inline figures) to HTML.

    An image on its own line — `![credit](path-or-url)` — becomes a styled inline
    figure (embedded, sized to the column, with the credit/caption beneath). This
    lets ANY section carry photos, not just the hero Photo-of-the-Month slot."""
    out = []
    buf_list = []
    buf_para = []

    def close_list():
        nonlocal buf_list
        if buf_list:
            out.append("<ul>" + "".join(f"<li>{inline_md(x)}</li>" for x in buf_list) + "</ul>")
            buf_list = []

    def close_para():
        nonlocal buf_para
        if buf_para:
            out.append("<p>" + inline_md(" ".join(buf_para)) + "</p>")
            buf_para = []

    for line in lines:
        s = line.strip()
        if not s:
            close_list(); close_para(); continue
        fig = _FIG_RE.match(s)
        if fig:
            close_list(); close_para()
            credit, src = fig.group(1).strip(), fig.group(2).strip()
            cap = f'<figcaption>{inline_md(credit)}</figcaption>' if credit else ""
            out.append(f'<figure class="inline-photo">'
                       f'<img src="{_embed_image(src)}" alt="{html.escape(credit)}">{cap}</figure>')
            continue
        li = re.match(r"^[-*]\s+(.*)", s)
        if li:
            close_para()
            buf_list.append(li.group(1))
        elif buf_list:
            # continuation line of the current bullet (wrapped text) — join it
            buf_list[-1] += " " + s
        else:
            buf_para.append(s)
    close_list(); close_para()
    return "\n".join(out)


def render_photo(inner_lines):
    """Photo of the Month: a fixed 16:9 frame. If a line contains an image path
    or URL, embed it; otherwise render an empty placeholder to crop into.
    An optional caption comes from a line starting 'Caption:'."""
    img = None
    caption = ""
    for ln in inner_lines:
        s = ln.strip()
        m = re.search(r'(https?://\S+\.(?:png|jpe?g|gif|webp))', s, re.I)
        mm = re.match(r'!\[[^\]]*\]\(([^)]+)\)', s)  # markdown image
        if mm:
            img = mm.group(1)
        elif m:
            img = m.group(1)
        elif s.lower().startswith("caption:"):
            caption = s.split(":", 1)[1].strip()
    if img:
        frame = f'<div class="frame"><img src="{_embed_image(img)}" alt="Photo of the Month"></div>'
    else:
        frame = ('<div class="frame">Photo / Video of the Month goes here<br>'
                 '<span style="font-size:8.5pt">(drop an image URL in the section and re-render, or crop to fit)</span></div>')
    cap = f'<div class="cap">{inline_md(caption)}</div>' if caption else ''
    return frame + cap


def render_signoff(inner_lines):
    """Signoff: group wrapped lines into paragraphs (blank line = break), then
    style the Joke and Prize paragraphs into their own callout boxes. This keeps
    a joke's punchline and a multi-line prize note together instead of orphaning
    the wrapped continuation lines below."""
    # 1) coalesce wrapped lines into paragraphs
    paras = []
    buf = []
    for ln in inner_lines:
        s = ln.strip()
        if not s:
            if buf:
                paras.append(" ".join(buf)); buf = []
        else:
            buf.append(s)
    if buf:
        paras.append(" ".join(buf))

    # 2) classify each whole paragraph
    out = []
    for p in paras:
        if re.search(r"nerd joke|joke of the month", p, re.I):
            out.append(f'<div class="joke">{inline_md(p)}</div>')
        elif re.search(r"the prize|🎁", p, re.I):
            out.append(f'<div class="prize">{inline_md(p)}</div>')
        elif "73" in p and len(p) < 12:
            out.append(f'<div class="seventythree">{inline_md(p)}</div>')
        else:
            body = p[2:] if p.startswith("- ") else p
            out.append(f'<p>{inline_md(body)}</p>')
    return "\n".join(out)



def render_citations(inner_lines):
    """Citations page: an ordered list of references. Accepts bullet or numbered
    lines; renders raw URLs as links."""
    items = []
    for ln in inner_lines:
        s = ln.strip()
        if not s:
            continue
        s = re.sub(r"^(\d+\.\s+|[-*]\s+)", "", s)  # strip existing numbering/bullets
        items.append(f"<li>{inline_md(s)}</li>")
    return "<ol class='refs'>" + "\n".join(items) + "</ol>"


def _card(cls, icon, heading, inner, span2=False):
    # Strip any leading emoji from the heading text, then use an on-brand SVG
    # glyph in the badge (icons.py) instead of a stock unicode emoji.
    htext = re.sub(r"^[\W\d_]*", "", heading).strip() or heading
    wrapper_cls = ("span2 " + cls) if span2 else ("sec " + cls)
    return (f'<div class="{wrapper_cls}">'
            f'<h2><span class="badge">{icon_for(cls)}</span>{html.escape(htext)}</h2>'
            f'<div class="body">{inner}</div></div>')


def build_html(md):
    month, coldopen, sections = parse_sections(md)
    if not month:
        month = dt.datetime.now().strftime("%B %Y")

    flow = []          # list of (kind, html): kind in {"sec","span2"}
    signoff_html = ""
    cite_html = ""

    for heading, inner_html, inner_lines in sections:
        cls, icon, zone, kind = classify(heading)
        if kind == "photo":
            flow.append(("sec", _card(cls, icon, heading, render_photo(inner_lines))))
        elif kind == "signoff":
            signoff_html = (f'<div class="signoff {cls}">'
                            f'<h2><span class="badge">{icon_for(cls)}</span>'
                            f'{html.escape(re.sub(r"^[\W\d_]*", "", heading).strip())}</h2>'
                            f'<div class="body">{render_signoff(inner_lines)}</div></div>')
        elif kind == "citations":
            cite_html = (f'<div class="citations">'
                         f'<h2><span class="badge">{icon_for("s-cite")}</span>'
                         f'{html.escape(re.sub(r"^[\W\d_]*", "", heading).strip())}</h2>'
                         f'{render_citations(inner_lines)}</div>')
        else:
            span2 = zone == "full"
            flow.append(("span2" if span2 else "sec",
                         _card(cls, icon, heading, inner_html, span2=span2)))

    # Group consecutive regular cards into break-safe 2-up rows so a side-by-side
    # pair stays whole on one page; span2 cards are full-width rows on their own.
    # Each .row has break-inside:avoid, which Chrome's paginator honors (unlike
    # css-multicol), so no section is ever sliced across a page boundary.
    flow_html = []
    buf = []
    def flush_row():
        if buf:
            flow_html.append('<div class="row">' + "".join(buf) + "</div>")
            buf.clear()
    for kind, chtml in flow:
        if kind == "span2":
            flush_row()
            flow_html.append('<div class="row full">' + chtml + "</div>")
        else:
            buf.append(chtml)
            if len(buf) == 2:
                flush_row()
    flush_row()

    cold = f'<div class="coldopen">{inline_md(coldopen)}</div>' if coldopen else ""

    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    return (tpl
            .replace("{{MONTH}}", html.escape(month))
            .replace("{{LOGO}}", _logo_data_uri())
            .replace("{{COLDOPEN}}", cold)
            .replace("{{FLOW}}", "\n".join(flow_html))
            .replace("{{SIGNOFF}}", signoff_html)
            .replace("{{CITATIONS}}", cite_html))


def render_pdf(html_str, out_path):
    payload = json.dumps({
        "html": html_str,
        "options": {"format": "Letter", "printBackground": True,
                    "preferCSSPageSize": True,
                    "margin": {"top": "0", "bottom": "0", "left": "0", "right": "0"}},
    }).encode("utf-8")
    url = f"{BROWSERLESS_URL}/pdf?token={BROWSERLESS_TOKEN}"
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # homelab self-signed-friendly (-k equivalent)
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        data = resp.read()
    if data[:5] != b"%PDF-":
        raise SystemExit(f"Browserless did not return a PDF: {data[:120]!r}")
    with open(out_path, "wb") as f:
        f.write(data)
    return len(data)


def main():
    ap = argparse.ArgumentParser(description="Render a newsletter draft to a styled PDF.")
    ap.add_argument("draft", help="Path to the composed draft markdown.")
    ap.add_argument("-o", "--out", help="Output PDF path (default: alongside draft).")
    ap.add_argument("--html-only", action="store_true",
                    help="Write the intermediate HTML and skip rendering.")
    args = ap.parse_args()

    if not os.path.isfile(args.draft):
        raise SystemExit(f"Draft not found: {args.draft}")
    global DRAFT_DIR
    DRAFT_DIR = os.path.dirname(os.path.abspath(args.draft))
    with open(args.draft, encoding="utf-8") as f:
        md = f.read()

    html_str = build_html(md)

    if args.html_only:
        hp = os.path.splitext(args.out or args.draft)[0] + ".html"
        with open(hp, "w", encoding="utf-8") as f:
            f.write(html_str)
        print(f"Wrote HTML: {hp}")
        return

    out = args.out or (os.path.splitext(args.draft)[0] + ".pdf")
    print(f"Rendering PDF via {BROWSERLESS_URL} ...", file=sys.stderr)
    n = render_pdf(html_str, out)
    print(f"Wrote {out} ({n:,} bytes)")


if __name__ == "__main__":
    main()
