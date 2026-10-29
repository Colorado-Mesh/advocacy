<!--
OCTOBER 2026 ISSUE — composed from issues/2026-10/data/candidates-public.json
(Sep 15 – Oct 27 window), PUBLIC channels only. Admin topic suggestions from
#mesh-ops folded in (Mesh Client V6 roundup, "community-run" framing, Western
Slope). EmComm/MECP is the lead + Story of the Month. Prize winner: jfh200.
Facts from gathered data; [CONFIRM: ...] = human-verify before publish.
Bigger than the Sept issue by design. Run dedup-check.py before publishing.
-->

# Colorado Mesh Monthly — October 2026

> Happy almost-Halloween, Colorado. October was the month the mesh started
> thinking hard about *emergencies* — a homegrown protocol for emergency
> comms (MECP), a push into TAK, and a volunteer emergency reporting network —
> all while Mesh Client shipped a monster V6, the map got a faster brain
> (say hello to Beacon), and wardrivers lit up everything from Durango to
> Buena Vista to the back roads off I-25. We've got more to cover than last
> month, so grab a warm drink and settle in. As always, it's sorted so you can
> jump straight to your corner of the mesh.

## 📰 General News

- **Emergency communications took center stage.** A lot of this month's energy went toward making the mesh genuinely useful when it matters most — a new **MECP** (Mesh Emergency Communications Protocol) under active development, and a TAK bridge for situational awareness. The whole thread gets its own Story of the Month below, but it's the throughline of October.
- **Admin team changes.** The leadership team shared a round of updates this month. Several admins stepped down to focus on other priorities — **👀, Dani, strex, Slim, and littlecrab (KFØWBX)** — and we're grateful for everything they put in. Please join us in welcoming **Zeva** to the admin team. The Admin Team handles day-to-day Discord and website operations; together with the Regional Representatives they make up the broader org leadership.
- **One short link to rule them all.** Colorado Mesh now has a tidy set of short links on the `colome.sh` domain: `colome.sh/discord`, `colome.sh/wiki`, `colome.sh/start`, `colome.sh/mcmap` (MeshCore map) and `colome.sh/mtmap` (Meshtastic map), to name a few. Easier to share, easier to remember.
- **Mesh Client v6.0.0 is here** — and it's big enough that it gets its own section below. The short version: new UI, a new BLE implementation, continued Reticulum work, and a lot more.
- **The map got a new engine.** The MeshCore map and analyzer, formerly powered by CoreScope, has been replaced with **Beacon**, a faster, more-performant, purpose-built tool.
- **A new TAK corner of the community.** A dedicated TAK server role and `#tak` channel spun up this month as interest in ATAK integration took off (more in Gear & Firmware).
- **This very newsletter made its debut.** The first Colorado Mesh Monthly (our Aug/Sept catch-up) went live on the blog and the website — thank you for the genuinely warm reception. If you're reading issue two, you're part of the habit now.

## 📅 Events & Meetups

- **A letter went to Rocky Mountain National Park.** JohnnyW5KV wrote to the park superintendent requesting permission to install a mesh repeater, making the case for backcountry communications infrastructure. No word back yet, but it's exactly the kind of ambitious ask that expands what the mesh can be. ([#backcountry-general](https://discord.com/channels/1436156966648152271/))
- **Wardriving keeps filling in the map.** It's an ongoing, year-round effort, and October was a productive stretch: Zeva ran a Grand Junction wardrive with MeshMapper and a weekend sweep that hit **#5 on the MeshMapper leaderboard**; wardrivers picked up fresh coverage along **I-25 and Highway 66**; and new observers lit up in **Durango** and **Buena Vista**. Got a car node? Every drive adds data — the map only gets better the more of us are out there.
- **Weekly Net — every Thursday, all day.** Quick reminder on the rules: a check-in is *any* message on the MeshCore Public channel between 12:00 a.m. and 11:59 p.m. on Thursday — not just the one-hour Discord event.

## 📸 Photo / Video of the Month

