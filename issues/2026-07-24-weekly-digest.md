![header](../assets/header.png)

# The Week in Seed: AI Graduated From Advisor to Operator

### $15M taught an AI to run a call center, $15M more taught one to run a steel factory, $2.65M went to guard the code AI agents write, and €4.5M went to beaming power at satellites in orbit.

This week's seed money skipped the pilot stage. Two rounds funded AI systems built to fully run something — a customer-support line, a steel-fabrication floor — instead of assisting a human who still owns the outcome. A third round bet on the flip side of that shift: someone has to guard the code those systems ship. And in orbit, the infrastructure buildout that funded satellite bandwidth last week moved one bottleneck over, to satellite power.

## This week's trends

1. **AI seed money graduated from advisor to operator.** telli's agents now run full customer conversations end-to-end across five channels, and 1872's Factory OS is meant to run an entire steel-fabrication line without a human in the loop — a bet against the industry's own adoption data, which shows most agentic AI projects never make it to production scale.
2. **Someone has to guard the code the new AI operators write.** Ossprey raised to catch malicious open-source packages before they reach production, a problem AI coding assistants are making worse by expanding the dependency surface faster than security teams can review it.
3. **Space's infrastructure story moved from bandwidth to power.** A week after a seed round funded satellite communication terminals, another funded satellite power delivery — investors are working down the list of orbital bottlenecks one narrow slice at a time.

## AI seed money graduated from advisor to operator

Enterprise agentic AI is pegged at roughly $9.9B in 2026, headed toward $24.5B–$46B by 2030 depending on scope (Grand View Research, MarketsandMarkets) — but adoption data undercuts the growth curve: task-specific AI agents are expected in 40% of enterprise applications by the end of 2026, yet only 23% of organizations have actually gotten one scaled into production, and over 40% of current agentic projects are forecast to be canceled before 2027. Two rounds this week bet on the minority that ships.

