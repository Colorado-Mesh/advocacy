# Colorado Mesh Monthly

The community newsletter for Colorado Mesh — a once-a-month digest of everything
happening on the mesh (Meshtastic, MeshCore, Reticulum) so nobody has to read
every Discord message to stay in the loop.

This folder holds the **tooling, templates, brand, docs, and published issues**.
The code and process are open on purpose; the raw Discord chatter that feeds it
is not committed (see **[DATA-PRIVACY.md](DATA-PRIVACY.md)**).

## How an issue is made
Five stages with human feedback gates — full detail in **[LIFECYCLE.md](LIFECYCLE.md)**:

```
gather (private) → topics/PICK-LIST ▸admins pick → draft.md ▸editors edit
   → PDF draft ▸final look → publish PDF ▸admin OK → ship
```

**Automation drafts, humans decide.** Kiro gathers/triages/composes/renders;
admins pick topics and give final approval; editors edit copy and proof the PDF.

## Folder map
```
newsletter/
├── LIFECYCLE.md         # the 5-stage production lifecycle + feedback gates
├── DATA-PRIVACY.md      # what's committed vs kept private, and why
├── README.md            # this file
├── tools/               # the pipeline (Python, stdlib-only where possible)
│   ├── gather-wiki.py        # Stage 0: pull wiki changes
│   ├── gather-discord.py     # Stage 0: pull Discord (token per-run, never stored)
│   ├── triage-stage1.py      # Stage 0: mechanical scoring → shortlist
│   ├── triage-stage2.py      # Stage 0: LLM clustering → candidates
│   ├── make-pick-list.py     # Stage 1: candidates → admin PICK-LIST
│   ├── build-pdf.py          # Stage 3/4: draft.md → branded PDF
│   ├── dedup-check.py         # Gate 2: flag repeated facts across sections
│   ├── icons.py              # on-brand inline SVG section icons
│   └── discord-{guilds,exclude}.txt  # which server / which channels to skip
├── templates/           # items-template.md, draft-template.md, pdf-template.html
├── brand/               # official assets from Colorado-Mesh/branding + brand.css
├── docs/                # DESIGN.md, EDITORIAL.md, voice-guide.md
└── issues/<YYYY-MM>/    # per issue: draft.md + newsletter-<month>.pdf (published)
                         #   data/, items-list.md, PICK-LIST.md, photos/ are gitignored
```

## Running the pipeline (reproduce an issue)
Requires Python 3, your own Discord read access, and an LLM endpoint (we use a
self-hosted vLLM). Rendering the PDF uses a headless-Chromium service (Browserless).

```bash
# Stage 0 — gather (raw output stays local, gitignored)
export DISCORD_TOKEN='...'          # pasted per-run, never stored
python tools/gather-wiki.py    --since 2026-10-01 --items issues/2026-10/items-list.md
python tools/gather-discord.py --raw-out issues/2026-10/data/raw.jsonl --items issues/2026-10/items-list.md
python tools/triage-stage1.py  issues/2026-10/data/raw.jsonl --out issues/2026-10/data/shortlist.jsonl
VLLM_API_KEY=... python tools/triage-stage2.py issues/2026-10/data/shortlist.jsonl \
     --items issues/2026-10/items-list.md --out-json issues/2026-10/data/candidates.json

# Stage 1 — topics list for the admins to pick from
python tools/make-pick-list.py issues/2026-10/data/candidates.json \
     --out issues/2026-10/PICK-LIST.md --month "October 2026"

# Stage 2 — compose issues/2026-10/draft.md from the admins' picks (see LIFECYCLE)
python tools/dedup-check.py issues/2026-10/draft.md      # Gate 2

# Stage 3/4 — render the PDF
python tools/build-pdf.py issues/2026-10/draft.md -o issues/2026-10/newsletter-october-2026.pdf
```

Config the tools read from the environment: `DISCORD_TOKEN`, `VLLM_API_KEY`,
`VLLM_BASE_URL`, `VLLM_MODEL`, `BROWSERLESS_URL`, `BROWSERLESS_TOKEN`.

## Contributing
- Got a topic for next month? Drop it in Discord — it'll surface in the pick list.
- Editors/admins: see **[docs/EDITORIAL.md](docs/EDITORIAL.md)** for the fact-check
  standard and roles, and **[docs/DESIGN.md](docs/DESIGN.md)** for the look.
- Built with help from Kiro (AI assistant) for the tooling and drafting; every
  issue is human-reviewed and human-approved before it ships.

## License
MIT, matching the advocacy repo.