Caption: [CONFIRM: pick the hero image — a strong candidate is a wardrive/map screenshot from the Durango or Buena Vista coverage expansion, or a solar-node build photo from #projects-and-builds. Drop the square-cropped image here as ![](photos/<name>_square_web.jpg).]

Honorable mention on the video side: the **Mesh Client V6 walkthrough** is up at https://youtu.be/iRu1FDME0-w — a good watch if you want to see the new version in motion.

## 📶 Meshtastic

- **Hold off on Meshtastic 2.8.** Multiple operators report that 2.8 releases are causing problems, including causing boot loops on Seeed Solar Nodes. If you're on 2.7 and stable, there's no rush to jump. ([#meshtastic](https://discord.com/channels/1436156966648152271/))
- **Firmware 3.0 is on the horizon — and it changes bandwidth allocations.** Meshtastic 3.0 will shift how bandwidth is allocated, with a default LongTurbo preset in the United States. That said, switching to LongTurbo right now isn't recommended due to performance drops.
- **MediumFast adoption is still the slow grind.** Some nodes in Denver are switching to MediumFast, as Colorado Mesh has recommended, but adoption remains slow since most people never change their default settings. This has caused a split between MediumFast and LongFast users. Preset defaults really do shape the whole network. If your area recommends MediumFast, the switch only pays off when neighbors make it too.
- **A clever idea: MediumFast as a backhaul.** Meanwhile, some have floated the idea of using MediumFast as an amplified point-to-point backhaul — super-long links between sites — with local breakouts onto LongFast.
- **The Lookout Mountain bridge is half-alive.** Zeva has a LongFast node and a Wi-Fi bridge up on Lookout Mountain; the goal is to bridge LongFast and MediumFast over serial and echo it all to MQTT. Not finished, but a real step toward tying the high-site plumbing together.
- **Commerce City feeder node is back online.** Live on-mesh Meshtastic data is being collected by a feeder node near the Rocky Mountain Arsenal and published to https://potato.meshtastic.coloradomesh.org. This provides a more holistic view of metro Denver and Fort Collins traffic, not just over-MQTT data.
- **Remote firmware from the mountain.** omgitsgela described a GL.iNet-router-over-ZeroTier setup that serves serial + firmware data to mountaintop nodes, so you can update and reconfigure without the climb. A good pattern for anything hard to reach.

## 🔗 MeshCore

- **CoreScope → Beacon.** The headline for MeshCore tooling this month: Colorado Mesh retired the CoreScope analyzer in favor of **Beacon**, a more efficient, purpose-built map. It lives at https://map.meshcore.coloradomesh.org (the old CoreScope link, https://analyzer.meshcore.coloradomesh.org, automatically redirects to Beacon). Beacon handles packet-ambiguity better than CoreScope, providing more accurate data about the local mesh.
- **Coverage keeps filling in.** The Buena Vista area popped up on the map with a half-dozen repeaters, a new Durango observer is tracking potential inter-state traffic with New Mexico, and wardrivers added I-25 and Highway 66. All repeaters in the area now support multibyte paths, even when their adverts still show single-byte — a real routing improvement.
- **A naming-convention experiment is spreading.** Chicago mesh users have begun trialing a "Chicagoland Naming Convention" that closely follows the Colorado Mesh schema. Nice to see our conventions getting adopted — and stress-tested — beyond state lines.
- **Should Colorado Mesh ship its own firmware?** Admins floated the idea that it might be time for a custom Colorado Mesh MeshCore firmware with enhanced features. An early conversation, but one worth watching.
- **Keep naming nodes to convention.** As the map fills, the [repeater name tool](https://tools.meshcore.coloradomesh.org/repeater_name_tool/) keeps everything legible and, more importantly, helps avoid conflicting public keys.

## 🛰️ Reticulum

- **Reticulum-over-MeshCore gets a working baseline.** Reticulum has been a first-class part of Mesh Client for a while now — the news this month is narrower and more technical: Zeva got a **Reticulum-on-MeshCore** baseline build working (WiFi clients on MeshCore are still failing, Meshtastic testing pending). It's early, but it's another transport combination coming together.
- **NomadNet keeps growing.** Zeva expanded their NomadNet interfaces and added saved-location storage (identifying nodes on connect), and shared the NomadNet-Pages repo for anyone building `.mu` pages: https://github.com/SebastianObi/NomadNet-Pages
- **On the dev bench.** Rin has been poking at Reticulum features — a possible fingerprint-button function, optional userid/password auth on sites — and sharing reference-doc thoughts for developers. The RRC hub remains an active gathering spot; it's still the easiest no-RF on-ramp to the whole hobby.

## 🛠️ Gear & Firmware

A busy month at the workbench — new radios, new bridges, and a few "learn from my mistakes" notes:

- **TAK is the new frontier.** W0RMT released **meshcore-tak-bridge**, which connects a MeshCore companion node to ATAK for full messaging. It's moving fast: **v0.1.2** added direct-message delivery receipts and radio battery monitoring (on-screen percentage plus low-battery alerts at 20% and 10%), and **MECP decoding + map-marker placement now work** in the bridge. A dedicated `#tak` channel and server role appeared to house all of it.
- **A new radio to watch.** The **Radioddity Nodara Meshtastic radio** is out and slated for review (JohnnyW5KV) — product page: https://www.radioddity.com/products/radioddity-nodara-meshtastic-radio
- **RFOXiA — a long-range BLE module that meshes.** A new protocol is being added to Mesh Client to support the RFOXiA BLE module; the manufacturer is sending two units to enable it. Heads-up from Rin: the RFOXiA firmware has a **50-byte message limit** (a compile-time constant, not a BLE/radio limitation), and the docs don't quite match the code yet.
- **A quiet, cheap build tip.** beala released a custom MeshCore build that **disables the LED and buzzer** (great for a silent, low-power node) — https://github.com/beala/MeshCore/releases/tag/t1000e-v1.17.1
- **Still a crowd favorite: the RAK 1W.** JohnnyW5KV again gives the RAK 1W board a thumbs-up for its integrated input/output filters — "an awesome little board for the price." Zeva confirms a 3000 mAh battery pairs with the RAK 1W companion without issues.
- **Solar builds everywhere.** Darin built a first solar node from an ACE Hardware solar light; beala shared a custom LFP + LR2021-carrier charger; UtahSTI stood up a solar repeater (SenseCAP P1-Pro) in Hesperus bound for a rooftop with a 5.8 dBi antenna. Zeva's modular magnetic car-node design continues — there's a 1W low-profile solar car-node model on Printables.
- **Hardware gotcha.** Runr flagged SD-card issues in MuziWorks "batch 1" — the cards are replaceable and a new order has shipped, so check yours if you're on that batch.

## 💻 Get the Mesh Client — now at V6

New here, or still juggling a different app per protocol? The community's free, cross-platform **Mesh Client** (Windows / macOS / Linux) speaks Meshtastic, MeshCore, *and* Reticulum from one window — and **version 6.0.0** just landed with a pile of upgrades. Highlights this cycle:

- A refreshed **user interface** and a new **BLE implementation** (with smarter handling when you've got multiple BLE radios of the same type — the UI now helps you tell which radio you're actually driving).
- **Reticulum support** maturing inside the client, plus ongoing work to decouple the backend from the UI and a clean-room `rnsgit`-in-Rust effort.
- Quality-of-life work on settings migrations and DB upgrades (hence the repeated "please test the next build" calls — thank you to everyone who did).
- A new **V6 walkthrough video**: https://youtu.be/iRu1FDME0-w

Huge thanks to **Joey (NV0N)**, lead developer, and the whole contributor crew — Zeva, Rin, cj, budt W0RMT and more. Grab it (and test builds) at github.com/Colorado-Mesh/mesh-client.

## 🛒 For Sale & Wanted

- No member classifieds came in this month. _Got gear to sell or a part you're hunting for? Drop it in the channel and we'll run it here next issue._

## 📣 Call to Action

**Lend a hand with emergency comms.** This is the month's big ask. A few concrete ways in:
- **Help shape MECP.** The Mesh Emergency Communications Protocol is being designed *now*, and the team is actively looking for emergency communicators to help plan (omgitsgela, an emergency communicator, already jumped in). If you've got EmComm/ICS experience, your input is gold.
- **Build and place nodes where they matter.** omgitsgela is sourcing physical nodes for roughly **$20 each** to push coverage into mountain areas and highway corridors, and is looking for volunteers to build and deploy. High spots and dead corridors are exactly where a new node does the most good.

And the evergreen one: **run an observer in your area**, especially out past the metro. If your region looks empty on the map, it's usually just because nobody's reporting from there yet. The [MeshCore MQTT guide](https://wiki.coloradomesh.org/wiki/MeshCore_MQTT) walks you through it.

## 🌟 Community Spotlight

A few people who moved the mesh this month:

- **budt W0RMT** — a one-person TAK pipeline, shipping the meshcore-tak-bridge, wiring up MECP decoding, and synthesizing community discussion into real documentation.
- **Zeva** — everywhere again: Mesh Client V6, Reticulum integration, Dockerizing the client, a Grand Junction wardrive, a #5 MeshMapper finish, and a steady stream of hardware builds.
- **nwithan8** — Beacon, observer onboarding, and MQTT plumbing.
- **omgitsgela** — EmComm planning energy, the MediumFast-backhaul idea, and a plan to seed $20 nodes into the gaps.

And a warm welcome to everyone who built their first node this month — including **Darin**, whose first solar node came out of an ACE Hardware solar light. That's the spirit.

## 🌐 Around the Web

- **Beacon / MeshCore map** — https://map.meshcore.coloradomesh.org
- **Mesh Client V6 walkthrough (video)** — https://youtu.be/iRu1FDME0-w
- **Rettui (Reticulum TUI) — now with an Android release** by Zeva — https://github.com/zevaryx/rettui/releases
- **MeshMapper app overview** (how the mapping works) — https://wiki.meshmapper.net/app_overview/
- **meshcore-tak-bridge** (MeshCore ↔ ATAK) — https://github.com/Colorado-Mesh/meshcore-tak-bridge
- **Colorado Mesh short links** — https://colome.sh

## 📗 Story of the Month: When the Mesh Grows Up — Emergency Comms

Every hobby network eventually faces the same question: *what is this actually for?* In October, Colorado Mesh started answering it out loud — and the answer kept coming back to emergencies.

The spark is a protocol. There's long been an awkward truth in the mesh world, and Rin said it plainly this month: there are **no real EMCOMM standards for LoRa mesh networks**. The established emergency framework, ICS, assumes infrastructure a mesh simply can't provide. So the community started building its own — **MECP**, the Mesh Emergency Communications Protocol — a structured way to move emergency information over LoRa mesh. It's early and the message volume is already enough that Rin asked for a summary doc just to keep up, but the pieces are moving fast: budt W0RMT already has **MECP decoding and map-marker placement working** inside the meshcore-tak-bridge, which pipes mesh traffic into **ATAK**, the situational-awareness tool a lot of EmComm and SAR folks already live in.

Around that protocol, an ecosystem is forming. omgitsgela — an actual emergency communicator — stepped up to help plan, and is sourcing ~$20 nodes to push coverage into the mountains and highway corridors where cell service dies and a mesh would matter most.

What's striking isn't any single feature — it's the shift in *posture*. A network that spent the summer celebrating its first cross-state-line packet is now asking how it performs on the worst day, not the best one. That's a community growing into its purpose. If you've got ICS or EmComm experience, or just a good high spot and a soldering iron, this is the moment your contribution counts double. The mesh is deciding what it wants to be when it grows up. Come help decide.

## 🔖 Sources & Further Reading

- Join / getting started — https://colome.sh/start
- Website - https://colome.sh
- Discord - https://colome.sh/discord
- MeshCore live map — https://colome.sh/mcmap
- Meshtastic live map — https://colome.sh/mtmap
- MeshCore config tools — https://colome.sh/mctools
- Run a MeshCore observer — https://colome.sh/mcmqtt
- Mesh Client — https://colome.sh/client
- MeshCore Weekly Net check-in — https://colome.sh/mcnet
- Donate to keep the network running — https://colome.sh/donate

## 👋 Until Next Month

That's October — a big one. The mesh is reaching for high spots, new protocols,
and a real role in emergencies, and it's all powered by people deciding their
corner of Colorado belongs on the map. Lit up a repeater? Printed an enclosure?
Ran a killer wardrive? Have EmComm experience to lend? Tell us — it lands in the
next issue. Big or small, we want it.

**😄 Nerd Joke of the Month:** Why did the MeshCore repeater refuse to panic in an emergency? It knew help was only a few hops away.

**🎁 The Prize:** congratulations to **jfh200** 🎉 — our winner this month, drawn at random from everyone who reacted to last month's newsletter announcement in Discord! This month's prize: **[PRIZE TBD — placeholder, admins to fill in]**. Want in next month? **React to this issue's announcement post** and you're entered.

**73** 📻
