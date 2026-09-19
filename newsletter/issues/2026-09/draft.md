<!--
FIRST ISSUE (Aug + Sept 2026 catch-up) — composed from candidates-aug-sep.json
(Aug 1 – Sep 16 window). Facts from gathered data; bracketed CONFIRM notes below = human-verify.
Deeper multi-sentence detail per DESIGN.md. Run dedup-check.py before publishing.
Future issues scope to the single prior month.
-->

# Colorado Mesh Monthly — August & September 2026

> Hey folks, and welcome to the very first Colorado Mesh Monthly. Since this is
> our kickoff and we're publishing mid-month, we're reaching back across both
> August and September so nobody misses the good stuff. Going forward this lands
> once a month — but for now, settle in: it was a huge two months. We linked the
> mesh across state lines into Nebraska, kept pushing the Denver metro onto
> MediumFast, started seriously mapping out regional "scopes," and welcomed a
> genuinely wonderful flood of new operators. Here's the recap, sorted by protocol
> so you can jump straight to your corner of the mesh.

## General News

- **We crossed over 1,000 Discord members**, and the pace of new arrivals hasn't slowed. Between August and September the introductions channel was one of the busiest in the whole server. If you're new: welcome, and don't be shy about asking where to put your first node.
- **A community reminder on airtime etiquette.** As the network grows, the public channels saw a spike in automated traffic — bots broadcasting every few seconds, plus the occasional commercial or crypto spam. Rin (R-4) asked everyone to keep automated messages to no more than once every few hours (a once-a-morning weather post is fine; every 30 minutes is not), and to keep commercial broadcasts off the public channels entirely. LoRa airtime is tiny and shared by everyone, so a little restraint keeps the whole mesh usable.
- **A community configuration tool consolidation.** The group standardized on https://tools.meshcore.coloradomesh.org as the primary config tool and deprecated the older site, streamlining how people set up and manage nodes.
- **A town hall may be in the works.** Zeva floated the idea of an online town hall to make up for the lack of recent in-person gatherings, and JohnnyW5KV has been vocal about wanting regular meetups. Nothing's scheduled yet — but if the interest is there, say so in the channels and help shape the format.
- **Coverage keeps pushing west.** More repeaters are going up around Grand Junction and the western slope, steadily filling in a part of the state that was thin not long ago. If you're out that way, an observer or a well-placed node goes a long way — coordinate in [#western-slope](https://discord.com/channels/1436156966648152271/1436159632090333304).
- **New areas, more voices.** Traffic has been strong across the regional channels, and the community keeps carving out new regional homes as the map fills in. Whichever corner of Colorado you're in, there's probably a channel for it now.

## Events & Meetups

- **BARCFest — October 4 (Boulder Amateur Radio Club).** Colorado Mesh has **two tables reserved** at BARCFest, the Boulder Amateur Radio Club's hamfest — come find us, meet the people behind the callsigns, and see the gear in person. There's also been talk of asking BARC about hosting a mesh repeater on one of their tower sites, so it may be more than a social visit. Details: https://barcw0dk.wordpress.com
- **We had a strong showing at the RMHAM Summer Swapfest (Aug 23)** — a good turnout at our tables and a lot of great conversations with folks new to the mesh. Thanks to everyone who staffed it.

![Colorado Mesh at the RMHAM Summer Swapfest, Aug 23 (photo: JohnC)](photos/event_2026-09-17_JohnC_2_web.jpg)

![The Colorado Mesh table at the RMHAM Summer Swapfest (photo: JohnnyW5KV)](photos/event_2026-09-17_JohnnyW5KV_1_web.jpg)
- **Parker Radio Association** held its monthly meeting on September 7 with a presentation on AllStar (via JohnnyW5KV). Keep an eye on announcements for the next one.
- **Weekly Net — every Thursday.** There's no dedicated channel: just post to the MeshCore Public channel any time on Thursday and you're checked in. New this cycle, Old Man Malice wired the net into MeshWars so your check-in earns credit there too.

## Photo / Video of the Month

![Mt Blue Sky summit](photos/bluesky_b_web.jpg)
Caption: On the summit of Mt Blue Sky (14,130 ft), M0TH3R logged which repeaters heard — and were heard by — a node at the top of Colorado. Photo: M0TH3R, Aug 31. [Two landscape options (B/C) and a portrait (A) are in issues/2026-09/photos/contact-sheet.html — open it in a browser to switch.]

