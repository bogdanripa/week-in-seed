![header](../assets/2026-07-17-header.png)

# The Week in Seed: Investors Funded the Plumbing, Not the App

### Two founders raised $81M for enterprise identity and IT ops, Germany's biggest seed went to robot data, and $6M funded satellite bandwidth.

This week's seed checks skipped the interface layer almost entirely. The biggest money went to two founders rebuilding enterprise identity and back-office operations as a single system instead of another point tool bolted onto the mess that's already there. Alongside them, a robotics-data company and a satellite-optics startup got funded for fixing problems one layer beneath the products people actually see — training data and bandwidth, not chatbots.

## This week's trends

1. **Enterprise seed money is buying control planes, not features.** Oak ($60M) and Thira ($21M) are both pitching a from-scratch operating layer — identity, back-office execution — instead of a plug-in on top of the existing stack, betting that CIOs are done patching and ready to rip out.
2. **Robots need a data supply chain before they need smarter software.** microagi's $55M round, Germany's largest seed ever, went to the "shovel" that captures human motion and feeds it to robotics models — not to a robot company itself.
3. **Space's bottleneck moved from launch cost to bandwidth.** A $6M seed for compact laser communication terminals shows investors chasing one narrow choke point in orbit, even as bigger defense and space rounds grabbed the week's larger headlines elsewhere.

## Enterprise seed money is buying control planes, not features

Identity governance and administration is pegged at roughly $8.4B–$10.7B in 2026, headed toward $17B–$33B by the early 2030s depending on whose scope you use (Fortune Business Insights, 360iResearch) — estimates that disagree by a factor of two on how big the category even is today. The adjacent world of IT process automation is on a similar trajectory, from about $10.6B now toward $20B+ by 2030. Two rounds this week bet both categories get rebuilt now that AI agents, not just humans, need to be governed and put to work.

