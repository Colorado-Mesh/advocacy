#!/usr/bin/env python3
"""
triage-stage2.py — LLM clustering/summarization of the stage-1 shortlist into
curated newsletter candidate items, using the homelab vLLM (Qwen3-8B).

    KEY=$(grep '^VLLM_API_KEY=' ~/chats/colorado-mesh-bot/.env | cut -d= -f2)
    VLLM_API_KEY=$KEY ./triage-stage2.py issues/2026-09/data/shortlist.jsonl \
        --items issues/2026-09/items-list.md

What it does:
  - Batches the shortlist into context-sized chunks (Qwen3-8B = 16k tokens).
  - For each chunk, asks the model to extract DISTINCT newsletter-worthy items,
    each tagged to a section (big / gtk / fyi / spotlight), summarized in the
    newsletter voice, with people + source (channel/date) + a confidence flag.
  - Merges + de-dupes across chunks, then injects grouped candidates into the
    items-list candidate sections (between the human-review markers).

Guardrails baked into the prompt:
  - Only use facts present in the provided messages. No fabrication.
  - Preserve callsigns/handles exactly; flag anything uncertain with [CONFIRM].
  - Prefer operator/admin-sourced items for "big news" (role weight already in
    the shortlist ordering + each item carries its author).

Env:
  VLLM_BASE_URL (default http://172.16.1.247:8000/v1)
  VLLM_MODEL    (default Qwen/Qwen3-8B)
  VLLM_API_KEY  (required)
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request

BASE = os.environ.get("VLLM_BASE_URL", "http://172.16.1.247:8000/v1")
MODEL = os.environ.get("VLLM_MODEL", "Qwen/Qwen3-8B")
KEY = os.environ.get("VLLM_API_KEY", "")

SYSTEM = """You are the editorial assistant for the Colorado Mesh community newsletter.
You read raw Discord messages and extract DISTINCT newsletter-worthy items.

Rules:
- Use ONLY facts present in the messages. Never invent details, names, or outcomes.
- Preserve callsigns/handles EXACTLY as written. If a fact, name, or callsign is
  uncertain, append " [CONFIRM]" to that part.
- Voice: warm, nerdy, first-person plural ("we", the community). No marketing-speak.
- Merge near-duplicate messages about the same event into ONE item. Do NOT repeat
  the same fact in two items.
- Skip pure chatter, off-topic banter, and one-line reactions.
- WRITE WITH DEPTH: each item's detail should be 2-4 full sentences that actually
  explain what happened, why it matters, and any specifics (numbers, places,
  people). If a topic had a lot of discussion, write more (up to ~6 sentences).
  Do not pad — but do not reduce a rich thread to one thin line either.

Classify each item into exactly one section (protocol sections are important):
  "news"  = cross-protocol / org-wide news, milestones, announcements, reminders
  "events"= hamfests, club meetings, presentations, nets (with date/place)
  "mt"    = Meshtastic-specific (MediumFast rollout, presets, MQTT, devices)
  "mc"    = MeshCore-specific (scopes, Nebraska/DIA links, observers, firmware, naming)
  "rns"   = Reticulum-specific (RRC server, transport nodes, RNode, bridges)
  "gear"  = hardware/firmware news: new devices, firmware releases, bug/issue
            notices, recalls, safety bulletins, buy/build tips (cross-protocol)
  "market"= for-sale / wanted classifieds (include price/ask + contact if present)
  "cta"   = a concrete call to action / ask of the community
  "spot"  = a person / node / build worth celebrating
  "web"   = a notable link that lives OUTSIDE Discord (blog, video, tool, article)
  "story" = a longer narrative worth featuring

Return STRICT JSON: an object with key "items" whose value is an array of:
  {"section":"news|events|mt|mc|rns|gear|market|cta|spot|web|story",
   "headline":"<=90 char summary in the newsletter voice",
   "detail":"2-4 sentences (more if the topic warrants), facts only",
   "people":["handles/callsigns involved"],
   "source":"#channel YYYY-MM-DD"}