## Meshtastic

- **The MediumFast migration is the big Meshtastic story.** The Denver metro is steadily moving from LongFast to MediumFast for better performance, and Lookout Mountain shifted its presets to nudge people toward MediumFast. Adoption is still uneven — plenty of nodes outside the metro remain on LongFast, and there's healthy discussion about the range tradeoffs — so check what your area is actually running before you switch. Legacy LongFast bridging is being wound down. (Runr, TickleMeTemplar, nwithan8) https://coloradomesh.org/news/mediumfast-changeover
- **A cross-protocol bridge experiment.** nwithan8 ran a live test bridging Meshtastic (LongFast) and MeshCore (Public) in the Denver area to see what actually crosses between the networks. The finding: Meshtastic traffic in range was light enough that there wasn't much worth bridging — useful data for how (and whether) to link the two going forward.
- **Firmware fix worth updating for.** A Meshtastic firmware update this cycle addressed a man-in-the-middle issue — a good reason to make sure your nodes are current. Discussion in [#meshtastic](https://discord.com/channels/1436156966648152271/1456820557176766556).
- **Know your presets.** Alongside MediumFast, there was ongoing talk about LongTurbo and frequency-slot choices, and what each means for range and congestion. If you're unsure what to run, ask before you flash — the channel is happy to help.
- **MQTT, maps, and observers.** A lot of quiet-but-useful plumbing work continued: publishing LongFast/MediumFast traffic to MQTT topics, feeding the Meshtastic map and analyzer, and standing up observers. If you want your area on the map, running an observer is the way in.

## MeshCore

- **We're meshing across state lines.** A working path along I-76 now links the Colorado mesh to Nebraska — an advert from a node near DIA was heard as far as Ogallala. It's a genuine milestone: coverage has grown from a metro network into something that reaches past the state border. (nwithan8)
- **"Scopes" — defining our regions.** With the network sprawling, a new [#scopes](https://discord.com/channels/1436156966648152271/1544705628142833714) channel spun up to plan and standardize MeshCore region definitions. The current proposal leans toward county-based scopes rather than IATA airport codes for better geographic accuracy, and nwithan8 has been coordinating with Nebraska, Utah, and Wyoming so the scheme stays compatible across state lines. Community input is wanted before anything is locked in. (Rin R-4, Zeva, nwithan8)
- **Observers are filling in the map.** New observers came online across the state — including Grand Junction — feeding the MQTT relay and the analyzer so we can actually see how the network is growing. A naming tool was added to help operators label nodes to convention, and folks in under-covered regions are encouraged to stand up an observer and report in. (nwithan8, Zeva)
- **A new MeshCore 500 profile.** Zeva added a MeshCore 500 profile centered on 915 MHz (Philly Mesh has been testing around 915.250) — one more option as we sort out the best local settings. Discussion in [#meshcore](https://discord.com/channels/1436156966648152271/1436175539135058082).
- **The MQTT relay ties it together.** A service on a VPS reads the MQTT broker and relays MeshCore traffic into Discord, so observers' packets show up where the community can see them — part of what makes the analyzer and maps useful.
- **Mind the naming convention.** As nodes multiply, sticking to the [MeshCore naming convention](https://wiki.coloradomesh.org/wiki/MeshCore_Naming_Convention) keeps the map legible for everyone — worth a look if you're renaming or standing up a repeater.
- **New repeaters keep lighting up.** Among them, mrpatzy placed one near Brittany Hill with strong line-of-sight to Denver and the mountains, and more are planned around Grand Junction. Every well-placed node makes the whole mesh more reliable.

## Reticulum

- **Our RRC hub is drawing people from all over.** The Colorado Mesh **RRC (Reticulum Relay Chat)** server has become a genuinely popular gathering spot — folks are joining from around the world to hang out, and a lot of the Reticulum conversation actually happens *there* rather than in Discord. A big shout-out to **KK4FRN (Alex)** for spinning up the hub. Join us: [#reticulum](https://discord.com/channels/1436156966648152271/1455311030832992298).
- **You don't need RF gear to try Reticulum.** This is the easiest on-ramp in the whole hobby: with just an internet connection you can join the RRC hub and get a feel for Reticulum before buying a single radio. **M3SHGHØST** added a Reticulum quick-setup guide to the Mesh Client to make that first step painless. Give it a spin and come say hi.
- **The Mesh Client is a great Reticulum window.** Beyond RRC chat, it now gives you NomadNet browsing — and, new this cycle, *editing* — all in one app. **Runr** and others have been experimenting with a range of Reticulum mobile apps on Android and iOS too, so there are more ways than ever to get on Reticulum from your pocket.
- **Work on the Lookout bridge.** omgitsgela has been configuring a bridge up on Lookout Mountain — a WiFi repeater for remote access, MQTT bridging, and local mirroring of MediumFast and LongFast, with a second radio planned to add LongFast support. It's a meaningful step toward tying the high-site infrastructure together.

## Gear & Firmware

New devices, firmware, and the occasional "don't do that" bulletin from the workbench channels this cycle:

- **Safety bulletin — never remove the antenna on a powered board.** A good reminder from Packman5280: if a LoRa board powers up (or stays powered) with no antenna attached, you can burn out the RF power amp. Power down *before* you swap antennas. Cheap mistake, expensive board.
- **Firmware fix for RNode over BLE.** An update this cycle fixed Bluetooth for RNode on ESP/nRF boards (V3, V4, T-Echo, T114). If you run RNode and BLE's been flaky, grab the update. (dude.eth, [#software](https://discord.com/channels/1436156966648152271/1436717476389060628))
- **Meshtastic firmware fixed a man-in-the-middle issue** — worth updating your nodes for. (See the Meshtastic section above.)
- **Custom repeater firmware from nightcrawler.** A standalone build that bakes in the advert/policy filtering from OpenHop — shared for anyone who wants to try it. ([#meshcore](https://discord.com/channels/1436156966648152271/1436175539135058082))
- **Board note — the RAK 1W is a lot of board for the money.** JohnnyW5KV gives it a +1: integrated input/output filters, solid little board. A popular pick for repeaters right now.
- **OTA gotcha.** A couple of folks learned the hard way that an over-the-air update on a rooftop/solar node can leave you climbing up to re-flash if it doesn't take — worth having a wired fallback plan before you push firmware to anything hard to reach.

## Get the Mesh Client

New here, or still juggling separate apps? The community maintains **Mesh Client** — a free, cross-platform desktop app (Windows, macOS, Linux) that speaks Meshtastic, MeshCore, *and* Reticulum from one window, so you don't need a different tool for each protocol. It's actively developed — a big thanks to Joey (NV0N), its lead developer, and the contributors — and it's the easiest way to manage your nodes and follow the mesh from a real screen. Grab it at github.com/Colorado-Mesh/mesh-client and give it a spin.

## For Sale & Wanted

- No member classifieds came in this cycle. A couple of build resources worth a look, though: Zeva shared a Printables model for a 1-watt low-profile solar mesh car node, and pointed to the RAK3401 1W LoRa booster kit on the RAKwireless store. _Got gear to sell or a part you're hunting for? Drop it in the channel and we'll list it here next month._

## Call to Action

**We need Reticulum full repeaters in high spots — build yours now!** High-elevation nodes are what turn scattered coverage into a real network, and Reticulum full transport nodes on ridges and rooftops are exactly where we're thin. If you've got a good vantage point, tower access, or a solar setup you've been meaning to deploy, this is the single highest-leverage thing you can do for the mesh right now. Ask in the channels — budt W0RMT and others have offered to help with repeater setup, and the wiki has the configuration docs.

**Run an observer in your area — especially outside the metro.** Observers are how a region gets onto the map and the analyzer. If you're in a corner of the state that looks empty on the map, that's often just because nobody's reporting from there yet. The wiki has a [guide to running an observer](https://wiki.coloradomesh.org/wiki/MeshCore_MQTT), and it's a low-effort, high-value way to contribute.

## Community Spotlight

Shout-out to **Iguy**, who stood up a brand-new repeater near Lexington and Union in Colorado Springs — balcony-mounted, solar plus battery, at 6,810 ft. That "just put one up and see what happens" energy is exactly how the mesh grows, one rooftop at a time. And a nod to **Zeva**, whose fingerprints are all over this cycle: region definitions, observer onboarding, config tooling, and a steady stream of technical help in the channels. Welcome to the map, Iguy — and thanks, Zeva.

![beala's hand-built 900 MHz bandpass filter (#projects-and-builds)](photos/filter_web.jpg)

Bonus build spirit of the month: beala hand-fabricated a 900 MHz bandpass filter from a PCB and copper tape — the VNA showed a real filter, just with (beala's words) a hilarious 33 dB of insertion loss. Not shippable yet, but exactly the kind of tinkering that makes this community fun.

More folks who moved the mesh forward this cycle: **JohnnyW5KV**, who finished a solar install and a chimney-mast setup for a Station G3 and has been a fixture troubleshooting repeaters; **EnderW**, who's been building out the northwest corner of the state; and **nightcrawler**, who shared RF sweep results and custom repeater firmware. The mesh grows on exactly this kind of hands-on effort — thank you all.

## Around the Web

- beala's writeup on the FCC and using 500 kHz bandwidth — a genuinely good technical deep-dive: https://beala.substack.com/p/the-fcc-want-me-to-use-more-bandwidth
- JohnnyW5KV's video reviews of mesh gear (the PeakMesh Climber, among others) on YouTube.
- A new coloradomesh.org news page on the 2-byte path changeover is in progress (KFØUFO - Andrew) — https://coloradomesh.org/news/2-byte
- Colorado MeshCore analyzer & tools — network stats, beacon data, contact-pack downloads, and range checks: https://analyzer.meshcore.coloradomesh.org and https://tools.meshcore.coloradomesh.org
- Setting up Reticulum infra? Zeva shared a Docker config for a NomadNet transport node in [#reticulum](https://discord.com/channels/1436156966648152271/1455311030832992298) — a handy starting point.

## Story of the Month: Meshing the Divide

If these two months had a single theme, it was *reach*. Back in August, the network was still largely a Front Range affair — a cluster of nodes trading packets between the foothills and the metro. By mid-September, the map told a different story: messages were routinely finding their way to the far corners of the state and, for the first time, spilling clean across a state line (you'll find the specifics up in the MeshCore section).

What's worth sitting with isn't any one hop — it's how it happened. Nobody flipped a switch. It was the cumulative payoff of dozens of small, unglamorous acts: a node zip-tied to a balcony, an observer quietly reporting from a town nobody had covered yet, a preset nudged on a mountaintop, and an awful lot of people comparing notes about antennas and coax loss at 900 MHz. That's the whole trick to a community mesh — it doesn't scale by decree, it scales by people deciding, one rooftop at a time, that their corner of Colorado belongs on the map. Not bad for a pile of low-power radios and a shared stubbornness about coverage.

## Sources & Further Reading

- Colorado MeshCore analyzer / live map — https://analyzer.meshcore.coloradomesh.org
- Meshtastic live map — https://map.meshtastic.coloradomesh.org
- MeshCore config tools — https://tools.meshcore.coloradomesh.org
- MediumFast changeover — https://coloradomesh.org/news/mediumfast-changeover
- 2-byte path changeover — https://coloradomesh.org/news/2-byte
- Colorado MeshCore Regions (wiki) — https://wiki.coloradomesh.org/wiki/Colorado_MeshCore_Regions
- MeshCore MQTT / running an observer (wiki) — https://wiki.coloradomesh.org/wiki/MeshCore_MQTT
- Weekly Net check-in — https://weekly-net.meshcore.coloradomesh.org
- Donate to keep the network running — https://coloradomesh.org/donate
- Join / getting started — https://coloradomesh.org

## Until Next Month

That's the catch-up. From here we'll land once a month, covering the prior month.
If you lit up a repeater, printed an enclosure, ran a great wardrive, or finally
beat a stubborn SNR — tell us, so it lands in the next issue. Big or small, we
want it.

**Nerd Joke of the Month:** Why did the LoRa packet bring a ladder to the net? It heard the best check-ins come from *high* SNR.

**The Prize:** this month's giveaway is a **RAKwireless WisBlock Meshtastic Starter Kit (US915)** — the RAK19007 Base + RAK4631 Core — bundled with a **RAK12501 GNSS location tracker module**. Everything you need to build a GPS-equipped Meshtastic node from scratch. Starting next month we'll draw a random winner from everyone who reacts to the newsletter in Discord — so react to this issue to be entered!

**73**
