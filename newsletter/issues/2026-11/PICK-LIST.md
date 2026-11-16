# Newsletter Pick List — November 2026

Admins: this is a **curated candidate pool** triaged from the month's Discord
activity + the wiki. Tick what you want, ignore the rest, add anything we missed.
We compose the newsletter from your picks (LIFECYCLE.md, Gate 1).

- [ ] blank = skip · [x] = include · edit the text freely

_Sections are best-effort; if something's mis-filed just note it — we'll re-file._
_Top candidates per section shown; the full pool is in the candidates JSON._


## General News

- [ ] **Vanderbilt University Network Hacked in Cyberattack** — Zeva reported that Vanderbilt University's Wi-Fi networks were reportedly hacked, though confirmation is pending. This incident is part of a string of attacks by a new group called BYOD, which is targeting universities. Zeva noted that there are many vulnerabilities in the current landscape, making it difficult to assess the full scope of the threat.  _(Zeva · #general 2026-11-10)_
- [ ] **Flaresat Renamed to Carroted Maps with Major Update** — The Flaresat app has been renamed to Carroted Maps, maintaining the same functionality and team. The update includes new features like route sharing, alert zones, and enhanced MeshCore integration. The app allows users to share maps without cell signal or accounts by pairing a MeshCore or Meshtastic radio over Bluetooth.  _(Adrelien · #carroted-maps 2026-11-05)_
- [ ] **Zeva Announces Meshtastic 2.0 Release with Backend Changes** — Zeva announced that the next version of Meshtastic will be 2.0 due to a backend change that is not compatible with 1.x, switching from SQLite to gzipped JSON. Additionally, Zeva identified critical security issues that are being addressed after extensive testing using Mythos. The release is expected to happen tonight.  _(Zeva · #software 2026-11-15)_
- [ ] **Zeva Working on Next Prerelease with Desktop App and Encrypted Backups** — Zeva is working on the next prerelease of the software, which includes a desktop app as a separate release artifact. Backups are now optionally encrypted, enhancing data security for users.  _(Zeva · #software 2026-11-02)_
- [ ] **Timing Error and Location Accuracy in RF Propagation** — beala 🆎 shared timing error data and location accuracy assumptions, noting that reflections are likely the biggest source of error in real-world conditions.  _(beala 🆎 · #rf-propagation 2026-11-08)_
- [ ] **RF Issues with Downspout Mounting** — cowoody asked if being on a downspout is bad for RF, indicating concerns about antenna placement and signal propagation.  _(cowoody · #rf-propagation 2026-11-11)_
- [ ] _add one:_ 

## Events & Meetups

- [ ] **Zeva Announces MeshWars Project** — Zeva shared a link to a project related to MeshWars, which uses the MeshMapper app for automatic uploads. The project can be viewed at https://discord.com/channels/1436156966648152271/1557615190462169138. This initiative is part of ongoing efforts to enhance mesh network activities and wardriving capabilities.  _(Zeva · #wardriving 2026-11-13)_
- [ ] **Meshcore Development and Testing Opportunities** — Half Live is developing a turn-based multiplayer game for the mesh network and is seeking testers. The game, called Grid Strike, is designed to run on various devices and is currently in testing phase. Interested individuals are encouraged to participate and report any issues. The project is hosted on GitHub for further details.  _(Half Live · #meshcore 2026-10-30)_
- [ ] **MECP-TAK Integration Confirmed in Mesh-Client** — budt W0RMT confirmed that MECP with location data plots on the ATAK map connected to the mesh-client TAK server, and that messages are removed from the map once resolved in the incidents tab. This integration is a valuable feature for incident management and coordination.  _(budt W0RMT · #mecp 2026-11-03)_
- [ ] **Interest in Expanding Mesh Coverage in Middle Park Area** — duggym122 expressed interest in extending the mesh through the Middle Park area, mentioning a potential setup with a friend in Grand Lake. This indicates community interest in expanding mesh coverage for reliable communication during internet outages.  _(duggym122 · #mesh-planning 2026-11-11)_
- [ ] **Plans to Expand Mesh Coverage Toward Fort Morgan** — sneaky_boi762 expressed interest in expanding mesh coverage toward Fort Morgan along I-76 and offered to install and maintain a node. This initiative highlights the community's efforts to improve connectivity in underserved areas.  _(sneaky_boi762 · #introductions 2026-11-02)_
- [ ] **Plans for Repeater in Fraser Area** — duggym122 mentioned plans to set up a repeater in the Fraser area and expressed interest in connecting with other mesh users in the region. This reflects the community's collaborative approach to expanding network coverage.  _(duggym122 · #mesh-planning 2026-11-11)_
- [ ] **Discussion on Repeater Setup on FlatTop** — KFØUFO - Andrew was asked about a potential repeater setup on FlatTop and suggested discussing the matter further. This highlights ongoing conversations about network expansion and infrastructure improvements.  _(KFØUFO - Andrew · #western-slope 2026-11-03)_
- [ ] **MeshCore Map Showing Network Activity** — Half Live shared a link to the MeshCore map, which displays network activity and is regularly updated. The map is a valuable resource for tracking mesh coverage and node locations across Colorado.  _(Half Live · #general 2026-11-13)_
- [ ] _add one:_ 

## Meshtastic

- [ ] **Meshcore Firmware and Client Development Updates** — cj shared insights about the firmware development process, noting that the firmware bot did not fit into some hardware boards. Additionally, cj mentioned the challenges of iOS lockdown mode and the potential for device tracking through radio differences and device names. These discussions highlight ongoing efforts to improve security and compatibility.  _(cj · #meshcore 2026-11-03)_
- [ ] **Meshcore Security and Privacy Considerations** — beala 🆎 raised concerns about privacy and security, noting that Meshcore messages include cleartext information about cell towers. This transparency can be a vulnerability, especially in the context of law enforcement infiltration. The community is encouraged to consider these risks and implement additional security measures where necessary.  _(beala 🆎 · #meshcore 2026-11-03)_
- [ ] **MECP Integration and Development Progress** — Blake is working on integrating MECP (Mesh Client Protocol) into multiple languages and has implemented test vectors to ensure compatibility. While the project is not yet ready for full integration, the work has provided valuable insights. Blake is seeking feedback and collaboration to refine the implementation further.  _(Blake · #mecp 2026-11-15)_
- [ ] **Long Turbo and MediumFast Settings Discussion** — Kobalt asked if others had started using long turbo on Meshtastic. Roran inquired about visibility of nodes on different speed settings, and beala explained that the app's map is populated based on the same settings as the user. This highlights the importance of consistent settings for mesh visibility and communication.  _(Kobalt, Roran, beala 🆎 · #meshtastic 2026-10-28, #meshtastic 2026-11-02)_
- [ ] **Zeva Shares Progress on Reticulum-Only App** — Zeva mentioned having a branch available for testing that is working mostly, though it is quirky and AI summaries do not function. Zeva is also conducting a security audit of their Reticulum-only app and has identified critical vulnerabilities. The work is ongoing, with plans to improve the mobile UI.  _(Zeva · #mesh-client-help 2026-11-15)_
- [ ] **Beala Develops Firmware Fork with Ranging Feature** — Beala is working on a firmware fork that incorporates lessons learned from the LR2021. A sneak peek at the ranging feature was shared, which allows for estimating the distance between two nodes using time of flight, similar to Apple's Find My feature. This feature does not rely on GPS.  _(beala 🆎 · #software 2026-11-04)_
- [ ] **Discussion on Automated Broadcasts in Mesh-Client** — cj raised concerns about automated broadcasts in the mesh-client, suggesting that they should be reserved for emergency alerts due to airtime considerations. The discussion highlights the community's interest in balancing functionality with resource management.  _(cj · #mesh-client-dev 2026-11-03)_
- [ ] **Rin's Discussion on MECP and Protocol Development** — Rin discussed the challenges of managing MECP, including the need for a dedicated space for enhancements and the importance of neutrality in discussions. Rin is working on protocol development and has been re-examining the base premise of the protocol.  _(Rin (R-⁰) · #mecp 2026-11-15)_
- [ ] **Discussion on MECP Standardization** — Blake expressed disagreement with a decision regarding MECP standardization and proposed standardizing vectors into the MECP repo. The discussion highlights ongoing efforts to improve interoperability and consistency across mesh protocols.  _(Blake · #mecp 2026-11-15)_
- [ ] **Discussion on MeshCore Firmware and Client Software** — WilsonInVR noted that while MeshCore is superior in communication compared to Meshtastic, the firmware and client software are lacking. This feedback underscores the need for continued development and improvement in the MeshCore ecosystem.  _(WilsonInVR · #general 2026-11-13)_
- [ ] **GPS and Mesh Client Issues** — N4CNR-Rich reported issues with the mesh client not recognizing GPS coordinates and mentioned using the mesh for sending files and testing. This highlights ongoing challenges with GPS integration and the use of mesh for data transfer.  _(N4CNR-Rich · #mesh-client-dev 2026-10-30, #mesh-client-dev 2026-11-14)_
- [ ] **nwithan8's Mention of MeshCore Filtering Features** — nwithan8 shared that Dutch MeshCore has implemented advanced filtering features, including per-origin advert windows, path-prefix blocking, and configurable message age limits. These features enhance network security and management.  _(nwithan8 · #meshcore 2026-11-09)_
- [ ] _add one:_ 

## MeshCore

- [ ] **CJ Advises Against Using MeshCore for Sensitive Data** — CJ warned that MeshCore is not suitable for data that absolutely needs encryption, as all group text packets and repeats can be seen even if the channel or message content is not known. Reticulum is recommended for privacy-sensitive LoRa messaging, while other platforms like Graphene OS or iOS lockdown mode are suggested for better security.  _(cj · #meshcore 2026-11-03)_
- [ ] **WearMesh App on WearOS Smartwatches** — budt W0RMT shared an experience using the WearMesh app on a Pixel Watch 5 with a Wismesh Tag, highlighting the potential for mesh communication from smartwatches. They also mentioned a check-in mode to conserve battery.  _(budt W0RMT · #meshcore 2026-11-06)_
- [ ] **MeshCore Beacon Live Map Issues Reported** — JohnnyW5KV reported a drastic change in experience with the Beacon live map, noting that adverts and group messages are no longer shown instantly, raising questions about the coding differences between the two systems.  _(JohnnyW5KV · #meshcore 2026-11-06)_
- [ ] **MeshCore Hoodie and Off-Grid Messaging Network** — budt W0RMT shared a photo of someone wearing a MeshCore hoodie and linked to an article about an off-grid messaging network in Western New York, emphasizing the community's impact and visibility.  _(budt W0RMT · #meshcore 2026-11-14)_
- [ ] **Security Concerns with MeshCore Group Chat Metadata** — fractalhuman shared concerns about the routing metadata in MeshCore for private group chats being mostly unencrypted, which could allow rough triangulation of users' physical movements.  _(fractalhuman · #meshcore 2026-11-03)_
- [ ] _add one:_ 

## Reticulum

- [ ] **Reticulum and Ratspeak Crypto Discussion** — cj clarified that Reticulum is a Rust-based implementation used in the mesh-client project and does not have any dependencies on Ratspeak crypto. There is no substantial evidence suggesting Ratspeak is a scam or rug pull, and the community is encouraged to continue using Reticulum for its reliability and performance.  _(cj · #reticulum 2026-11-06)_
- [ ] **Reticulum Forum Thread Resolved** — A discussion regarding LXMF-121 from static-only rejecting client resource uploads has been resolved, with the issue smoothing out. The thread can be viewed here: https://rns.recipes/forum/general/lxmf-121-from-static-only-rejects-client-resource-uploads#post-3908  _(d1 · #reticulum 2026-11-08)_
- [ ] **James W5PL Makes truSDX Driver for Reticulum** — James - W5PL shared a GitHub link to a driver for the truSDX radio, making it usable on Reticulum. This development could enhance the integration of the truSDX radio within the Reticulum network.  _(James - W5PL · #reticulum 2026-11-08)_
- [ ] **Documentation on Damaged Packets in MeshCore** — beala 🆎 shared a link to documentation detailing how damaged packets are handled in MeshCore, providing technical insights into the network's robustness and error correction mechanisms.  _(beala 🆎 · #software 2026-11-07)_
- [ ] _add one:_ 

## Gear & Firmware

- [ ] **Battery Chemistry Discussion for Solar Nodes** — LiteSwitch asked about using IMR 14500 cells for solar nodes, comparing them to LiPo and LiFePo. They are considering using spare solar path lights with these cells and inquired about charging issues below freezing temperatures. Woof suggested a bimetal thermostat near 0C for solar panel lines, while Your Mom expressed interest in building a comprehensive mesh power supply board with various protections and sensors.  _(LiteSwitch, Woof, Your Mom · #hardware 2026-11-12)_
- [ ] **Beala Releases MeshOS APK on GitHub** — Beala uploaded the latest version of the MeshOS APK to GitHub, with metadata indicating it was uploaded two weeks ago. The release is available at https://github.com/andymux/meshos-releases/releases#release-v1.0.31, and is part of ongoing firmware development efforts.  _(beala 🆎 · #meshcore 2026-11-07)_
- [ ] **Battery Management Considerations for Lithium Packs** — JohnnyW5KV discussed the challenges of finding a BMS for 1S lithium packs that can shut off charging below 32F. He noted that higher voltage packs (3S or 4S) typically have built-in temperature protection, and recommended using Nitecore low-temp batteries for convenience and safety.  _(JohnnyW5KV · #hardware 2026-11-12)_
- [ ] **Bundle Size and PR Management in Meshcore** — cj mentioned that the bundle size check is not being run for every PR, which could lead to issues. They suggested either running the check for every PR or increasing the bundle size limit. They also noted that some E2E tests are failing on macOS due to intercepted clicks.  _(cj · #mesh-client-dev 2026-10-28)_
- [ ] **Bundle Size and E2E Test Issues in Meshcore** — cj noted that the bundle size check is not being run for every PR, leading to potential issues. They mentioned that increasing the bundle size limit or running checks on every PR could help. Additionally, some E2E tests are failing on macOS due to intercepted clicks.  _(cj · #mesh-client-dev 2026-10-28)_
- [ ] **Hardware Recommendations and Battery Tips** — Woof recommended the Samsung 35E 18650 battery for its reliability and performance, providing a link to a supplier. This advice is particularly useful for those building or maintaining mesh nodes, as reliable power sources are essential for consistent operation.  _(Woof · #hardware 2026-11-11)_
- [ ] **Li-ion Battery Performance in Cold Temperatures** — Users have reported that Li-ion batteries lose capacity rapidly in low temperatures and cannot be charged if they fall below 32°F. This is primarily a safety concern and may be exacerbated by the presence of protection units in the batteries.  _(cj · #hardware 2026-11-12)_
- [ ] **Zeva Recommends PiMesh V2 for MeshCore Use** — Zeva mentioned having a PiMesh V2 with the E22P, which works directly on a Raspberry Pi and is considered great for MeshCore applications. This device is a popular choice for mesh network enthusiasts due to its reliability and performance.  _(Zeva · #western-slope 2026-11-03)_
- [ ] **Antenna and DX Setup Discussion** — beala 🆎 shared details about a DX setup with a Mosley Pro-67 antenna mounted on a tower, covering multiple bands. This showcases the diversity of antenna setups and the importance of high-quality equipment for long-range communication.  _(beala 🆎 · #ham-radio 2026-10-30)_
- [ ] **Broken Links and Website Issues** — jk reported that links to brandmeister repeater pages and the W0DMR website were not working, returning 403 Forbidden and NXDOMAIN errors. This indicates potential issues with website maintenance and accessibility for the community.  _(jk · #ham-radio 2026-11-08)_
- [ ] _add one:_ 

## Call to Action

- [ ] **Call to Action for Mesh Map Services** — Sid mentioned the difference between two mesh map services and noted that they are both useful. This highlights the importance of using multiple tools for comprehensive mesh coverage and encourages users to explore and utilize different services.  _(Sid · #wardriving 2026-11-12)_
- [ ] **Need for App Store Signing Credentials** — cj is working on iOS and Android builds for mesh-client and is asking if the community has an LLC for app store signing or if someone is willing to use their personal Apple Developer account. They also mentioned that the process is complicated.  _(cj · #mesh-client-mobile-apps 2026-11-03)_
- [ ] **Add Your Callsign for Potential KG Prefixes** — nwithan8 reminded members to add their callsigns when they receive them, as they may be among the first to get the `KG` prefixes. This is an important step for those interested in amateur radio and the Colorado Mesh community.  _(nwithan8 · #ham-radio 2026-11-10)_
- [ ] **Zeva Invites Contributions to Mesh-Client TUI** — Zeva is working on a TUI (Text User Interface) for the mesh-client that works on all platforms with extra features. Zeva encourages community members to contribute and make cool things, while ignoring any drama that may arise.  _(Zeva · #reticulum 2026-11-09)_
- [ ] **Help Needed for Meshcore App Development** — Budt W0RMT is working on MECP stuff for the TAK server part of mesh-client and is asking if others want to hold off on PRs until other issues are resolved to reduce noise. They are also seeking help with the project.  _(budt W0RMT · #mesh-client-dev 2026-10-28)_
- [ ] **Membership Dues and Club Announcements** — WX9S mentioned being good on dues until April or May of next year, noting the timing of the announcement following a QST article on club membership. This could signal potential changes or updates in club policies.  _(WX9S · #ham-radio 2026-10-30)_
- [ ] _add one:_ 

## Community Spotlight

- [ ] **JohnnyW5KV Shares MeshWars Video** — JohnnyW5KV shared a video link related to MeshWars, which uses the MeshMapper app for automatic uploads. The video can be viewed at https://youtu.be/cXhbZNiNIH4, and is a valuable resource for those interested in wardriving and mesh network activities.  _(JohnnyW5KV · #general 2026-11-15)_
- [ ] **Community Member Recognized for Meshcore Setup** — shadowblackRS shared a positive experience with setting up Meshcore, expressing gratitude for the initial support received. This highlights the importance of community assistance and the satisfaction of successfully integrating mesh technology into personal projects.  _(shadowblackRS · #general 2026-11-04)_
- [ ] **cj's Contributions to Meshcore Development** — cj has been actively involved in mesh-client development, working on layout tests, bundle size checks, and E2E testing. They have also been addressing issues with the app store signing process and have shared insights on the development workflow.  _(cj · #mesh-client-mobile-apps 2026-11-03)_
- [ ] **Newcomer Interested in Setting Up a Repeater** — stinger, a new member, mentioned starting to explore the project and having a small piece of land where they plan to set up a repeater. This shows the community's welcoming nature and the potential for new contributions to mesh infrastructure.  _(stinger · #louisville-lafayette-superior 2026-11-05)_
- [ ] **Half Live Shares MeshCore Map Link** — Half Live frequently shares links to the MeshCore map, which is a key resource for tracking network activity and node locations. This consistent contribution highlights their role as an active community member and information provider.  _(Half Live · #general 2026-11-13)_
- [ ] **Budt W0RMT's Contributions to Meshcore** — Budt W0RMT has been actively contributing to mesh-client development, working on MECP stuff for the TAK server and helping with various aspects of the project. They have also shared insights on bundle size checks and E2E testing.  _(budt W0RMT · #mesh-client-dev 2026-10-28)_
- [ ] **JohnnyW5KV Celebrated for 11 Years as a Ham Radio Operator** — JohnnyW5KV celebrated making their first contacts on 60 meters, marking 11 years as a ham radio operator. They also shared a YouTube video of a doublet antenna they built for 80–10 meters.  _(JohnnyW5KV · #ham-radio 2026-11-01)_
- [ ] _add one:_ 

## Around the Web

- [ ] **Meshcore Tools and Resources** — nwithan8 shared a link to a Meshcore tool, providing access to additional resources for the community. This tool is likely to be useful for developers and enthusiasts looking to enhance their mesh network capabilities.  _(nwithan8 · #general 2026-11-14)_
- [ ] **Global Mesh Mapper Website** — Zeva shared a link to the Global Mesh Mapper website, which is used for mapping mesh networks. This tool is valuable for visualizing and understanding network coverage and connectivity.  _(Zeva · #wardriving 2026-11-01)_
- [ ] **MeshCore Website Shared** — Half Live shared the MeshCore website (https://meshcore.io/) in the Aurora channel, indicating community interest in meshcore-related resources and tools.  _(Half Live · #aurora 2026-11-09)_
- [ ] **FluxCore: A New MeshCore Fork Announced** — Beala 🆎 announced a new MeshCore fork called FluxCore on their Substack blog, providing an update on the development and features of the fork.  _(beala 🆎 · #software 2026-11-06)_
- [ ] **Colorado MeshCore Radio Settings Wiki Page** — Half Live shared a link to the Colorado MeshCore Radio Settings wiki page, providing detailed information on configuration and setup.  _(Half Live · #meshcore 2026-10-29)_
- [ ] _add one:_ 

---
## Recurring / fixed (auto-included unless you say otherwise)
- [x] **Get the Mesh Client** reminder (Joey NV0N's cross-protocol app)
- [x] **Weekly Net reminder** (Thursdays, post to Public)
- [x] **Photo of the Month**
- [x] **The Prize**
- [x] **Nerd Joke of the Month**, **Cold open**, **Sources** (auto-built)

## Anything big we missed? Add it here:
- [ ] 
---
## 🔒 Sourcing note
Candidates are from PUBLIC channels only. Internal channels (#mesh-ops, #scopes,
#advocacy) are read for context but never quoted/published → candidates-background.json.
(#mesh-planning and #emcomm-network-ops are public and quotable.)

## 🔁 Carry-forward from October (still live?)
- [ ] **MECP** — momentum continues; TAK-bridge integration maturing (see net-new)
- [ ] **CoreScope → Beacon** — follow-up: some report the Beacon live map no longer
      shows adverts/group messages instantly (JohnnyW5KV) — worth a status note
- [ ] **Mesh Client** — V6 shipped last issue; this month is incremental (see net-new)

## 🔂 Recurring anchors (default-include)
- [x] Weekly Net reminder (Thursdays)
- [x] Get the Mesh Client (Joey NV0N)
- [x] "No RF needed — try Reticulum on the RRC hub"
- [ ] Run an observer in your area
- [ ] MeshCore naming convention / repeater name tool

## 🧵 Follow-ups on October threads
- [ ] **Beacon live-map behavior change** — adverts/group msgs not instant now; clock-drift
      questions on observers (JohnnyW5KV, Your Mom, Sid). Status/explainer?
- [ ] **meshcore-tak-bridge / MECP** — MECP 1.2.1 released; location plots on ATAK, clears
      when resolved (budt W0RMT). Good progress update.
- [ ] **RMNP repeater letter** (JohnnyW5KV, Oct) — any reply from the park?

## 🆕 Net-new November themes (PUBLIC-sourced)
- [ ] **Meshtastic "2.0" / Mesh Client backend change** — Zeva: next version is 2.0 due to
      a breaking backend change (SQLite → gzipped JSON); desktop app as a separate artifact;
      optional encrypted backups. [#software] — likely a lead/feature.
- [ ] **MECP matures** — MECP 1.2.1; TAK-bridge location plotting; Rin working on governance/
      neutrality + a dedicated space for enhancements. [#mecp]
- [ ] **Security & privacy reality check** — CJ/fractalhuman: MeshCore group-text packets &
      routing metadata are largely unencrypted (visible repeats, rough triangulation). An
      honest "know what's private" explainer. [#meshcore]
- [ ] **FluxCore — a new MeshCore fork** announced by beala (Substack). [#software]
- [ ] **WearMesh on a smartwatch** — budt W0RMT ran MeshCore from a Pixel Watch + Wismesh Tag. [#meshcore]
- [ ] **Flaresat → "Carroted Maps"** rename + update (route sharing, alert zones). [#carroted-maps]
- [ ] **Coverage push: Fort Morgan (I-76), Fraser, Middle Park/Grand Lake, FlatTop** — several
      new operators volunteering high/remote sites. [#mesh-planning, #western-slope, #introductions]
- [ ] **New Fort Collins weekly meetup** — Dervish, Thursdays 6 p.m., alt-comms/tech. [#foco-greeley]
- [ ] **Hardware corner** — beala's dual-band (915 MHz + 2.4 GHz) 1W custom WisBlock; LR2021
      on-chip FFT opcode; PiMesh V2; cold-weather BMS tips; PETG for enclosures. [#projects-and-builds, #hardware]
- [ ] **KG callsign prefixes** — add your callsign; Coloradans may be among first to get `KG`. [#ham-radio]
- [ ] **Grid Strike** — Half Live's turn-based multiplayer game for the mesh, seeking testers. [#meshcore]

## 💡 Story-of-the-Month candidates
- [ ] The privacy reality of mesh ("it's resilient, not secret") — timely given the security thread
- [ ] Coverage reaching the mountains — Fraser, Middle Park, Fort Morgan, the high sites
- [ ] NYC Mesh as inspiration (nwithan8) — what a mature community mesh looks like

## 📝 Context (not for print)
- Prize draw has been DROPPED from the newsletter going forward (per Alex, Nov 2026).