### [Oak](https://www.oak.id/) — $60M seed (co-led by Accel, CRV, and Greylock Partners)
- **Problem:** legacy identity and access management was built to govern humans logging into cloud apps; it wasn't built for machine identities and AI agents that now outnumber human accounts and change their own permissions.
- **Product:** a unified identity control plane that continuously maps who and what has access to which systems, stripping unneeded permissions in real time instead of during a periodic audit.
- **Customer:** CISOs and IAM leads at large enterprises already running a patchwork of disconnected identity tools — the buying trigger is an AI-agent rollout that breaks the old audit cadence.
- **Stage:** $60M seed, raised quietly in late 2025 and publicly announced this week, co-led by Accel, CRV, and Greylock Partners with AlphaDrive Ventures, Hetz Ventures and angels; the product is already generally available with unnamed enterprise customers live ([announcement](https://techcrunch.com/2026/07/15/backed-by-60m-in-funding-oak-steps-out-of-stealth-to-fix-the-identity-mess-that-ai-agents-are-making-worse/)).
- **TAM:** identity governance and administration runs $8.4B–$10.7B in 2026, headed toward $17B–$33B by the early 2030s — a wide analyst spread (Fortune Business Insights, 360iResearch), all estimates.
- **Moat:** founder Shai Morag has three prior cybersecurity exits (Integrity-Project to Mellanox, Secdo to Palo Alto Networks, Ermetic to Tenable), which buys credibility and a CISO Rolodex, not necessarily product durability — Okta, SailPoint and Saviynt are all bolting agentic features onto entrenched distribution, and Oak has to win on clean-slate architecture before they catch up.

### [Thira](https://www.thira.com/) — $21M seed (led by Madrona)
- **Problem:** enterprises lose a stated $1 trillion a year to manual, cross-system back-office work — resetting accounts, provisioning laptops, approving purchases — that no single tool owns end to end.
- **Product:** a "system of execution" — self-learning AI agents wired into an enterprise knowledge graph, with governance and audit trails built in, meant to actually complete multi-step workflows rather than just recommend the next step.
- **Customer:** CIOs and enterprise IT leaders under pressure to cut back-office headcount without losing compliance — the trigger is the gap between what copilots promise and what they actually finish.
- **Stage:** $21M seed led by Madrona, with FUSE and a group of CIO and advisor angels; 10 enterprise design partners ahead of a fall launch, pre-revenue ([announcement](https://www.businesswire.com/news/home/20260714608171/en/Thira-Raises-$21-Million-Seed-Round-Led-by-Madrona-to-Build-the-Back-Office-That-Runs-Itself)).
- **TAM:** Thira cites $1 trillion in annually wasted enterprise IT spend — the company's own framing, not an independent estimate; the narrower IT-robotic-automation market analysts track independently is $10.6B in 2026 growing toward $20B by 2030, a large gap between the aspirational number and the market that exists today.
- **Moat:** founders Sunny Gupta and Kurt Shintaffer built and sold Apptio, so they know how to sell into IT budgets — but "system of execution" is also ServiceNow's stated direction, and Thira is still pre-launch against an incumbent that already owns the CIO relationship and the ticketing data.

## Robots need a data supply chain before they need smarter software

Estimates for the broader "physical AI" market span wildly, from $81B–$110B today to anywhere between $430B (2030) and $1.6T (2040) depending on scope (Grand View Research, MarketsandMarkets) — analysts can't agree on the category's edges. The narrower slice for robot-perception training data and labeling is estimated at roughly $18.4B annually by 2030. Whatever the real number, the constraint right now isn't compute or model architecture — it's that, as Berkeley roboticist Ken Goldberg has put it, robots have nothing like the internet's text corpus to learn from.

### [microagi](https://www.microagi.ai/atlas) — $55M seed (led by Hummingbird)
- **Problem:** robotics models have no equivalent of the internet to pretrain on — real-world manipulation data is scarce, and what exists rarely transfers cleanly from one factory's tasks to another's.
- **Product:** Atlas, a hardware- and model-agnostic platform that records workers on cameras and sensor-equipped gloves through its "shift" data-collection network, then uses that footage to fine-tune existing robotics models for a specific customer's production line.
- **Customer:** manufacturers in automotive, logistics and food production trying to move robots from pilot demos into actual production, without betting on one robot vendor or one foundation model.
- **Stage:** $55M seed — Germany's largest ever — led by Hummingbird, with Northzone, LocalGlobe, Village Global and Redalpine; five companies are live on the data-collection side and one is preparing its first production deployment, roughly 10 months after founding ([announcement](https://sifted.eu/articles/munich-robotics-startup-microagi-raises-55m-germanys-largest-ever-seed-round)).
- **TAM:** robot-perception training data and labeling is estimated at ~$18.4B annually by 2030; zoom out to the full physical-AI market and estimates range from $430B (2030) to well over $1T by the late 2030s — a spread wide enough to say the category boundaries aren't settled yet.
- **Moat:** shift's 20,000-plus paid contributors across 15 countries is a real data-sourcing edge today, but gig-sourced footage of people doing chores in exchange for free apartment cleanings is a different quality bar than a robotics lab's own curated demonstrations — the underwriting question is whether crowd-collected data is good enough to fine-tune a production-line robot, or just good enough to raise a round.

## Space's bottleneck moved from launch cost to bandwidth

Estimates for the optical (laser) satellite communications market range from roughly $0.6B–$3.3B today to $1.6B–$27B by 2030–2035, depending on which research firm's scope you use (MarketsandMarkets, Business Research Insights, Mordor Intelligence) — even the analysts don't agree on how big "laser comms" is yet. What they agree on: as more compute moves into orbit, the radio-frequency links satellites use today can't keep up.

### [Ravee Optics](http://raveeoptics.com) — $6M seed (led by BIG Capital)
- **Problem:** satellites can already collect more data than they can transmit to Earth or to each other — optical laser links solve the bandwidth problem, but existing laser terminals are too bulky and expensive for most small-satellite operators.
- **Product:** ultracompact optical communication terminals built with meta-optics on silicon wafers instead of traditional bulky lenses, claiming 10–100x the throughput of current standards in a smaller, cheaper package.
- **Customer:** government and commercial satellite operators, particularly the emerging wave of orbital data-center and small-satellite constellation builders who can't afford or fit legacy laser terminals.
- **Stage:** $6M oversubscribed seed led by BIG Capital, with JobsOhio Ventures and CincyTech; the Dayton, Ohio team has already generated early revenue through testing programs and demonstrated its core optics via a U.S. Air Force program ([announcement](https://www.businesswire.com/news/home/20260713438881/en/Ravee-Optics-Secures-$6-Million-Seed-Round-as-the-Need-to-Move-More-Data-in-Space-Explodes)).
- **TAM:** optical satellite communications estimates range from $0.6B–$3.3B in 2025 to $1.6B–$27B by 2030–2035 — a wide analyst spread, but consistent double-digit growth in every version.
- **Moat:** founders Piyush Shah and Augustine Urbas bring Air Force Research Lab optics experience, and manufacturing meta-optics on silicon wafers is a real cost and size edge over bulky legacy terminals — but the same manufacturability argument is what every laser-comms challenger makes, and $6M buys engineering time, not yet a flown, proven product.

## What to watch next week

This week's four rounds skewed heavily toward the US and Israel (Oak, Thira, Ravee Optics), with Germany's microagi as the lone outlier — worth flagging, not correcting, especially since the week's largest defense and space megadeals (Helsing, Quantum Systems) landed in Europe while the seed-stage money covered here went mostly stateside. Asia and Latin America were blind spots again this week. Watch whether Oak and Thira's "control plane" pitch draws an incumbent response (Okta, ServiceNow) before either startup gets past its design-partner stage, and whether microagi's gig-sourced data holds up on an actual production line rather than a pilot.
