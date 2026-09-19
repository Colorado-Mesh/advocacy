# Data & Privacy

We want this newsletter's **code and process to be fully transparent** — anyone
can read exactly how issues are made and reproduce the tooling. At the same time,
the community's **raw Discord conversations are not ours to republish**. This doc
explains the line we draw.

## What we DO commit (public)
- **All the code** (`tools/`) — gatherers, triage, PDF builder, dedup check.
- **Templates** (`templates/`) and **brand assets** (`brand/`, from the official
  `Colorado-Mesh/branding` repo).
- **Docs** — `LIFECYCLE.md`, `docs/DESIGN.md`, `docs/EDITORIAL.md`,
  `docs/voice-guide.md`, this file.
- **The finished product** per issue: the reviewed `draft.md` and the published
  `newsletter-<month>.pdf`. These contain only what the editors approved for
  publication.
- **Config that is just IDs**, not content: `tools/discord-guilds.txt` (the guild
  we cover) and `tools/discord-exclude.txt` (channels we skip).

## What we DON'T commit (private)
- **Raw Discord messages** (`issues/*/data/`, `raw-*.jsonl`). These are members'
  conversations. We read them to *find* newsletter topics; we do not republish the
  chat log. Only the summarized, edited, approved result goes public.
- **Triage intermediates** (shortlists, candidate JSON) — they embed message text.
- **Gatherer state** (`.state/state.json`) — operational, not content.
- **Tokens / secrets** — the Discord token is pasted per-run into an environment
  variable and **never written to disk or committed**. Same for the LLM API key.
- **The working items list / pick list** — scratch that can contain raw quotes;
  shared with admins out-of-band, not published.
- **Source photos** — kept local until the pictured person's credit/permission is
  settled per issue; only the chosen, credited image ships inside the PDF.

## Principles
- **Summaries, not transcripts.** The newsletter reports *what happened*, attributed
  and sourced, in the community's own voice — it is not a dump of who said what.
- **Attribute, don't expose.** We credit people by their public handle/callsign and
  never publish real names, locations, or private details beyond what they already
  shared publicly.
- **Consent for spotlights & photos.** Featuring a person or their photo is an
  editorial decision made with their community norms in mind (see `docs/EDITORIAL.md`).
- **Tokens live in the environment only.** Reading Discord uses a token supplied at
  run time via `DISCORD_TOKEN`; it is never persisted. If one is ever exposed, reset it.

## Reproducibility
Everything needed to *run* the pipeline is public. To reproduce an issue you supply
your own Discord read access and LLM endpoint (see `README.md`) — the private inputs
stay yours; the public outputs are what you see here.
