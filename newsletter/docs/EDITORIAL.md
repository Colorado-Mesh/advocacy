# Editorial Process — Colorado Mesh Monthly

This is a public, community-facing publication. That means we hold it to real
editorial standards: nothing goes out that hasn't been fact-checked, sourced,
and read by a human. This doc is the process.

## Principles

1. **Accuracy over speed.** A wrong callsign, a misattributed build, or a
   garbled fact erodes trust. When unsure, cut it or mark it `[CONFIRM]`.
2. **Every claim is sourced.** If we say "X happened," we can point to where —
   a Discord message, a wiki edit, a repo, a post. The Sources page and inline
   links exist so readers can verify and go deeper.
3. **People are credited, and never exposed.** Use handles/callsigns exactly.
   Never publish anyone's real name, address, or private details beyond what
   they've already shared publicly.
4. **Humans decide what ships.** The pipeline gathers, scores, and drafts. It
   never posts. A person — ideally with an admin — approves every issue.
5. **The voice stays consistent.** Always compose against `voice-guide.md`.

## Roles

| Role | Who | Does |
|---|---|---|
| **Gatherer** | Kiro (automated) | Runs the monthly gather + triage, produces the items list and a first draft. |
| **Editor** | A designated community member | Owns the issue: curates items, writes/edits copy, resolves every `[CONFIRM]`, runs the checklist, approves. |
| **Fact-checker** | An admin/operator (ideally) | Verifies the Big News, Community Reminders, and any claim about infrastructure, people, or numbers. |
| **Publisher** | Editor or admin | Posts the approved issue to Discord and attaches the PDF; runs the prize draw. |

For a small team, one person can wear several hats — but **at least two sets of
eyes** should see an issue before it posts (editor + one admin), especially the
Big News and anything with a callsign.

## The monthly workflow

1. **Gather** (Kiro): wiki + Discord, incremental since last issue.
   `./gather-wiki.py` and `./gather-discord.py`
2. **Triage** (Kiro): score + LLM-cluster into candidates.
   `./triage-stage1.py …` then `./triage-stage2.py …`
3. **Pick list** (Kiro → Admins): FIRST STEP each month. Generate a curated,
   sectioned candidate list (`issues/<month>/PICK-LIST.md`) with a checkbox per
   item, and hand it to the admins. THEY decide what goes in, cut what doesn't,
   and add anything missed — before we compose. This keeps editorial control with
   the community and catches mis-categorization early.
4. **Draft** (Kiro): compose `issues/<month>/draft.md` from the admins' PICKS
   (+ wiki + `carryover.md`), in the voice, with `[CONFIRM]` on anything unverified.
5. **Curate** (Editor): tighten, reorder, add any last shout-outs.
6. **Fact-check** (Fact-checker): work the checklist below. This is the gate.
7. **Photo + citations** (Editor): choose the Photo of the Month; make sure every
   notable claim has a link or a Sources entry.
7. **Render** (Editor): `./build-pdf.py issues/<month>/draft.md`; proofread the PDF.
8. **Approve** (Editor + admin): sign off. Only now is it publishable.
9. **Publish** (Publisher): post to Discord (chunk-by-chunk or the PDF), pin it.
10. **Prize** (Publisher): draw last month's winner from prior-issue reactions;
    announce; remind people to react to enter for next month.
11. **Carryover** (Editor): update `carryover.md` — close resolved threads, add
    new ongoing ones.

## Fact-check checklist (the gate before publishing)

Resolve **every** item before approving. No `[CONFIRM]` markers may remain.

- [ ] **Callsigns & handles** spelled exactly right, matched to the right person.
- [ ] **Every Big News item** is traceable to a real source (link it).
- [ ] **Numbers** (member counts, distances, elevations, dates) verified.
- [ ] **Attribution** correct — the right person credited for each build/tool/repeater.
- [ ] **Community Reminders** reflect what admins actually asked (link the post).
- [ ] **Events** have correct date / time / place (or are marked tentative).
- [ ] **Links work** and point where they claim to.
- [ ] **No private info** — names, addresses, anything not already public.
- [ ] **No unverified rumor** — if it can't be sourced, it's cut, not softened.
- [ ] **Tone** passes the voice-guide litmus test (sounds like a real human).
- [ ] **Prize** winner (if any) confirmed with whoever ran the draw.

## Sourcing standard

- Prefer a **public, durable link** (wiki page, repo, blog, coloradomesh.org).
- Discord message links are fine for provenance but many readers can't open them
  — so summarize the fact and point to a durable source where one exists.
- Everything in the draft comes from **gathered data**. The composer must not
  invent details; if a fact isn't in the items list, it doesn't go in.
- The **Sources & Further Reading** page collects the "read more" links. Aim for
  8–15 quality references per issue.

## Corrections

If we get something wrong after publishing, we fix it: post a brief correction
in the channel and, if the PDF is hosted, re-render and replace it. Owning a
mistake plainly is part of being trustworthy.

## What the automation may and may not do

- **May:** gather, score, cluster, draft, render, suggest.
- **May not:** post publicly, invent facts, publish an unverified callsign, or
  skip the human gate. Those are human calls, every time.
