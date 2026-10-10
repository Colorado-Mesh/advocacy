# Newsletter Pick List — October 2026

Admins: this is a **curated candidate pool** triaged from the month's Discord
activity + the wiki. Tick what you want, ignore the rest, add anything we missed.
We compose the newsletter from your picks (LIFECYCLE.md, Gate 1).

- [ ] blank = skip · [x] = include · edit the text freely

_Sections are best-effort; if something's mis-filed just note it — we'll re-file._
_Top candidates per section shown; the full pool is in the candidates JSON._


## General News

- [ ] **MeshCore Node Configuration Issue Identified** — User beala reported a configuration issue with the node cc <@785699420201025536>, which is advertising every 2 minutes. The issue was flagged on the MeshCore map at https://map.meshcore.coloradomesh.org/?iata=FNL&regions=northeast-colorado%2Csoutheast-colorado%2Cfront-range%2Ccentral-colorado%2Cwestern-slopes%2Cnorthwest-colorado%2Csouthwest-colorado&tab=Nodes&node=023692bb-014b-413b-a7e0-56eff069ac69.  _(beala · #meshcore 2026-10-08)_
- [ ] **MeshCore Reach Check Tool Released** — The Colorado Mesh community has released a new tool for checking mesh reach, available at https://github.com/Colorado-Mesh/meshcore-reach-check. This tool is based on the upstream project by yellowcooln at https://github.com/yellowcooln/meshcore-health-check.  _(nwithan8 · #meshcore 2026-10-08)_
- [ ] **Admin Team Leadership Updates** — Several members of the admin team have stepped down to focus on other priorities, including <@170852206701051904>, <@150458776917377024>, <@1058449491402956821>, <@144172620563087360>, and <@351881179827273739>. The community is also welcoming <@196018858455334912> to the admin team.  _(<@170852206701051904>, <@150458776917377024>, <@1058449491402956821> · #announcements 2026-10-07)_
- [ ] **Colorado Mesh Monthly Newsletter Published** — The first edition of the Colorado Mesh Monthly newsletter has been released, featuring news and updates from the community. It is available at https://blog.coloradomesh.org/2026/09/21/colorado-mesh-monthly-aug-sept-2026.html.  _(<@219923482694254592> · #announcements 2026-09-22)_
- [ ] **Weekly Net Activity and Participation Challenges** — nwithan8 noted that there is substantial conversation happening on the Public channel during the weekly net, though participation from outside the region, such as Tennessee, is limited. They are working on addressing this issue.  _(nwithan8 · #weekly-net 2026-10-07)_
- [ ] **Colorado Emergency Reporting Network Seeks Volunteers** — The Colorado Emergency Reporting Network (CERN) is actively seeking volunteers to support emergency communication efforts. For more information, visit their website at https://co-cern.org/.  _(nwithan8 · #ham-radio 2026-10-08)_
- [ ] **KFØUFO - Andrew Notes Wiki Sufficiency for Device Information** — KFØUFO - Andrew mentioned that a separate page for listing devices on the Wiki is unnecessary, as the existing Wiki is already comprehensive. This indicates the community's confidence in the current documentation.  _(KFØUFO - Andrew · #wiki 2026-09-24)_
- [ ] _add one:_ 

## Events & Meetups

- [ ] **Parker Radio Association Chili Cookout** — JohnnyW5KV announced the Parker Radio Association Chili Cookout for members and their families this weekend. The event takes place on 80 acres of land in Franktown. Club membership is $25 per year, and the mesh group has contributed to 5-6 new attendees at PRA meetings.  _(JohnnyW5KV · #ham-radio 2026-10-02)_
- [ ] **Colorado Mesh Promo Video in Development** — A promo video is being developed to showcase the capabilities of the Colorado Mesh network, including support for multiple protocols, online maps, MQTT, and emergency communications. This video is intended to attract new users and contributors.  _(<@1019232922580045876>, JohnnyW5KV · #emcomm-network-ops 2026-09-24)_
- [ ] **Repeater Programming in Camper for VHF/UHF** — JohnnyW5KV has decided to program repeaters into his VHF/UHF radio in his camper for use in remote areas of Colorado where cell signal is unreliable. He mentioned tuning into the 'Colorado Connection' net and encountering various transmissions.  _(JohnnyW5KV · #ham-radio 2026-10-08)_
- [ ] **New MeshCore Node Setup in Hesperus** — UtahSTI, a new member in Hesperus, shared details about setting up two nodes: a solar repeater (DRO-HESP-TRPPRS-RE-3A9C) and an MQTT observer (DRO-HESP-TRPPRS-OB-7A0B). The repeater is moving to the roof with a 5.8 dBi antenna.  _(UtahSTI · #western-slope 2026-10-08)_
- [ ] **Observer Participation and Wardriving** — nwithan8 thanked an observer for reporting data and mentioned ongoing efforts to onboard DRO on MeshMapper for wardriving in new locations. This helps in mapping mesh coverage and bridging mesh islands.  _(nwithan8 · #western-slope 2026-10-08)_
- [ ] **Zeva Heading to Grand Junction for Mesh Mapping** — Zeva plans to head to Grand Junction this weekend to conduct mesh mapping, aiming to gather extensive coverage data. This is part of ongoing efforts to improve network coverage and data collection.  _(Zeva · #wardriving 2026-09-29)_
- [ ] **Zeva Planning to Visit Western Slope for Mesh Networking** — Zeva is excited to visit the western slope and plans to meet new contacts during their trip. They mentioned staying near Moab and are looking forward to expanding the mesh network in the area.  _(Zeva · #western-slope 2026-10-01)_
- [ ] **Weekly Net Check-In Rules** — nwithan8 clarified that any message on Public between 12 a.m. and 11:59 p.m. on Thursdays counts as a check-in for the weekly net, even if the event is only an hour long on Discord.  _(nwithan8 · #weekly-net 2026-10-09)_
- [ ] _add one:_ 

## Meshtastic

- [ ] **Mesh Emergency Communications Protocol (MECP) Support Added** — Support for the Mesh Emergency Communications Protocol (MECP) has been added to the mesh-client. This integration allows for emergency communications and is part of a broader effort to support various protocols. More details and test builds are available at https://mecp.radio/ and https://github.com/Colorado-Mesh/mesh-client/actions/runs/35866220321.  _(<@1019232922580045876> · #mesh-client 2026-09-23)_
- [ ] **MeshMapper Questions Raised About Wardriving Practices** — Brian C Stradale asked about the practices involved in using MeshMapper, specifically whether wardriving is done from cars or on foot, and the distinction between DEAD and DISC statuses on the map. These questions highlight the community's engagement with mapping and network coverage.  _(brian_c_stradale · #wardriving 2026-10-06)_
- [ ] **Meshtastic Traffic Monitoring Updated** — nwithan8 reported that the Meshtastic traffic monitoring system is now collecting and reporting actual message traffic. It captures LongFast and MediumFast traffic from the official Meshtastic MQTT broker on the topic `msh/US/CO`, though LongTurbo is still pending default status.  _(nwithan8 · #meshtastic 2026-09-23)_
- [ ] **Solar Input and Mount Design** — ZRIN (R-4) shared updates on the solar input design for the magnetic car mount, noting that the hole for solar input will be up to the user to seal if necessary. A 25.4mm SMA bulkhead flange adapter was created, though N-Type adapters are recommended to be purchased separately.  _(ZRIN (R-4) · #hardware 2026-09-30)_
- [ ] **Custom Firmware Build for MeshCore** — beala shared a custom build of MeshCore that disables both the LED and buzzer, available at https://github.com/beala/MeshCore/releases/tag/t1000e-v1.17.1. This build is useful for users looking to reduce power consumption or simplify hardware.  _(beala · #hardware 2026-09-23)_
- [ ] **User Suggests UX Improvement for Nomad App** — Runr proposed adding a 'favorite' star to the Nomad app interface to improve user experience, specifically for quickly favoriting pages without scrolling through long lists. This suggestion highlights the community's interest in refining tools for better usability.  _(Runr · #mesh-client 2026-10-01)_
- [ ] **Mesh Client Update Generates Positive Feedback** — User FuzzyKaos shared their enthusiasm for the new Mesh Client, highlighting the significant improvements and overall positive experience with the update. This feedback reflects the community's appreciation for ongoing development and enhancements to the platform.  _(FuzzyKaos · #general 2026-10-03)_
- [ ] **nwithan8 Discusses Network Latency and Device Performance** — nwithan8 calculated that 10 nines (99.99999999%) of uptime equates to 315 ms of downtime per year, highlighting the importance of network reliability. They also noted that the new firmware may significantly impact device range, with results still being evaluated.  _(nwithan8 · #colorado-springs 2026-09-16)_
- [ ] **Lookout Mountain Bridge Progress** — omgitsgela reported that the Lookout Mountain bridge is up but only partially functional. A LongFast node has been installed, and there is a WiFi bridge to facilitate connectivity between LongFast and MediumFast, with plans to echo to MQTT for full integration.  _(omgitsgela · #meshtastic 2026-10-02)_
- [ ] **Meshtastic Relay and MQTT Gateway Details Shared** — nwithan8 explained that the Meshtastic relay reads from the public MQTT broker. Messages reach the broker via either a physical LoRa device in Commerce City or through the Client Proxy feature on the mobile app, which uses the phone's internet connection.  _(nwithan8 · #meshtastic 2026-09-25)_
- [ ] **New Protocol Development for Mesh-Client** — The community is working on adding support for a new protocol from the RFOXiA BLE module, which is a long-range Bluetooth LE system that also supports mesh networking. The manufacturer is sending hardware to enable this new protocol in the mesh-client.  _(<@1019232922580045876>, <@&1436158252437209209>, <@&1470998047642222642> · #mesh-client 2026-10-05)_
- [ ] **MediumFast Traffic Integration with MQTT** — nwithan8 mentioned that any MediumFast traffic reaching a Potato feeder node would also be fed to MQTT, provided the message is tagged for publishing. They also noted that LongTurbo messages should appear on the map as soon as they reach the broker.  _(nwithan8 · #meshtastic 2026-09-23)_
- [ ] _add one:_ 

## MeshCore

- [ ] **MeshCore Software and Map Improvements Discussed** — nwithan8 mentioned plans to deprecate the MeshCore Analyzer and is considering improvements to the map, including a 'Save my favorites' feature and toggling node visibility in live mode. These changes aim to enhance user experience and data visualization.  _(nwithan8 · #meshcore 2026-09-20)_
- [ ] **MeshCore BBS Setup and Updates** — cj announced that the MeshCore BBS is set up and users can message the coloradomesh.org-bbs user for updates. The #bbs channel is recommended for newsletter and post updates. The BBS is hosted on Reticulum and includes a CLI wizard for setup.  _(cj · #meshcore 2026-09-23)_
- [ ] **Chicagoland Naming Convention Trial** — The community is trialing the Chicagoland Naming Convention for MeshCore. This includes a personalization block instead of the trailing hash. The community has closely followed the conventions and is adapting them to fit their needs.  _(<@1019232922580045876> · #meshcore 2026-10-05)_
- [ ] **CoreScope Replacement with Beacon** — The CoreScope instance is being replaced with Beacon due to performance issues. Beacon is a more efficient and intentionally designed application. The transition is expected to improve the overall performance of the meshcore system.  _(<@1019232922580045876> · #meshcore 2026-10-07)_
- [ ] _add one:_ 

## Reticulum

- [ ] **Reticulum Audits Completed with No Violations Found** — Rin (R-⁰) confirmed that both Reticulum audits were completed with no violations found. The audits confirmed that RNS code is not vendored in mesh-client, and the sidecar uses independent Rust implementations, ensuring compliance with licensing conditions.  _(Rin (R-⁰) · #reticulum 2026-10-09)_
- [ ] **Reticulum BBS and Mobile Posting Demonstrated** — Cj and Budt W0RMT showcased the Reticulum BBS, with Budt W0RMT posting from a mobile device using the Columba app through a home transport node. This highlights the community's use of Reticulum for communication and collaboration.  _(cj, budt W0RMT · #reticulum 2026-09-23)_
- [ ] **Reticulum Client and RSNomad Review** — Rin (R-4) shared that they asked opencode to review a large ranting document and evaluate the mesh client and rsNomad for violations. The results will be shared once the PR is up in the mesh client channel.  _(Rin (R-4) · #reticulum 2026-10-09)_
- [ ] **Reticulum Server and User Authentication** — There is a discussion about allowing users to create a userid and password for the Reticulum server, which would be easier for retui than for the mesh client due to the presence of a UI, sidecar, and DB.  _(nwithan8 · #reticulum 2026-10-01)_
- [ ] **Reticulum and RRC Server Updates** — nwithan8 discussed Reticulum and RRC server interactions, noting that they were RRC-ing with nodes to explore Reticulum capabilities. This highlights ongoing experimentation with Reticulum integration.  _(nwithan8 · #general 2026-10-08)_
- [ ] **Zeva Discusses Python Support for Reticulum Client** — Zeva mentioned that their Rust-only client is looking into adding Python support, inspired by the reticast project. This indicates ongoing efforts to expand the client's capabilities and compatibility.  _(Zeva · #reticulum 2026-09-28)_
- [ ] **Zeva Explores Webhook Integration for Reticulum** — Zeva is considering integrating webhook support to send posts from Reticulum into the Discord channel. This could enhance communication and automation between the mesh network and Discord.  _(Zeva · #reticulum 2026-09-25)_
- [ ] _add one:_ 

## Gear & Firmware

- [ ] **Affordable Kelvin Sense Battery Holder** — beala shared a $8 Kelvin sense battery holder for battery testing setups, featuring spring-loaded contacts and 3D-printed components. The product is available on AliExpress at https://www.aliexpress.us/item/3256811870803867.html.  _(beala · #hardware 2026-09-21)_
- [ ] **Oscillator Drift Measurement Blog Post** — beala has written a blog post about measuring oscillator drift in various transmitters, including a discussion on the performance of TCXOs. The post is available at https://beala.substack.com/p/i-bought-a-very-precise-clock-so.  _(beala · #hardware 2026-09-23)_
- [ ] **M9 Device Promises Accessibility for Non-Geeks** — Budt W0RMT praised the M9 device for its potential to be a good option for non-technical users, such as those interested in skiing, running, or hiking. This highlights the community's interest in making mesh technology more accessible to a broader audience.  _(budt W0RMT · #hardware 2026-09-16)_
- [ ] **RFOXiA BLE Module Firmware and Hardware** — The RFOXiA BLE module, which is a long-range Bluetooth LE system with mesh capabilities, has been shared with the community. The firmware is open-source, and the manufacturer is sending hardware to enable support for this module in the mesh-client.  _(<@1019232922580045876> · #mesh-client 2026-10-05)_
- [ ] **Antenna Replacement and Wardriving** — Zeva answered questions about wardriving, confirming that it can be done in a car with either internal or external antennas. They use a solar node magnetically attached to their car and mentioned that speed does not affect the app's performance.  _(Zeva · #wardriving 2026-10-06)_
- [ ] **User Shares Experience with Meshtastic Device** — Runr mentioned purchasing the Meshtastic version of the device, which they believe is unaffected by the MeshCore units being held back. This indicates ongoing interest in using Meshtastic devices for temporary, outdoor purposes.  _(Runr · #hardware 2026-09-16)_
- [ ] **RNode Firmware for RAK 4631** — budt W0RMT shared a link to RNode firmware for the RAK 4631, hosted on GitHub at https://github.com/markqvist/RNode_Firmware. This firmware allows Reticulum functionality on RAK 4631 devices.  _(budt W0RMT · #general 2026-09-22)_
- [ ] **Runr Addresses SD Card Issues in Hardware Orders** — Runr mentioned that an SD card issue was found in a batch of hardware, but the order shipped today. They noted that the SD card is replaceable, indicating that the issue is manageable and not a critical failure.  _(Runr · #hardware 2026-09-16)_
- [ ] **Battery Testing and Setup** — rocode mentioned experiments with an external antenna and waiting for rak 1-watt boards and a solar enclosure for a carpeater. They also noted the need to verify firmware to avoid causing issues for the region.  _(rocode · #general 2026-09-18)_
- [ ] **nwithan8 Shares MeshCore Map and Node Details** — nwithan8 provided links to the MeshCore map and node details, including instructions on how to search for nodes and view recent packets. This information is crucial for network monitoring and troubleshooting.  _(nwithan8 · #software 2026-10-08)_
- [ ] _add one:_ 

## Call to Action

- [ ] **Website Maintenance Scheduled** — KFØUFO - Andrew informed the community that the website and some services may be rebooted intermittently overnight for maintenance. Apologies for any service interruptions, which are expected to be brief.  _(KFØUFO - Andrew · #general 2026-10-09)_
- [ ] **Request for Observer Hosting in Western Slope** — nwithan8 is asking if anyone in Grand Junction or the Western Slope can host a MeshCore observer. One of the firmwares allows a device to function as a repeater/observer, provided it has internet access.  _(nwithan8 · #western-slope 2026-09-22)_
- [ ] **Request for Summary Document on MECP Messages** — nwithan8 is requesting a summary document of messages related to MECP to help digest the information and organize it into buckets or channels for better management.  _(nwithan8 · #mecp 2026-10-08)_
- [ ] _add one:_ 

## Community Spotlight

- [ ] **Zeva's Contributions to the Community** — Zeva has been actively contributing to the community, including sharing projects and providing support. Their work on the solar mesh car node and other builds has been valuable to the mesh network.  _(Zeva · #projects-and-builds 2026-09-15)_
- [ ] **Zeva Shares Repeater Information** — Zeva shared a link to a repeater on MeshMapper, located at 4D59, 38.33593, -104.75653. This information is useful for locating and connecting to repeaters in the area.  _(Zeva · #pueblo 2026-09-17)_
- [ ] **nwithan8 Adds /AG to Call for Next Few Days** — nwithan8 has added the /AG designation to their call for the next few days, indicating a specific mode or activity.  _(nwithan8 · #ham-radio 2026-10-05)_
- [ ] _add one:_ 

## Around the Web

- [ ] **Sensor Node Blog Post Shared for Community Interest** — Beala shared a blog post about a new sensor node type, which could be of interest to the community for potential projects or applications. This demonstrates the community's interest in exploring new hardware and technology.  _(beala · #projects-and-builds 2026-09-19)_
- [ ] **New Mesh Client Video Released** — A new mesh client video has been released, showcasing features and updates. The video can be viewed at https://discord.com/channels/1436156966648152271/1485240999406993489/1556411174570954757.  _(nwithan8 · #software 2026-10-04)_
- [ ] **Mesh-Client v6 Release** — The latest version of the mesh-client, v6, has been released. Users can download the release for their platform from https://github.com/Colorado-Mesh/mesh-client/releases/tag/v6.0.0.  _(<@1019232922580045876> · #mesh-client 2026-09-30)_
- [ ] **MeshCore Map and MQTT Nodes** — The community can view known Meshtastic nodes via MQTT at https://map.meshtastic.coloradomesh.org/map and known MeshCore nodes at https://map.meshcore.coloradomesh.org/?tab=Map.  _(<@1019232922580045876> · #aurora 2026-09-29)_
- [ ] **MeshCore Map and Beacon Live View** — JohnnyW5KV preferred the live map of beacon for its clarity, as it removes nodes not in the equation. Rachel provided a link to the MeshCore Repeater Setup guide on the wiki for optimal settings.  _(JohnnyW5KV, Rachel · #meshcore 2026-09-21)_
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
## 🔒 Sourcing note (read first)
Candidates here come **only from public channels**. Discussion in internal/
planning channels (#mesh-ops, #scopes, #mesh-planning, #advocacy) was read for
context but is NOT quoted or published — see candidates-background.json for that
material (do-not-publish). If a topic you want is only in those channels, confirm
it's been said publicly before including it.

## 🔁 Carry-forward from September (unused, still relevant?)
- [ ] NextNav friction (recurring) — only if raised publicly
- [ ] Review ~90 unused Sept candidates (issues/2026-09/data/candidates-aug-sep.json) for public ones

## 🔂 Recurring anchors (default-include)
- [x] Weekly Net reminder (Thursdays)
- [x] Get the Mesh Client (Joey NV0N)
- [x] "No RF needed — try Reticulum on the RRC hub"
- [x] Airtime etiquette reminder
- [ ] Run an observer in your area
- [ ] MeshCore naming convention

## 🧵 Follow-ups on September threads (status check)
- [ ] **BARCFest RECAP** — happened Oct 4; we previewed it. How'd it go? (confirm from a public post)
- [ ] **500 kHz profile** — Sept was "testing toward"; result now? (SNR sweeps discussed internally — need a public update)
- [ ] **Scopes / Chicagoland naming trial** — the Chicagoland trial IS public (#meshcore); the scope-definition debate itself is internal, don't quote it
- [ ] **MediumFast migration** — adoption update (public channels only)

## 🆕 Net-new October themes (PUBLIC-sourced — safe to include)
- [ ] **EmComm / MECP** — the Mesh Emergency Communications Protocol; public in #emcomm-network-ops, #mecp, #mesh-client. Likely lead story. [CONFIRM #emcomm-network-ops is a public channel]
- [ ] **Mesh Client V6 (Wayland)** — public in #general/#mesh-client/#software
- [ ] **Chicagoland Naming Convention trial** — public in #meshcore (Ed)
- [ ] **CoreScope → Beacon** — analyzer change, public in #meshcore/#general
- [ ] **Admin / leadership updates** — from #announcements (public ✓)
- [ ] **Reticulum: BBS + mobile posting; security audit passed** — public in #reticulum

## ⚠️ Needs a PUBLIC source before including
- [ ] **PRA Repeater is up** (JohnnyW5KV) — only found in #mesh-planning (internal). Likely announced publicly too; confirm a public post before publishing.
