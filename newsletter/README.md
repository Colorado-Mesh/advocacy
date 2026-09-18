# Colorado Mesh Monthly Newsletter

A monthly newsletter for the Colorado Mesh community. Covers the big and the
small: updates, good-to-knows, FYIs, community spotlights, and a joke or two.

The goal: nobody can read every Discord message, wiki edit, and news drop — so
we digest a month of activity into one friendly, nerdy read.

## The workflow

```
  [wiki API]  ─┐
  [Discord]   ─┼─► gather ─► items-list.md ─► flesh ─► draft.md ─► PDF (styled, Browserless)
  [our notes] ─┘  (+state)   (auto + human)   out
                     ▲
                 carryover.md (multi-month thread memory)
                             HUMANS review before the PDF ships (shared in Discord)
```

1. **Gather** — run the gatherer scripts to pull activity since we last looked.
   - `gather-wiki.py` — recent changes + new pages from wiki.coloradomesh.org
     (read-only, no credentials needed).
   - `gather-discord.py` — **auto-discovers every channel your token can read**
     across all servers, and remembers a per-channel high-water mark in
     `state.json` so each run pulls only what's new (nothing missed, nothing
     duplicated — even for threads that span months). Token pasted each run,
     never stored. See its header for usage.
   - Both **inject markdown** into the month's items list between anchors.
2. **Carryover memory** — `carryover.md` tracks multi-month threads (a repeater
   build, an event, a running debate) so continuity survives across issues. Read
   it when composing; update it after.
3. **Items list** — `issues/<YYYY-MM>/items-list.md` is the shared scratchpad.
   Auto-gathered items land in the "Gathered" sections; we and the admins add our
   own under "Human-contributed". Each item is a one-liner with a source + date.
4. **Compose** — turn the fleshed-out items list into a real draft. Use
   `voice-guide.md` as the style spec and `draft-template.md` as the skeleton.
   Read `carryover.md` first. Kiro can draft this; a human always reviews.
5. **Review** — a human (and ideally an admin) reads the draft, fixes any facts,
   names, or callsigns, resolves every `[CONFIRM: ...]` marker, and approves.
   Follow the fact-check checklist in `EDITORIAL.md`. This step never gets
   skipped — it's a public community publication. Pick the **Photo of the Month**
   and make sure notable claims have links (the **Sources & Further Reading**
   page collects the "read more" references).
6. **Publish — the PDF is the deliverable:**
   - `./build-pdf.py issues/<YYYY-MM>/draft.md` renders a designed, magazine-style
     PDF via the homelab Browserless headless Chromium.
   - Share that PDF in Discord (attachment or link) and wherever else the community
     wants it. There's no separate Discord-markdown format.

## Triage: 24k messages → a curated shortlist (the monthly heavy lift)

A deep backfill returns tens of thousands of messages — too many to read. Two
stages funnel it down. Runs monthly, so it's fine to spend real compute.

```bash
# Stage 1 — mechanical, free, fully explainable. Scores every raw message by
# author authority (authority.json), reactions, channel, links, keywords, etc.
# and keeps the top few hundred. A per-(author,channel) cap stops one prolific
# poster flooding the shortlist.
./triage-stage1.py issues/2026-09/data/raw-messages.jsonl \
    --authority authority.json --top 400 --per-author-channel 8 \
    --out issues/2026-09/data/shortlist.jsonl \
    --report issues/2026-09/data/stage1-report.md

# Stage 2 — LLM (homelab vLLM / Qwen3-8B). Clusters the shortlist into distinct,
# sectioned, attributed newsletter candidates and writes them into the items
# list's candidate sections. Facts-only, [CONFIRM] on anything shaky.
KEY=$(grep '^VLLM_API_KEY=' ~/chats/colorado-mesh-bot/.env | cut -d= -f2)
VLLM_API_KEY=$KEY ./triage-stage2.py issues/2026-09/data/shortlist.jsonl \
    --items issues/2026-09/items-list.md \
    --out-json issues/2026-09/data/candidates.json
```

**Authority weighting:** the Discord user token can't list guild members, so
`authority.json` is a curated operator map (owner/admin/regional-rep/operator)
plus a behavioral signal (posting in admin-gated channels). Edit it as we learn
who's who — it directly shapes what floats to "Big News".

**Qwen3 gotcha:** `/no_think` must be the FIRST thing in the user message or the
model spends its whole budget "thinking" and never emits JSON.

## First run vs. every run (Discord)

Scope is locked to **Colorado Mesh only** (`discord-guilds.txt`) so the token's
other servers are never touched. Discovery runs every time, so **new channels
are picked up automatically** and **deleted/renamed channels are flagged** in a
"🔀 Channel changes since last run" note at the top of the gathered items.

```bash
export DISCORD_TOKEN='...'          # grabbed from the Discord web app, this shell only

# FIRST run — reach back further, since conversations predate this month.
# Raise the per-channel cap so very active channels (e.g. #meshcore) come back
# in one pass instead of catching up over several runs.
./gather-discord.py --backfill-days 180 --max-per-channel 20000

# EVERY run after — pulls only what's new since last time (state.json):
./gather-discord.py
```

Notes:
- `state.json` holds a per-channel high-water mark. Quiet channels advance their
  mark to "now" so empty windows aren't rescanned.
- The default `--max-per-channel` is 2000. If a channel has more new messages
  than the cap, the rest arrives on the next run (nothing is lost).
- A "➖ Channel gone" notice means a channel was deleted, renamed, newly
  excluded, or access was revoked — its entry stays in `state.json` until you
  remove it.


## Files

| File | Purpose |
|---|---|
| `README.md` | This file. |
| `EDITORIAL.md` | The editorial process — roles, fact-check checklist, sourcing standard, corrections. Read before publishing. |
| `voice-guide.md` | The custom newsletter voice — fun + nerdy, first-person "we". |
| `carryover.md` | Long-term memory of multi-month threads. |
| `items-template.md` | Blank template for a month's items list. |
| `draft-template.md` | Blank template for a composed newsletter draft. |
| `pdf-template.html` | Styled HTML template for the PDF (edit the CSS to restyle). |
| `gather-wiki.py` | Pull recent wiki activity into the items list. |
| `gather-discord.py` | Auto-discover + pull all readable Discord channels (stateful). Use `--raw-out` to persist messages for triage. |
| `triage-stage1.py` | Mechanical scorer: raw messages → ranked shortlist (role/reactions/links/keywords). |
| `triage-stage2.py` | LLM (vLLM/Qwen3-8B) clusters the shortlist into sectioned newsletter candidates. |
| `authority.json` | Curated operator/authority map that weights whose messages matter most. |
| `discord-guilds.txt` | Guild ALLOW-LIST — only these servers are ever touched (Colorado Mesh). |
| `discord-exclude.txt` | Channel IDs you *can* read but don't want in the newsletter. |
| `build-pdf.py` | Render a draft to a designed PDF via Browserless. |
| `state.json` | Per-channel high-water marks (created on first Discord run). |
| `issues/<YYYY-MM>/` | Per-issue working folder (items list, draft, PDF). |

## Principles

- **Humans decide what ships.** The tooling gathers and drafts; it never posts.
- **Attribute and date everything** in the items list so review is easy.
- **The voice stays consistent** — always compose against `voice-guide.md`.
- **Small stuff counts.** A one-line "good to know" is as welcome as big news.
