![header](../assets/header.png)

# The Week in Seed: The Money Went to the Senses — Touch, Identity and Measurement

### A hand that can feel, a badge system for software that borrows human logins, and a laser ruler for orbit

A quieter week at the top of the cap table, and a more telling one: the checks went to the unglamorous layer underneath the thing everyone demos.

## Robots have a brain problem solved and a hand problem open

General-purpose AI models can now describe how to seat a gasket or mate a connector. They still can't do it, because the last few millimetres of manipulation depend on feel: contact, slip, resistance, the half-second correction a human hand makes without thinking. That is a sensing and control problem, not a language problem, and no amount of model scale on the cognitive side closes it.

Why now: tactile sensing has gotten cheap enough to put on every fingertip, and learned control finally has a data source other than hand-coded trajectories. The winners will be whoever owns the touch-and-motor-skill layer that sits between a foundation model and a gripper — and the losers are integrators selling bespoke, hard-coded assembly cells that break when a part changes by a millimetre. The underwriting question is whether that layer stays a standalone product or gets absorbed by the robot makers it needs to sell to.

### Tangent Robotics — $4.5M pre-seed (led by Fly Ventures and Toyota Ventures)
- **Problem:** Robot hands lack the fine motor skills for contact-rich factory work (assembly, threading, connector mating, gasket seating, snap fitting, gear meshing); the founders call it a layer "currently missing in robotics but omnipresent in the real world."
- **Product:** A stack combining light-based touch sensors, dexterous robotic hands, and machine-learned motor skills.
- **Customer:** Manufacturers with precision assembly lines that still rely on human hands — a production or automation engineering lead with a task too variable for a fixed cell.
- **Stage:** First disclosed round, $4.5M pre-seed, with Logos Fund and Sparked Ventures participating; a New York company spun out of Columbia, founded in 2025. Customers and pilots were not disclosed ([announcement](https://www.citybiz.co/article/912007/tangent-robotics-raises-4-5-million-pre-seed-to-advance-robot-dexterity/)).
- **TAM:** Not quantified in the announcement, and no estimate was sourced this run.
- **Moat:** Thin on paper, so the bet is on vertical integration — sensor, hand and learning stack tuned together — and on the founders' academic lab lineage. Underwriting question: does a hardware-plus-software bundle beat a robot maker simply buying a good touch sensor?

## Identity is being rebuilt for software that isn't a person

Security stacks assume that a login belongs to a human or a clearly labelled service account. AI agents break that: they act through a person's session, borrow credentials, and hold access that no one explicitly granted. When an agent misbehaves, the logs say a human did it.

This is the same direction the agentic-security category has been moving for several weeks running: the identity layer, not the model, is where the control point sits. What's new is that it is no longer a pitch — buyers with large estates and compliance obligations are deploying it in production. Expect the incumbents' identity platforms to bolt on agent attribution; the open question is whether a dedicated correlation layer is a product or a feature on someone else's roadmap.

### [Rig Security](https://rig.security) — $12M seed (co-led by Ten Eleven Ventures and Brightmind Partners)
- **Problem:** AI agents operate through human and machine identities, so existing tools can't tell the agent from the person whose session it uses; the company cites roughly three in four breaches involving compromised identities.
- **Product:** An identity-protection platform built on a proprietary correlation engine (RICE) that resolves identities across cloud, on-prem and identity-provider systems, plus an endpoint sensor for runtime attribution and policy enforcement. It claims 96%+ correlation accuracy — a vendor figure, not independently verified.
- **Customer:** Large regulated enterprises (the company names financial services, insurance, healthcare and tech) whose security team has to answer "which agent did this?" after an incident.
- **Stage:** $12M seed, with the CrowdStrike Falcon Fund and Wiz co-founder Ami Luttwak as backers; founded by Guy Kozliner (CEO), Nokky Goren (CTO) and Michal Haikov (Head of Product), and says it is already in production at Fortune 200 customers, listed on AWS and CrowdStrike marketplaces. Round size and customer count beyond that were not disclosed ([announcement](https://finance.yahoo.com/technology/ai/articles/rig-security-emerges-stealth-define-120000698.html)).
- **TAM:** Not disclosed by the company; no analyst estimate was sourced this run.
- **Moat:** Data gravity: the more environments the correlation engine ingests, the better its mapping of who-is-who gets. Weak point is distribution — the strategic investor on the cap table is also a platform that could build the same thing.

## Space's next bottleneck is knowing exactly where everything is

Launch got cheap, then bandwidth and power became the story. The next constraint is quieter: with tens of thousands of objects in orbit and more arriving, operators need to know where their hardware actually is — and where everyone else's debris is — to a precision that radar and legacy geodesy weren't built for. Positioning accuracy underpins collision avoidance, navigation resilience and Earth observation alike.

The old infrastructure is scarce, expensive and manually operated, and the argument is that automation turns a scientific technique into a metered service. Winners are those who control both the network and the hardware flying on satellites; losers are legacy facilities priced for a research budget.

### [Foundational](https://foundational.space) — £8.2M pre-seed (backed by Inflection, BACKED, Final Frontier, Adjacent and Type One Ventures; no lead disclosed)
- **Problem:** Satellite operators need millimetre-grade tracking, while existing geodetic infrastructure is sparse, costly and aging — the company cites a UN warning that it is "perilously close to collapse."
- **Product:** A vertically integrated satellite laser ranging network: retroreflectors fitted to satellites, automated weatherproof ground stations (claimed roughly 30x cheaper than legacy facilities) and a software platform that processes and delivers the data.
- **Customer:** Operators of low-Earth-orbit constellations and government space and navigation agencies that need precise orbit and positioning data on demand.
- **Stage:** £8.2M (about €9.6M) pre-seed, billed as Europe's largest space-tech pre-seed; London-based, founded in 2025 by Hira Virdee (CEO, previously founded Lumi Space) and Dave Gooding. The company lists the European Space Agency, UK government bodies, constellation operators and aerospace manufacturers as customers; contract values were not disclosed ([announcement](https://foundational.space/news/foundational-emerges-from-stealth)).
- **TAM:** Not specified; the company's only sizing context is that ESA tracked roughly 45,000 orbital objects at end of 2025.
- **Moat:** Owning the retroreflector on the satellite creates a hardware hook competitors can't replicate from the ground, and the founding team's prior laser-ranging work is real experience. The skeptic's question: can it get operators to fly its reflectors before a scale network exists to justify them?

## What to watch next week

Whether a large identity or endpoint-security platform announces native agent attribution, which would test how long a standalone correlation layer stays independent. Also whether more touch-and-dexterity rounds follow — one pre-seed is a data point, a cluster is a category. A geography note, as an observation only: one US, one Israel-founded and one UK company this week.
