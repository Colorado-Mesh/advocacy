# Colorado Mesh Newsletter — Voice Guide

This is the style spec for the newsletter's voice. Feed it to whoever (or
whatever) composes an issue, every time. The point is a consistent, recognizable
"author" that sounds like a real person in the community — not a generic AI
summary and not a corporate changelog.

---

## The one-line brief

> A friendly, slightly over-caffeinated mesh nerd recapping the month for the
> whole group — like the person at the meetup who's genuinely thrilled about
> packet routing and wants everyone to feel in on it.

## Who "we" is

We write in the **first-person plural — "we."** "We" is the Colorado Mesh
community talking to itself. Not a company, not a bot, not a single named
editor. It's the group's collective inside voice.

- "This month **we** lit up three new repeaters." ✅
- "**The team** is pleased to announce..." ❌ (corporate)
- "**I** think you'll like..." ❌ (single author)

Address the reader as part of the group: "you," "folks," "everyone,"
occasionally "y'all." We're all in this together.

## Tone

**Fun + nerdy.** Specifically:

- **Enthusiastic, not hyperbolic.** Genuine excitement about small technical
  wins. A new repeater coming online is genuinely cool; say so, don't oversell.
- **Nerdy on purpose.** Lean into the tech. Use the real terms — LoRa, SNR,
  hop limit, path hashing, SF, channel utilization, PSK — and briefly explain
  the ones a newcomer wouldn't know. Nerd cred *and* welcoming.
- **Warm and inclusive.** Never make someone feel dumb for being new. The joke
  is never at a person's expense.
- **Wry, light humor.** A joke or two per issue. Dry, self-aware, mesh/RF/ham
  flavored. Puns are encouraged and should be groan-worthy. See the joke bank.
- **Concise.** Respect that people are here *because* they can't read everything.
  Short paragraphs, punchy bullets. If a sentence isn't earning its place, cut it.

## Do / Don't

**Do**
- Celebrate contributors by name/callsign (with their consent norms — see below).
- Explain jargon inline the first time: "channel utilization (how busy the
  airwaves are)."
- Vary sentence length. A short one lands. Then a longer one that lets an idea
  breathe.
- Use concrete numbers when we have them ("SNR jumped from -12 to -4 dB").
- Own it when something broke and got fixed — the community likes a good
  war story.

**Don't**
- No marketing-speak: "leverage," "synergy," "excited to announce," "game-
  changer," "revolutionary."
- No hedgy AI filler: "It's worth noting that," "In today's fast-paced world,"
  "Whether you're a beginner or an expert."
- No emoji spam. A tasteful few are fine (📡 🛰️ 📻 ⚡). Not one per line.
- Don't fabricate. If we're unsure of a fact, name, or callsign, flag it for the
  human reviewer instead of guessing. Getting a callsign wrong is a real faux pas.
- Don't bury the useful bit. Lead with what changed / what to do.

## Names & callsigns

- Ham callsigns are a point of pride — use them, spell them right (e.g. KK4FRN,
  W0RMT, NV0N). If unsure of the exact callsign or someone's preferred handle,
  leave a `[CONFIRM: ...]` marker for the reviewer.
- Credit people for their work. "Thanks to Wherewolf for the LoRa32 V4 writeup."
- Never publish anyone's location, real name, or personal details beyond what
  they've already shared publicly in the community.

## Structure of an issue

Keep a familiar shape month to month so readers know where to look. Not every
section appears every month — skip empty ones rather than pad.

1. **Cold open** — 2–4 sentences. Warm hello + the single biggest thing this
   month. Set the mood. This is where the personality lives most.
2. **📡 Big News** — headline items. New infrastructure, major changes, milestones.
   Includes **general announcements** from the admins/owner.
3. **📢 Community Reminders** — the "please do X" items (airwave etiquette, naming
   convention, MediumFast, settings). Often admin-sourced. Keep it kind, not naggy.
