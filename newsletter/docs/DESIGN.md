# Colorado Mesh Monthly — Design Document

The single source of truth for how the newsletter looks and what goes in it.
Templates implement this doc; when they disagree, this doc wins. Update it first.

---

## 1. Brand

Assets and palette come from the official repo
**github.com/Colorado-Mesh/branding**, mirrored under `brand/` (see
`brand/SOURCE.md`). Never invent brand colors — use `brand/colors.css` via the
role tokens in `brand.css`.

### Palette (official)
Four families in `brand/colors.css` (1 = lightest → 9 = darkest):
- **Blue** `#16538E … #011033` — the brand's dominant color (the logo is navy).
- **Green** `#76e0a4 … #012821` — secondary.
- **Yellow/Gold** `#F8E7B9 … #A67107` — accent.
- **Red** `#f97699 … #360D18` — sparing use (alerts, for-sale price tags).

### Identity
**Deep navy blue primary · green secondary · gold accent.** The newsletter is a
dark navy flyer. Role tokens (in `brand.css`):
- `--bg #011033` canvas · `--panel #04213f` cards · `--band #010c26` heading bands
- `--primary #16538E` (links/rules) · `--green #4cb578` · `--gold #F2B138`
- `--text #EDEDED` · `--text-dim #9fb4cc`

### Per-protocol accent colors
Each protocol section is color-coded so readers learn the visual shorthand:
- **Meshtastic → green** (`--mt`)
- **MeshCore → brand blue** (`--mc`)
- **Reticulum → gold** (`--rns`)

### Logo
`brand/logo.svg` (logo-v2) in the masthead. Raster fallback `brand/logo_256.png`.
Credits (megabear KD5IHC, Johnny W5KV) live in `brand/SOURCE.md` — no need to
print them each issue, but keep them if a credits/colophon line is added.

## 2. Typography
- System sans stack (portable in Chrome/Browserless). No web-font dependency.
- Masthead title ~26–30pt/800. Section headings ~11–13pt/800. Body ~9.5–10.5pt.
- Ham callsigns and protocol names in body weight; never mangle a callsign.

## 3. Layout / grid
- **Full-bleed dark flyer.** `@page margin:0`; the navy canvas reaches every edge
  on every page (page 1 masthead touches the top).
- **Continuous flow of break-safe ROWS** (NOT css-multicol — multicol ignores
  page-break control and slices sections). Each `.row` = up to two side-by-side
  section cards, `break-inside:avoid`. Big News / Story / protocol lead / signoff
  span full width (`.span2`).
- **Row spacing = top padding** (not bottom margin) so continuation pages keep
  their top clearance (padding survives page breaks; margins collapse). One
  `--rowgap` var controls it everywhere.
- **Section header treatment:** a SOLID heading band (`--band`) + a 2px accent
  divider (protocol color / green / gold). This is what makes header vs body read
  as distinct zones — a faint gradient does NOT (learned the hard way).
- Citations render on their own final page.

## 4. Section taxonomy (Joey NV0N's expanded structure)
Order top → bottom. Skip any section with nothing to report (except the fixed
recurring ones). Each section maps to a CSS class `s-<key>` + a badge.

1. **Masthead** — logo + "Colorado Mesh Monthly" + month + tagline.
2. **Cold open** — 2–4 sentence warm hello + the month's single biggest thing.
3. **📰 General News** (`s-news`) — cross-protocol / org-wide headlines, milestones,
   announcements, community reminders.
4. **📅 Events & Meetups** (`s-events`) — hamfests, club meetings, presentations,
   nets to attend. Include date/time/place.
5. **📸 Photo / Video of the Month** (`s-photo`) — the hero image slot +
   caption/credit. Video = a still/thumbnail + a link.

