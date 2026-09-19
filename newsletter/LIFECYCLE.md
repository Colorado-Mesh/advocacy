# Newsletter Lifecycle

How an issue of *Colorado Mesh Monthly* goes from raw chatter to a published PDF.

There are two tracks that run in lockstep:
- **Code lifecycle** — the automated pipeline (like CI stages) that produces artifacts.
- **Editorial lifecycle** — the human review gates between stages. Nothing advances
  past a gate without a human's OK.

The whole point: **automation drafts, humans decide.** Every stage has an artifact
you can look at, and every gate is a real chance to change course cheaply — it's
much easier to cut a topic from a list than to rewrite a laid-out PDF.

```
  STAGE                 ARTIFACT                     GATE (who signs off)
  ─────────────────────────────────────────────────────────────────────────
  0. Gather        →    raw messages (LOCAL ONLY)    — (automated, private)
  1. Topics list   →    PICK-LIST.md                 ▸ GATE 1: admins pick topics
  2. Markdown draft→    draft.md                      ▸ GATE 2: editors edit copy
  3. PDF draft     →    draft PDF                     ▸ GATE 3: final look/layout
  4. Publish       →    newsletter-<month>.pdf        ▸ GATE 4: admin approval → ship
```

---

## Stage 0 — Gather  *(automated · private)*
Pull the month's activity. **This is the only stage whose raw output never leaves
the local machine.**
- **Code:** `tools/gather-wiki.py` (wiki, read-only) + `tools/gather-discord.py`
  (Discord, token pasted per-run, never stored). Then `tools/triage-stage1.py`
  (mechanical scoring) → `tools/triage-stage2.py` (LLM clustering via homelab vLLM).
- **Artifact:** `issues/<month>/data/` — raw messages, shortlist, candidates.
  **Git-ignored. Never committed** (see DATA-PRIVACY.md).
- **No gate** — this is plumbing. It feeds Stage 1.

## Stage 1 — Topics List  ▸ **GATE 1: Admins pick the topics**
Turn candidates into a decision-ready list and hand it to the admins FIRST.
- **Code:** `tools/make-pick-list.py` → `issues/<month>/PICK-LIST.md`.
- **Artifact:** `PICK-LIST.md` — every candidate as a checkbox, by section.
- **Gate:** admins tick what belongs in the issue, cut the rest, add anything
  missed, and fix mis-categorization. **Cheapest place to steer the issue.**
  Output: the approved topic set.

## Stage 2 — Markdown Draft  ▸ **GATE 2: Editors edit the copy**
Compose the picked topics into real prose, in the newsletter voice.
- **Code:** composed against `docs/voice-guide.md` + `templates/draft-template.md`,
  reading `issues/<month>/carryover.md` for multi-month threads. Multi-sentence
  detail; `[CONFIRM]` on anything unverified.
- **Artifact:** `issues/<month>/draft.md` — plain markdown, easy for anyone to edit.
- **Gate:** editors rewrite freely, fix tone, resolve every `[CONFIRM]`, and run:
  - `tools/dedup-check.py draft.md` — flags repeated facts across sections.
  - the fact-check checklist in `docs/EDITORIAL.md` (callsigns, attributions, numbers).
  No `[CONFIRM]` markers may remain. Output: approved copy.

## Stage 3 — PDF Draft  ▸ **GATE 3: Final look & layout**
Render the approved markdown into the branded PDF for a visual proof.
- **Code:** `tools/build-pdf.py draft.md` → styled HTML (`templates/pdf-template.html`
  + `brand/`) → Browserless → PDF. Choose the Photo of the Month here.
- **Artifact:** a draft PDF (not the final filename yet).
- **Gate:** proof every page — layout, the photo, no orphaned text, page breaks.
  Small copy fixes loop back to Stage 2 (cheap). Output: layout approved.

## Stage 4 — Publish  ▸ **GATE 4: Admin approval → ship**
Produce the final artifact and release it.
- **Code:** final `tools/build-pdf.py` → `issues/<month>/newsletter-<month>.pdf`.
- **Gate:** an admin gives the final yes.
- **Ship:**
  1. Commit the issue's markdown + final PDF to the advocacy repo (NOT the data/).
  2. Post to Discord (PDF attachment + teaser) in the agreed channel; pin it.
  3. Ask people to REACT (seeds next month's prize draw).
  4. Record the posted message ID; update `carryover.md`.

---

## Feedback loops (where things go backward)
- Gate 1 → back to Stage 1: admins want different topics. Re-issue the pick list.
- Gate 2 → stays in Stage 2: editors rewrite copy directly in the markdown.
- Gate 3 → back to Stage 2: layout looks fine but copy needs a tweak → edit md,
  re-render. Layout-only issues are template changes (rare, affect all issues).
- Gate 4 → back to Stage 3/2: any last "actually, change X" before shipping.

## Cadence
- **Monthly.** Each issue covers the prior month. (The first issue, Aug+Sept 2026,
  is a catch-up covering two months — see that issue's notes.)
- Stage 0 is incremental: the Discord gatherer keeps a high-water mark so each
  month only pulls what's new.

## Who does what
| Role | Stages | Notes |
|---|---|---|
| Kiro (tooling) | 0, and drafts 1–4 | Gathers, triages, composes, renders. Never publishes. |
| Admins | Gate 1, Gate 4 | Pick topics; give final approval. |
| Editors | Gate 2, Gate 3 | Edit copy, resolve CONFIRMs, proof the PDF. |
| Fact-checker (admin) | Gate 2 | Verify callsigns, attributions, numbers. |

See `docs/EDITORIAL.md` for the fact-check standard and `DATA-PRIVACY.md` for what
does and doesn't get committed.