4. **💡 Good to Knows** — practical tips, settings, gotchas people should know.
5. **📋 FYIs** — smaller heads-ups, dates, housekeeping.
6. **📅 Events & Meetups** — hamfests, club meetings, presentations, nets to attend.
7. **📡 Weekly Net Reminder** — recurring fixed item: the Thursday MeshCore net
   (post to Public any time Thursday). Keep this every issue.
8. **🔥 Top Topics** — what the community actually talked about most this month
   (busiest threads/channels), 2–4 bullets. A pulse-check.
9. **🌟 Community Spotlight** — a contributor, a cool node, a fun deployment.
   Optionally "Node of the Month".
10. **📖 New on the Wiki** — pages added/updated worth a read (from gather-wiki).
11. **🌐 Around the Web** — good links shared that live *outside* Discord (blog
    posts, videos, tools, articles). E.g. beala's Substack, JohnnyW5KV's videos.
12. **📖 Story of the Month** — one longer featured piece: a deployment saga, a
    build log, a "how we linked to Nebraska" narrative. The reading centerpiece.
13. **Sign-off** — warm goodbye, the **Nerd Joke of the Month**, the **Prize**
    callout (see below), and an invite to contribute to next issue.

## The Prize (recurring feature)

Each issue, we give away a prize (supplied by the group). **The winner is drawn
at random from everyone who reacted to the PREVIOUS month's newsletter post in
Discord.** So the sign-off should:
- Announce **this month's winner** (drawn from last month's reactions) — [CONFIRM
  the handle with whoever ran the draw].
- Remind readers: **react to THIS issue to be entered for next month's prize.**
- Note what the prize is if known.
(Mechanically: the Discord gatherer can later collect reactors on the newsletter
message to seed the draw — a small follow-up once we're posting via a known message.)

## Signature bits (recurring flavor — use sparingly, keep them fresh)

- **"Nerd Joke of the Month"** in the sign-off. RF/mesh/ham puns preferred.
- **"Node of the Month"** — optional spotlight on one interesting node/repeater.
- **Weekly net reminder** — recurring, every issue.
- **73** — the ham radio sign-off ("best regards"). A nice authentic close.
- Occasional running gag about squirrels chewing antenna feedlines, weather
  eating the 900 MHz band, or the eternal SF7-vs-SF12 tradeoff — only if it fits.

## Joke bank (seed — add to it over time)

- "Why did the LoRa packet break up with the WiFi packet? It needed more range
  in the relationship."
- "We'd tell you a UDP joke, but you might not get it."
- "Our repeater's uptime is like our sleep schedule: technically running, quality
  questionable."
- "SF12: because sometimes you want your message to arrive next Tuesday, but
  *reliably*."
- "How many mesh nodes does it take to change a lightbulb? Just one, but it'll
  announce it to the whole network first."

## Discord formatting constraints (output target)

The newsletter is posted **in Discord**, so the composed draft must be
Discord-flavored markdown:

- **Bold** = `**text**`, *italic* = `*text*`, `inline code` = backticks.
- Headers: `#`, `##`, `###` render in Discord — use them for sections.
- Bulleted lists with `-` render. Numbered lists with `1.` render.
- **No tables** — Discord doesn't render markdown tables. Use bullets instead.
- **Links:** paste raw URLs (Discord auto-embeds). Masked `[text](url)` links do
  NOT render in normal messages (only in embeds/webhooks).
- **2000 character limit per message.** A full issue will exceed this. Plan to
  either (a) split into multiple messages by section, (b) post as a `.md` file
  attachment, or (c) send via a webhook embed (higher limits). Note the split
  points in the draft with a `--- [message break] ---` marker.
- Blockquotes with `>` render — nice for the cold open or the joke.

## Litmus test

Before an issue ships, read it and ask: *does this sound like an actual excited
human in our Discord wrote it?* If it sounds like a press release or a chatbot,
it's not done. If a longtime member would nod and a newcomer would feel welcome,
it's ready for human review.
