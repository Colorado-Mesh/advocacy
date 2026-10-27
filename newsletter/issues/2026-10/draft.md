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

- **Emergency communications took center stage.** A lot of this month's energy went toward making the mesh genuinely useful when it matters most — a new **MECP** (Mesh Emergency Communications Protocol) under active development, a TAK bridge for situational awareness, and a call for volunteers for the Colorado Emergency Reporting Network. The whole thread gets its own Story of the Month below, but it's the throughline of October.
- **Admin team changes.** The leadership team shared a round of updates this month: several admins stepped down to focus on other priorities — our sincere thanks for everything they put in — and the team welcomed a new admin aboard. The Admin Team handles day-to-day Discord and website operations; together with the Regional Representatives they make up the broader org leadership. [CONFIRM: whether to name the departing/incoming admins or keep it general — defer to the announcement's wording.]
- **One short link to rule them all.** Colorado Mesh now has a tidy set of short links on the `colome.sh` domain: `colome.sh` → main site, `colome.sh/discord`, `colome.sh/wiki`, `colome.sh/start` (getting-started), `colome.sh/mcmap` (the MeshCore map). Easier to share, easier to remember.
- **Mesh Client v6.0.0 is here** — and it's big enough that it gets its own section below. The short version: new UI, a new BLE implementation, Reticulum support, and a lot more.
- **The map got a new engine.** The MeshCore analyzer formerly known as CoreScope has been replaced by **Beacon**, a faster, purpose-built app. The old CoreScope URL now redirects to Beacon at https://map.meshcore.coloradomesh.org.
- **A new TAK corner of the community.** A dedicated TAK server role and `#tak` channel spun up this month as interest in ATAK integration took off (more in Gear & Firmware).
- **This very newsletter made its debut.** The first Colorado Mesh Monthly (our Aug/Sept catch-up) went live on the blog and the website — thank you for the genuinely warm reception. If you're reading issue two, you're part of the habit now.

## 📅 Events & Meetups

- **Parker Radio Association Chili Cookout.** PRA hosted a chili cookout for members and families on 80 acres in Franktown — and it pulled in **5–6 new members from the Colorado Mesh community**. Club membership is $25/year. More at www.parkerradio.org. [CONFIRM date if we want to print it.]
- **A letter went to Rocky Mountain National Park.** JohnnyW5KV wrote to the park superintendent requesting permission to install a mesh repeater, making the case for backcountry communications infrastructure. No word back yet, but it's exactly the kind of ambitious ask that expands what the mesh can be. ([#backcountry-general](https://discord.com/channels/1436156966648152271/))
- **Wardriving season is in full swing.** Zeva ran a Grand Junction wardrive with MeshMapper and a weekend sweep that hit **#5 on the MeshMapper leaderboard**; wardrivers picked up fresh coverage along **I-25 and Highway 66**; and new observers lit up in **Durango** and **Buena Vista** (a half-dozen new repeaters on the map there alone). If you've got a car node, this is the month to drive.
- **Weekly Net — every Thursday, all day.** Quick reminder on the rules: a check-in is *any* message on the MeshCore Public channel between 12:00 a.m. and 11:59 p.m. on Thursday — not just the one-hour Discord event. nwithan8 noted most regular check-ins are showing strong "green dot" coverage (seen by many nodes), with isolated exceptions out in Pueblo and the western slope.

## 📸 Photo / Video of the Month

Caption: [CONFIRM: pick the hero image — a strong candidate is a wardrive/map screenshot from the Durango or Buena Vista coverage expansion, or a solar-node build photo from #projects-and-builds. Drop the square-cropped image here as ![](photos/<name>_square_web.jpg).]

Honorable mention on the video side: the **Mesh Client V6 walkthrough** is up at https://youtu.be/iRu1FDME0-w — a good watch if you want to see the new version in motion.

## 📶 Meshtastic

- **A firmware warning worth heeding: hold off on Meshtastic 2.8.** Multiple operators report that *every* 2.8 release (including nightlies) is causing problems, and **2.8 on Seeed Solar Nodes specifically causes boot loops** — discovered the hard way. The 2.7 line is still behaving. If you're on 2.7 and stable, there's no rush to jump. ([#meshtastic](https://discord.com/channels/1436156966648152271/))
- **Firmware 3.0 is on the horizon — and it changes bandwidth allocations.** omgitsgela notes that 3.0 will shift how bandwidth is allocated, and that switching to LongTurbo right now isn't recommended due to performance drops. The advice: wait for 3.0 before making big preset changes. [CONFIRM 3.0 specifics before printing as fact.]
- **MediumFast adoption is still the slow grind.** A node in the Denver south suburbs switched to MediumFast as recommended but wasn't seeing other nodes — and JohnnyW5KV put his finger on why: most people never change their defaults, so traffic splits between whoever's on MediumFast and whoever stayed on LongFast. Preset defaults really do shape the whole network. If your area recommends MediumFast, the switch only pays off when neighbors make it too.
- **A clever idea: MediumFast as a backhaul.** omgitsgela floated using MediumFast as an amplified point-to-point backhaul — super-long links between sites — with local breakouts onto LongFast. They're already running an amplifier on a MediumFast node (but not the paired LongFast one) to keep an overloaded LongFast repeater from drowning in channel utilization. Interesting blueprint for extending reach without clogging the local air.
- **The Lookout Mountain bridge is half-alive.** Zeva has a LongFast node and a WiFi bridge up on Lookout; the goal is to bridge LongFast and MediumFast over serial and echo it all to MQTT. Not finished, but a real step toward tying the high-site plumbing together.
- **Commerce City feeder node is back online**, pushing live on-mesh Meshtastic data again — handy for tracking nodes and messages across the metro.
- **Remote firmware from the mountain.** omgitsgela described a GL.iNet-router-over-ZeroTier setup that serves serial + firmware data to mountaintop nodes, so you can update and reconfigure without the climb. A good pattern for anything hard to reach.

## 🔗 MeshCore

- **CoreScope → Beacon.** The headline for MeshCore tooling this month: nwithan8 retired the CoreScope analyzer in favor of **Beacon**, a more efficient, purpose-built map. It lives at https://map.meshcore.coloradomesh.org (the old link redirects). nwithan8 also walked through how Beacon resolves packet-ambiguity on the map, and there's an open feature request for a "save my favorites" function — feedback welcome.
- **A "Stale" repeater mystery, solved.** If MeshMapper has been flipping your repeater between online and "Stale" for no reason: it's a timing mismatch. MeshMapper looks for an advert within a 24-hour window, but **MeshCore firmware 1.16.0+ only advertises repeaters every 47 hours** — so a perfectly healthy repeater can look stale between adverts. Known issue, not your hardware. ([#wardriving](https://discord.com/channels/1436156966648152271/))
- **Coverage keeps filling in.** Buena Vista picked up a half-dozen repeaters, a Durango observer is tracking heavy traffic (https://map.meshcore.coloradomesh.org/?tab=Packets&iata=DRO), and wardrivers added I-25 and Highway 66. beala confirmed that **all repeaters in the area now support multibyte paths** even when their adverts still show single-byte — a real routing improvement.
- **A naming-convention experiment is spreading.** Ed kicked off a trial of a "Chicagoland Naming Convention" that closely follows the Colorado Mesh scheme with a couple of tweaks (like swapping the trailing hash for a "personalization block"). Nice to see our conventions getting adopted — and stress-tested — beyond state lines.
- **Should Colorado Mesh ship its own firmware?** Zeva floated the idea that it might be time for a custom Colorado Mesh MeshCore firmware with enhanced features. Nightcrawler already maintains a custom repeater build (on GitHub, with the OpenHop-style advert/policy filtering), so the raw materials are there. Early conversation — worth watching.
- **Keep naming nodes to convention.** As the map fills, the [repeater name tool](https://tools.meshcore.coloradomesh.org/repeater_name_tool/) keeps everything legible. Rachel also updated the wiki with location-based best practices for configuring repeaters.

## 🛰️ Reticulum

- **Reticulum is landing inside Mesh Client.** Zeva got a Reticulum baseline working on MeshCore within the client (WiFi clients on MeshCore are still failing, Meshtastic testing is pending) — part of the V6 push to make the client a true three-protocol window. Expect this to keep maturing fast.
- **Setting up an observer on Reticulum.** nwithan8 posted instructions for standing up a Colorado Mesh observer over Reticulum, tied to the MQTT setup guide — another low-effort way to put your area on the map.
- **NomadNet keeps growing.** Zeva expanded their NomadNet interfaces and added saved-location storage (identifying nodes on connect), and shared the NomadNet-Pages repo for anyone building `.mu` pages: https://github.com/SebastianObi/NomadNet-Pages
- **On the dev bench.** Rin has been poking at Reticulum features — a possible fingerprint-button function, optional userid/password auth on sites — and sharing reference-doc thoughts for developers. The RRC hub remains an active gathering spot; it's still the easiest no-RF on-ramp to the whole hobby.

## 🛠️ Gear & Firmware

A busy month at the workbench — new radios, new bridges, and a few "learn from my mistakes" notes:

- **TAK is the new frontier.** budt W0RMT released **meshcore-tak-bridge**, which connects a MeshCore companion node to ATAK for full messaging. It's moving fast: **v0.1.2** added direct-message delivery receipts and radio battery monitoring (on-screen percentage plus low-battery alerts at 20% and 10%), and **MECP decoding + map-marker placement now work** in the bridge. A dedicated `#tak` channel and server role appeared to house all of it.
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
- **Volunteer for the Colorado Emergency Reporting Network** — nwithan8 put out the call; details at https://co-cern.org/.
- **Help shape MECP.** The Mesh Emergency Communications Protocol is being designed *now*, and the team is actively looking for emergency communicators to help plan (omgitsgela, an emergency communicator, already jumped in). If you've got EmComm/ICS experience, your input is gold.
- **Build and place nodes where they matter.** omgitsgela is sourcing physical nodes for roughly **$20 each** to push coverage into mountain areas and highway corridors, and is looking for volunteers to build and deploy. High spots and dead corridors are exactly where a new node does the most good.

And the evergreen one: **run an observer in your area**, especially out past the metro. If your region looks empty on the map, it's usually just because nobody's reporting from there yet. The [MeshCore MQTT guide](https://wiki.coloradomesh.org/wiki/MeshCore_MQTT) walks you through it.

## 🌟 Community Spotlight

A few people who moved the mesh this month:

- **budt W0RMT** — a one-person TAK pipeline, shipping the meshcore-tak-bridge, wiring up MECP decoding, and synthesizing community discussion into real documentation.
- **Zeva** — everywhere again: Mesh Client V6, Reticulum integration, Dockerizing the client, a Grand Junction wardrive, a #5 MeshMapper finish, and a steady stream of hardware builds.
- **nwithan8** — Beacon, observer onboarding, MQTT plumbing, and the Emergency Reporting Network call.
- **omgitsgela** — EmComm planning energy, the MediumFast-backhaul idea, and a plan to seed $20 nodes into the gaps.

And a warm welcome to everyone who built their first node this month — including **Darin**, whose first solar node came out of an ACE Hardware solar light. That's the spirit.

## 🌐 Around the Web

- **Beacon / MeshCore map** — https://map.meshcore.coloradomesh.org
- **Colorado Emergency Reporting Network** — https://co-cern.org/
- **Mesh Client V6 walkthrough (video)** — https://youtu.be/iRu1FDME0-w
- **Rettui (Reticulum TUI) — now with an Android release** by Zeva — https://github.com/zevaryx/rettui/releases
- **MeshMapper app overview** (how the mapping works) — https://wiki.meshmapper.net/app_overview/
- **meshcore-tak-bridge** (MeshCore ↔ ATAK) — [CONFIRM repo link before printing]
- **Colorado Mesh short links** — https://colome.sh

## 📗 Story of the Month: When the Mesh Grows Up — Emergency Comms

Every hobby network eventually faces the same question: *what is this actually for?* In October, Colorado Mesh started answering it out loud — and the answer kept coming back to emergencies.

The spark is a protocol. There's long been an awkward truth in the mesh world, and Rin said it plainly this month: there are **no real EMCOMM standards for LoRa mesh networks**. The established emergency framework, ICS, assumes infrastructure a mesh simply can't provide. So the community started building its own — **MECP**, the Mesh Emergency Communications Protocol — a structured way to move emergency information over LoRa mesh. It's early and the message volume is already enough that Rin asked for a summary doc just to keep up, but the pieces are moving fast: budt W0RMT already has **MECP decoding and map-marker placement working** inside the meshcore-tak-bridge, which pipes mesh traffic into **ATAK**, the situational-awareness tool a lot of EmComm and SAR folks already live in.

Around that protocol, an ecosystem is forming. nwithan8 put out a call for volunteers for the **Colorado Emergency Reporting Network** (co-cern.org). omgitsgela — an actual emergency communicator — stepped up to help plan, and is sourcing ~$20 nodes to push coverage into the mountains and highway corridors where cell service dies and a mesh would matter most. There's talk of VPN-tunneled distributed compute to keep things running when the normal internet doesn't.

What's striking isn't any single feature — it's the shift in *posture*. A network that spent the summer celebrating its first cross-state-line packet is now asking how it performs on the worst day, not the best one. That's a community growing into its purpose. If you've got ICS or EmComm experience, or just a good high spot and a soldering iron, this is the moment your contribution counts double. The mesh is deciding what it wants to be when it grows up. Come help decide.

## 🔖 Sources & Further Reading

- Beacon / MeshCore live map — https://map.meshcore.coloradomesh.org
- Meshtastic live map — https://map.meshtastic.coloradomesh.org
- MeshCore config tools — https://tools.meshcore.coloradomesh.org
- Running an observer (wiki) — https://wiki.coloradomesh.org/wiki/MeshCore_MQTT
- Colorado Emergency Reporting Network — https://co-cern.org/
- Mesh Client — https://github.com/Colorado-Mesh/mesh-client
- Colorado Mesh short links — https://colome.sh
- Weekly Net check-in — https://weekly-net.meshcore.coloradomesh.org
- Donate to keep the network running — https://coloradomesh.org/donate
- Join / getting started — https://colome.sh/start

## 👋 Until Next Month

That's October — a big one. The mesh is reaching for high spots, new protocols,
and a real role in emergencies, and it's all powered by people deciding their
corner of Colorado belongs on the map. Lit up a repeater? Printed an enclosure?
Ran a killer wardrive? Have EmComm experience to lend? Tell us — it lands in the
next issue. Big or small, we want it.

**😄 Nerd Joke of the Month:** Why did the MeshCore repeater refuse to panic in an emergency? It knew help was only a few hops away.

**🎁 The Prize:** congratulations to **jfh200** 🎉 — our winner this month, drawn at random from everyone who reacted to last month's newsletter announcement in Discord! [CONFIRM prize item for this issue.] Want in next month? **React to this issue's announcement post** and you're entered.

**73** 📻