### [telli](https://telli.com) — $15M seed (led by Redalpine)
- **Problem:** B2C companies' customer-facing operations — sales, service, support — have outgrown what a human-staffed contact center and static IVR menus can handle across voice, chat, SMS, WhatsApp and email at once.
- **Product:** an AI agent platform built around "Charlie," an AI coworker that builds, deploys and monitors voice and chat agents that carry full conversations — qualifying leads, booking appointments, collecting payments, handling support — rather than routing to a human after the first message.
- **Customer:** ops leaders at B2C companies in high call-volume categories (real estate, healthcare, solar/HVAC, insurance, telecom) who need to scale conversation volume without scaling headcount — the trigger is inbound/outbound call load a human line can't staff economically.
- **Stage:** $15M seed (total raised $18.5M+) led by Redalpine, with Mutschler Ventures, Cherry Ventures, Y Combinator and angels; agents already handle millions of conversations for customers including Sky, Viessmann, Enpal, Vaillant, 1KOMMA5° and Clark ([announcement](https://tech.eu/2026/07/23/telli-secures-15m-seed-to-automate-customer-facing-operations/)).
- **TAM:** AI-driven customer service software runs about $15B in 2026, headed toward $32B–$82B by 2030–2034 depending on whose scope you use (Grand View Research, Fortune Business Insights) — all estimates, wide spread.
- **Moat:** named enterprise logos and millions of handled conversations are real distribution today — but voice-agent platforms are multiplying fast, and "handles the conversation" isn't yet the same claim as "handles it at a lower error rate than the human line it replaces," which is the number that actually stops a CFO from switching vendors.

### [1872](https://1872.ai) — $15M seed (from private funds advised by The O.H.I.O. Fund)
- **Problem:** heavy steel fabrication for modular construction and infrastructure runs on manual coordination, with lead times stretching months to years because no single system owns sourcing, scheduling, welding and logistics together.
- **Product:** Factory OS, a proprietary AI platform that ingests CAD files, plans and schedules production, and directs robotic welding (via Path Robotics' Obsidian system) and material movement across the shop floor — aiming to compress lead times to weeks.
- **Customer:** modular-construction and infrastructure developers who need large structural steel components (frames, skids, enclosures) fast — the buying trigger is a lead-time crunch a traditional fab shop can't compress.
- **Stage:** $15M seed — one of Ohio's largest ever — from private funds advised by The O.H.I.O. Fund; founded by three ex-SpaceX engineers led by CEO Dan Summers, the Cincinnati facility is running early automation now, with full autonomy targeted for 2027 ([announcement](https://www.businesswire.com/news/home/20260722906712/en/1872-Launches-Autonomous-Steel-Fabrication-Factory-Model-in-Cincinnati-and-Closes-%2415-million-Seed-Funding-Round)).
- **TAM:** 1872 cites the $350B U.S. fabricated metal products market as its opportunity — the company's own framing, not an independent estimate; the broader industrial robotics market analysts track separately spans a wide $15B–$65B in 2026 depending on scope, itself a sign of how unsettled "how big is factory automation" still is.
- **Moat:** SpaceX-caliber manufacturing-ops pedigree is a real hiring and credibility edge, and a single vertically integrated facility is hard to copy overnight — but 1872 owns exactly one factory today, "full autonomy" is a 2027 promise rather than a 2026 fact, and the competition is every regional fab shop's ability to just hire more welders.

## Someone has to guard the code the new AI operators write

Open-source code already makes up roughly 90% of enterprise software, and AI coding assistants are expanding that dependency surface faster than security teams can review it — attackers don't submit malicious packages for cataloging, so new threats can sit live in public registries for days before anyone flags them. The category that catches this is still small: software supply-chain security is valued at about $2.16B in 2026, with most forecasts putting 2030s growth at only $3B–$3.4B (a single-digit-to-low-double-digit CAGR) — modest next to most AI-security pitches, and a real cap on how big a standalone "catch the bad package" business gets on its own.

### [Ossprey](https://ossprey.com) — $2.65M pre-seed (led by Episode 1 Ventures)
- **Problem:** with open source underpinning nearly all enterprise software, and AI coding tools accelerating how fast new dependencies get pulled in, security teams can't keep pace vetting packages against known-vulnerability databases alone — the threats that matter haven't been cataloged yet.
- **Product:** a detection engine using static analysis and behavioral techniques to flag suspicious activity inside open-source packages and AI-agent-generated code, scoring severity by malicious intent rather than matching against existing CVE databases.
- **Customer:** engineering and security teams at fast-moving companies adopting AI coding tools — particularly CTOs worried their open-source blind spot is growing faster than headcount to review it.
- **Stage:** $2.65M pre-seed led by Episode 1 Ventures, with Osney Capital and Octopus Ventures; founded in 2026 by Nate Dunning and David Read, funds go toward product development and expansion across the UK, Europe and North America ([announcement](https://www.vestbee.com/insights/articles/ossprey-lands-2-65-m)).
- **TAM:** software supply-chain security runs roughly $2.16B in 2026, with most estimates reaching only $3B–$3.4B by the early 2030s (Verified Market Reports, Custom Market Insights) — a smaller, slower-growing category than the AI-security label usually implies.
- **Moat:** behavioral detection catches novel threats signature-based tools miss, a real technical edge today — but it's also a feature the well-funded software-composition-analysis incumbents (Snyk, Socket, Sonatype) could bolt on, and $2.65M buys engineering time, not yet a defensible data or distribution advantage.

## Space's infrastructure story moved from bandwidth to power

Wireless power transmission overall is estimated at $14B–$18B in 2025–2026, headed toward $48B–$105B by the early-to-mid 2030s (Market Research Future, Future Market Insights) — but that figure spans consumer electronics and EVs too; the orbital-power slice is a fraction analysts haven't broken out separately yet. What's clear is the direction: as more spacecraft and payloads go up, power delivery — not just data delivery — is becoming its own funded category.

### [ORiS](https://oris-space.com) — €4.5M pre-seed, €5.7M with a regional grant (led by Earlybird)
- **Problem:** satellites lose power availability during eclipse periods and as solar panels degrade over a mission, and the only fix today is bigger batteries and panels — mass and cost that get harder to justify with every added constraint.
- **Product:** space-qualified laser terminals that beam power directly to a receiving satellite's existing solar arrays with no hardware modification required, using autonomous tracking and sub-microradian pointing accuracy.
- **Customer:** satellite operators — especially smaller-spacecraft and hosted-payload operators — who need to extend mission life or keep operating through eclipse without redesigning the spacecraft.
- **Stage:** €4.5M pre-seed (€5.7M including a regional grant) led by Earlybird, co-led by Pitchdrive, with Galaxia, Vento and Piemonte Next Fund; the Turin-based team has beamed power to drones 100m away in ground tests, has a NATO DIANA-backed terrestrial system, and is targeting a Q1 2027 in-orbit demo with D-Cubed ([announcement](https://spacenews.com/italian-startup-oris-raises-funding-for-laser-power-beaming-technology/)).
- **TAM:** wireless power transmission spans $14B–$18B today to $48B–$105B by the early-to-mid 2030s (Market Research Future, Future Market Insights) — a figure dominated by terrestrial and consumer uses; the orbital-power niche ORiS is chasing is a slice analysts haven't sized on its own.
- **Moat:** NATO DIANA backing and a named 2027 flight demo are real, verifiable milestones most seed-stage space startups don't have yet — but ORiS is still pre-flight, and the same laser-power-beaming pitch is being made by well-funded rivals like Mantis Space ($10M+ seed) and the Space Force-backed Pulse Space, so the underwriting question is who actually gets hardware into orbit first, not who has the best simulation.

## What to watch next week

This week's four rounds spread wider than most — Germany (telli), the US (1872), the UK (Ossprey) and Italy (ORiS) — with zero Bay Area rounds among the featured deals, worth flagging as a real pattern rather than something to correct for. Watch whether telli and 1872 can show a cost or error-rate number that proves their AI is actually cheaper than the humans it replaces, not just capable of the same task; whether Ossprey's behavioral-detection edge survives incumbents copying the approach; and whether ORiS's 2027 in-orbit demo with D-Cubed actually flies on schedule.