Return ONLY the JSON object, nothing else."""


def strip_think(text):
    # Qwen3 emits <think>...</think>; remove it, then grab the JSON object.
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


def extract_json(text):
    text = strip_think(text)
    # find the outermost {...}
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return None
    blob = text[start:end + 1]
    try:
        return json.loads(blob)
    except json.JSONDecodeError:
        # sometimes trailing commas / fences; try a light cleanup
        blob = re.sub(r",\s*([}\]])", r"\1", blob)
        try:
            return json.loads(blob)
        except json.JSONDecodeError:
            return None


def call_llm(messages, max_tokens=4000, retries=3):
    payload = json.dumps({
        "model": MODEL, "messages": messages,
        "max_tokens": max_tokens, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(BASE + "/chat/completions", data=payload,
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Content-Type": "application/json"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                d = json.load(r)
            return d["choices"][0]["message"]["content"]
        except Exception as e:
            if attempt == retries - 1:
                raise
            print(f"    LLM retry {attempt+1} ({e})", file=sys.stderr)
            time.sleep(3)


def chunk_shortlist(msgs, per_chunk):
    for i in range(0, len(msgs), per_chunk):
        yield msgs[i:i + per_chunk]


def format_chunk(chunk):
    lines = []
    for m in chunk:
        c = (m.get("content", "") or "").replace("\n", " ").strip()
        if len(c) > 400:
            c = c[:400] + "…"
        lines.append(f"[#{m['channel']} {m['ts'][:10]}] {m['author']}: {c}")
    return "\n".join(lines)


def inject_candidates(items_path, grouped):
    with open(items_path, encoding="utf-8") as f:
        text = f.read()

    sec_markers = {
        "big": "## 📡 Big News (candidates) `#big`",
        "gtk": "## 💡 Good to Knows (candidates) `#gtk`",
        "fyi": "## 📋 FYIs (candidates) `#fyi`",
        "spotlight": "## 🌟 Community Spotlight (candidates) `#spotlight`",
    }
    for sec, header in sec_markers.items():
        if header not in text:
            continue
        bullets = []
        for it in grouped.get(sec, []):
            people = (" — " + ", ".join(it["people"])) if it.get("people") else ""
            src = f" _({it.get('source','')})_" if it.get("source") else ""
            line = f"- [ ] **{it['headline']}** {it.get('detail','')}{people}{src}"
            bullets.append(line)
        block = header + "\n_LLM-clustered from the shortlist. Verify facts + callsigns before publishing._\n\n" + \
            ("\n".join(bullets) if bullets else "- [ ] ") + "\n"
        # replace from this header up to the next "## " heading
        pat = re.compile(re.escape(header) + r".*?(?=\n## )", re.DOTALL)
        text = pat.sub(block + "\n", text, count=1)

    with open(items_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser(description="Stage-2 LLM triage into newsletter candidates.")
    ap.add_argument("shortlist")
    ap.add_argument("--items", required=True)
    ap.add_argument("--per-chunk", type=int, default=40)
    ap.add_argument("--out-json", help="also save merged candidates JSON")
    ap.add_argument("--max-chunks", type=int, help="limit chunks (for a quick test)")
    args = ap.parse_args()

    if not KEY:
        raise SystemExit("VLLM_API_KEY not set.")

    msgs = [json.loads(l) for l in open(args.shortlist, encoding="utf-8") if l.strip()]
    print(f"shortlist: {len(msgs)} items", file=sys.stderr)

    all_items = []
    chunks = list(chunk_shortlist(msgs, args.per_chunk))
    if args.max_chunks:
        chunks = chunks[: args.max_chunks]
    for i, chunk in enumerate(chunks, 1):
        print(f"  chunk {i}/{len(chunks)} ({len(chunk)} msgs) -> LLM", file=sys.stderr)
        user = ("/no_think\n"
                "Extract newsletter items from these messages. "
                "Higher-authority authors (admins/operators) tend to signal bigger news.\n\n"
                + format_chunk(chunk))
        out = call_llm([{"role": "system", "content": SYSTEM},
                        {"role": "user", "content": user}])
        parsed = extract_json(out or "")
        if not parsed or "items" not in parsed:
            print(f"    ! chunk {i} returned no parseable items", file=sys.stderr)
            continue
        all_items.extend(parsed["items"])
        print(f"    +{len(parsed['items'])} items", file=sys.stderr)

    # de-dupe by (section, headline lowercased first 50 chars)
    SECTIONS = ["news", "events", "mt", "mc", "rns", "gear", "market", "cta", "spot", "web", "story"]
    seen = set()
    grouped = {s: [] for s in SECTIONS}
    for it in all_items:
        sec = it.get("section", "news")
        if sec not in grouped:
            sec = "news"
        key = (sec, (it.get("headline", "")[:50]).lower())
        if key in seen:
            continue
        seen.add(key)
        grouped[sec].append(it)

    total = sum(len(v) for v in grouped.values())
    print(f"merged: {total} distinct candidates (" +
          ", ".join(f"{s}={len(grouped[s])}" for s in SECTIONS if grouped[s]) + ")",
          file=sys.stderr)

    if args.out_json:
        json.dump(grouped, open(args.out_json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)

    inject_candidates(args.items, grouped)
    print(f"injected candidates into {args.items}", file=sys.stderr)


if __name__ == "__main__":
    main()