> **Use photos generously.** Beyond the hero slot, **any section can carry inline
> photos**. Put a markdown image on its own line inside a section:
> `![credit / caption](photos/name_web.jpg)` and it renders as a styled figure
> (embedded, sized to the column, credit beneath). A repeater build in a protocol
> section, a spotlighted node, a summit deployment in the Story — pictures add a
> lot and there's no reason not to. Source them with `tools/fetch-photos.py`
> (downloads image attachments + builds a contact sheet to pick from). Always
> credit the poster; photos are gitignored until credit/permission is settled,
> and only the chosen images ship embedded in the PDF.

6. **PROTOCOL SECTIONS** — the heart of the expanded newsletter. Each is a
   full-width lead card with protocol-colored heading, then its items:
   - **📶 Meshtastic** (`s-mt`, green) — e.g. *MediumFast rollout in Denver*,
     presets, MQTT, device notes.
   - **🔗 MeshCore** (`s-mc`, blue) — e.g. *Scopes*, *Nebraska link*, *DIA bridge*,
     observers, naming convention, firmware.
   - **🛰️ Reticulum** (`s-rns`, gold) — e.g. *RRC server* status, transport nodes,
     RNode usage, bridges.
6a. **🛠️ Gear & Firmware** (`s-gear`) — cross-protocol hardware/firmware news:
   new devices, firmware releases, bug/issue notices, recalls, safety bulletins,
   and buy/build tips worth knowing. Lead with anything urgent (a recall or a
   "don't do X or you'll fry your board" warning). Sourced from #hardware,
   #software, #mesh-client-releases, and the protocol channels.
6b. **💻 Get the Mesh Client** (`s-client`, RECURRING) — a short standing reminder
   that the community's cross-platform Mesh Client app exists, with where to get
   it. Appears every issue (like the Weekly Net reminder), refreshed with any
   notable release news.
7. **🛒 For Sale & Wanted** (`s-market`) — community classifieds; only when there
   are submissions. Format: `FOR SALE`/`WANTED` · item · price/ask · contact handle.
8. **📣 Call to Action** (`s-cta`) — a concrete ask, e.g. "We need Reticulum full
   repeaters in high spots — build yours now!" One or two per issue, actionable.
9. **🌟 Community Spotlight** (`s-spot`) — a person / node / build to celebrate.
10. **📖 New on the Wiki** (`s-wiki`) — pages added/updated (from gather-wiki).
11. **🌐 Around the Web** (`s-web`) — good links that live outside Discord.
12. **📗 Story of the Month** (`s-story`) — one longer featured narrative.
13. **👋 Sign-off** (`s-bye`) — warm goodbye, **Nerd Joke of the Month**, **Prize**
    (random winner from the PREVIOUS issue's reactions; react to enter next month).
14. **🔖 Sources & Further Reading** (`s-cite`) — numbered references, own page.

## 5. Item schema (for the items list + triage)
Each candidate item carries:
- `section` — one of the keys above (`news`, `events`, `photo`, `mt`, `mc`, `rns`,
  `market`, `cta`, `spot`, `wiki`, `web`, `story`).
- `headline` — ≤90 chars, in voice.
- `detail` — 1–2 sentences, facts only.
- `people` — handles/callsigns (exact).
- `source` — `#channel YYYY-MM-DD` or a URL.
- for `market`: `kind` (sale/wanted), `price`, `contact`.

## 6. Voice
See `voice-guide.md` (unchanged): first-person "we", fun + nerdy, warm, RF/ham
flavor, Joke of the Month, "73" sign-off. Protocol sections may get slightly more
technical but stay welcoming.

## 7. Editorial
See `EDITORIAL.md`: humans review; every claim sourced; callsigns exact; no
`[CONFIRM]` markers may remain before publishing.

## 8. Output
- **A single PDF** is the deliverable. `build-pdf.py issues/<month>/draft.md`
  → styled HTML → Browserless /pdf. Write the draft as clean markdown — no
  length limits, no message chunking.
- **Publishing** = share that PDF in Discord (attachment or link) and wherever
  else the community wants it. There is no separate Discord-markdown format.
- Verify PDF pages by rasterizing (pymupdf), not HTML screenshots — screenshots
  don't reflect @page/pagination.
