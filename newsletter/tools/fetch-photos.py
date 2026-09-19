#!/usr/bin/env python3
"""
fetch-photos.py — pull candidate photos for an issue from the gathered raw data,
make web-sized copies, and build a contact sheet so editors pick images in a
browser. Complements the "more pictures" goal: any section can carry a photo.

    ./fetch-photos.py issues/2026-10/data/raw.jsonl \
        --out issues/2026-10/photos --min-reactions 1

Only pulls image attachments the gatherer captured (rec["images"]). Downloads
to <out>/, writes <name>_web.jpg (max 1600px) for embedding, and a
contact-sheet.html grouped by channel with caption + credit + suggested
markdown you can paste into the draft.

Photos are gitignored (kept local until credit/permission is settled per issue);
only the chosen images end up embedded in the published PDF.
"""
import argparse
import json
import os
import re
import urllib.request

PHOTO_CHANNELS = {  # channels where photos tend to be newsworthy
    "projects-and-builds", "pictures", "meshcore", "meshtastic", "reticulum",
    "hardware", "mesh-planning", "denver", "pueblo", "colorado-springs",
    "western-slope", "aurora", "introductions", "wardriving",
}


def sanitize(s):
    return re.sub(r"[^A-Za-z0-9._-]", "_", s)[:60]


def main():
    ap = argparse.ArgumentParser(description="Fetch candidate photos for an issue.")
    ap.add_argument("raw", help="raw-messages.jsonl from gather-discord.py")
    ap.add_argument("--out", required=True, help="output photos/ dir")
    ap.add_argument("--min-reactions", type=int, default=0,
                    help="only messages with >= this many reactions (default 0).")
    ap.add_argument("--channels", help="comma list to restrict (default: photo-worthy set).")
    ap.add_argument("--max", type=int, default=60, help="cap total photos fetched.")
    args = ap.parse_args()

    try:
        from PIL import Image
    except ImportError:
        raise SystemExit("Pillow required: pip install pillow")

    chans = set(args.channels.split(",")) if args.channels else PHOTO_CHANNELS
    os.makedirs(args.out, exist_ok=True)

    rows = [json.loads(l) for l in open(args.raw, encoding="utf-8") if l.strip()]
    # candidates: messages with images, in photo channels, meeting the reaction bar
    cands = []
    for m in rows:
        if not m.get("images"):
            continue
        if m.get("channel") not in chans:
            continue
        if m.get("reactions", 0) < args.min_reactions:
            continue
        cands.append(m)
    # richest first: reactions, then a caption present
    cands.sort(key=lambda m: (m.get("reactions", 0), len(m.get("content", ""))), reverse=True)

    entries = []
    count = 0
    for m in cands:
        if count >= args.max:
            break
        for i, img in enumerate(m["images"]):
            if count >= args.max:
                break
            url = img.get("url")
            if not url:
                continue
            base = f"{m['ts'][:10]}_{sanitize(m['author'])}_{count}"
            raw_path = os.path.join(args.out, base + ".jpg")
            web_path = os.path.join(args.out, base + "_web.jpg")
            try:
                data = urllib.request.urlopen(
                    urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
                    timeout=30).read()
                with open(raw_path, "wb") as f:
                    f.write(data)
                im = Image.open(raw_path).convert("RGB")
                w, h = im.size
                im.thumbnail((1600, 1600))
                im.save(web_path, "JPEG", quality=85)
            except Exception as e:
                print(f"  skip {url[:60]}: {e}", flush=True)
                continue
            entries.append({
                "web": os.path.basename(web_path), "raw": os.path.basename(raw_path),
                "author": m["author"], "channel": m["channel"], "ts": m["ts"][:10],
                "caption": re.sub(r"\s+", " ", m.get("content", "")).strip()[:160],
                "w": w, "h": h, "orient": "portrait" if h > w else "landscape",
            })
            count += 1

    # contact sheet
    css = ("body{background:#011033;color:#EDEDED;font-family:sans-serif;padding:22px}"
           "h1{color:#F2B138}figure{display:inline-block;margin:10px;width:300px;vertical-align:top}"
           "img{width:300px;border:2px solid #103a63;border-radius:8px}"
           "figcaption{font-size:12px;margin-top:4px;color:#bcd2e6}"
           "code{background:#04213f;color:#F8E7B9;padding:1px 4px;border-radius:3px;font-size:11px}")
    html = [f"<!doctype html><meta charset=utf-8><style>{css}</style>",
            f"<h1>Photo candidates — {len(entries)} images</h1>",
            "<p>Pick one, copy the markdown under it into the draft section where it belongs.</p>"]
    for e in entries:
        md = f'![{e["author"]} — {e["channel"]}](photos/{e["web"]})'
        html.append(
            f'<figure><img src="{e["web"]}">'
            f'<figcaption><b>{e["author"]}</b> · #{e["channel"]} · {e["ts"]} · {e["orient"]}<br>'
            f'{e["caption"] or "(no caption)"}<br><code>{md}</code></figcaption></figure>')
    with open(os.path.join(args.out, "contact-sheet.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"fetched {len(entries)} photos to {args.out}/")
    print(f"open {args.out}/contact-sheet.html to pick")


if __name__ == "__main__":
    main()
