![header](../assets/header.png)

# The Week in Seed: The Bottleneck Moved From the Brain to the Fingertips and the Wiring

### A touch-sensing robotics pre-seed, a startup untangling the cables inside quantum computers, and two seed rounds that arrived with a measured result already attached: crop yields and subscriber growth

A week when the interesting money went below the model layer, plus two companies that came with their numbers in hand.

## Machines are hitting a signal problem, not an intelligence problem

For two years the physical-AI story was about brains: bigger models, more demonstration data, smarter planners. The constraint is now shifting to the plumbing that carries information between the machine and the world. A robot that cannot feel how hard it is gripping fails at the last centimetre of a task, however good its planner is. A quantum processor that needs a thicket of cables per qubit cannot grow past the point where the cables no longer fit in the refrigerator. Different fields, same shape: capability is bounded by the channel, and the channel is mostly custom, expensive and fragile today.

That is attractive seed territory because the channel is a component, and components sell to many builders. If you supply the sensing layer or the signal-handling layer, you win when any of your customers wins, without having to beat them at their own game. The risk is the mirror image. Component vendors depend on a small number of buyers who may build in-house once the category proves out, and hardware timelines are long enough that the funding can run out before the first design win.

Who loses? Teams whose robotics or quantum roadmaps assume today's sensors and wiring will stretch another order of magnitude, and integrators who have been papering over the gap by hand. The honest caveat is that both bets are early: neither company discloses a paying customer, so this week's round sizes are a statement about the bottleneck, not about demand.

### [Enact Intelligence](https://enact-intelligence.com/) — $30M pre-seed (no lead disclosed; investors include redalpine, Notion Capital and firstminute capital)
- **Problem:** Most robots lean mainly on cameras, which makes grasping and fitting unreliable. Existing force- and touch-sensing options are described as too expensive and fragile for factories.
- **Product:** A full stack for robots that feel: its own sensors and actuators, a "nervous system" that senses force across the body down to the fingertips, and a "cortex" model that interprets those signals and controls movement. It adapts existing video models to generate robot motion and is meant to fit anything from an arm to a humanoid.
- **Customer:** Manufacturers with fiddly final-assembly steps (inserting plugs, snapping clips, driving screws), starting with European companies in manufacturing, infrastructure, retail and food processing, which the company says it is in talks with.
- **Stage:** $30M pre-seed, about €27M, announced on exiting stealth. Angels include Yann LeCun, Arthur Mensch and Andrew Lonsberry. The company was founded in March by CEO Manuel Yves Galliker, who previously led the team that taught 1X's NEO robot to walk and later worked at Physical Intelligence; the team is about 12 people. No performance data or named customers have been published; the plan is to quintuple headcount by the end of 2027 ([announcement coverage](https://www.trendingtopics.eu/enact-pre-seed-yann-lecun-mistral-robotics/)).
- **TAM:** No reliable market-size estimate found. The company's own adoption statistic is the best anchor: it says 4.6% of German small and mid-size companies use robots versus 24% of large ones, which frames the opportunity as unlocking the smaller manufacturers.
- **Moat:** Owning sensors, actuators and models together is the only version of this that sticks, because a software-only layer gets copied. The underwriting question is whether a 12-person team can ship durable hardware before the money, which is large for pre-seed, is spent on research alone.

### [Coherence Quantum](https://coherencequantum.tech) — €2.78M seed (led by Lifeline Ventures)
- **Problem:** Every added qubit multiplies the control and readout signals that must reach the processor, while space and cooling power inside the cryostat are scarce and the qubits must be shielded from thermal noise.
- **Product:** An integrated cryogenic signalling and control platform for solid-state quantum computers. It starts with cryogenic signal conditioning, then higher-density signal interfaces, then more control functionality inside the cryostat, closer to the processor.
- **Customer:** Builders of solid-state quantum computers who need an architecture that supports larger systems. The company names no customers.
- **Stage:** €2.78M seed led by Lifeline Ventures with Mårten Mickos participating; no earlier round is mentioned. The Aalto University spinout has spent over two years designing and testing cryogenic prototypes, including validation in dilution refrigerators with qubit systems. Founders are CEO Aashish Sah, CTO Suman Kundu and CPO Erkki Soininen, ex-Bluefors, with Aalto professor Mikko Möttönen as founding advisor. No revenue or pilots are disclosed ([announcement coverage](https://tech.eu/2026/10/20/coherence-quantum-raises-eur278m-to-tackle-quantum-computer-scaling-challenges/)).
- **TAM:** Estimates are tiny and wildly scope-dependent. One analyst puts cryo-CMOS quantum control electronics at about $15M in 2025 rising to roughly $410M by 2035; a broader cryogenic electronics estimate is about $1.35B in 2025. Both are vendor-published estimates with paywalled methods.
- **Moat:** Research lineage and prototype history in a field with very few people who can build this, plus the patent filings the company reportedly has pending. The underwriting question is concentration: a handful of quantum builders are the whole customer list, and any of them could choose to build this in-house.

## Seed rounds that arrive with a measured result

The recurring idea of recent weeks, money following proof, shows up again here in two unglamorous, very large markets. In both, the buyer can check the claim themselves without trusting a pitch. A farmer sees yield at harvest; a hobbyist hears whether they can play the song. That customer-verifiable outcome is what lets a young company sell for real money before it has a brand.

Both categories also share an old reliability complaint. Products that promise a biological or behavioural change have a long history of underdelivering, so buyers discount the claim until they see it. The startups that break through do it by making the result observable, early and cheaply, then putting the number in the marketing. The discount a skeptical customer applies is the opportunity.

The caution is that company-reported figures are not independent evidence. Trial averages hide a wide spread, and growth rates off an undisclosed base can look dramatic. Investors are paying for the direction of the numbers, not their size.

### [IMIO](https://www.imio.co/) — $12M seed (led by Sofinnova Partners)
- **Problem:** Biological crop inputs have a reputation for inconsistent cost, shelf stability and performance, while the nutrients locked in crop residue, harder to break down in modern higher-lignin corn, go unrecovered.
- **Product:** Re-Gen, a freeze-dried microbial powder applied to crop residue, typically in spring around planting, that releases nutrients; one version for row crops and one for produce. The powder has a shelf life of 12 months or more.
- **Customer:** Corn and other row-crop growers, plus specialty growers (broccoli, Brussels sprouts, lettuce), with the company now starting to work through distributors.
- **Stage:** $12M seed led by Sofinnova Partners with Cultivate Next (Chipotle's venture fund), Starshot Capital, Grow Together Salinas, Earth Foundry and Serra Ventures; $16.5M raised in total. About 100 customers and small commercial revenue for a couple of years. Company-reported trials on over 10,000 Midwest acres in 2024 and 2025 showed an average corn yield gain of 11.9 bushels per acre, within a range of roughly 5 to 20+. The money funds a Chicago biomanufacturing and R&D site, expected to be finished in Q2 2027 ([announcement coverage](https://agfundernews.com/imio-raises-12m-to-unlock-nutrients-trapped-in-crop-residues-with-new-generation-of-dependable-ag-biologicals)).
- **TAM:** Analyst estimates put all agricultural biologicals at roughly $17–20B in 2025 and about $31–39B by 2030 (MarketsandMarkets, Lucintel and others); the residue-management slice is a small part of that, and no one sizes it separately.
- **Moat:** A shelf-stable formulation and a manufacturing process, which is the hard part of biologicals; strain discovery is easier to imitate. The question is whether an average gain that wide in range holds up across soils and seasons, since that spread is what has hurt the category before.

### [ArtMaster (Artie)](https://artmaster.com/artie) — $2.4M seed (investors include Factorial Capital, Reflex Capital and Moises)
- **Problem:** Beginners make several mistakes at once, and video lessons give no individual feedback; a human teacher is costly and scarce.
- **Product:** Artie, an iOS-only AI piano-learning app that listens through the microphone or connects by MIDI, gives real-time feedback, builds a step-by-step learning path and includes an AI assistant. Piano only for now, with guitar, other instruments and Android on the roadmap. It is priced at $34.99 a month or $149.99 a year after a limited free tier.
- **Customer:** Adult beginners and solo practisers who want teacher-style feedback at app prices.
- **Stage:** $2.4M seed with new investors Factorial Capital, Reflex Capital and Moises; earlier backers include Robert Kyncl and Jaroslav Beck's JARO Capital and Purple Ventures, which led an €800K+ round in March 2025. Total raised is not stated. Company-reported traction: over 500,000 users, and paying subscribers and monthly recurring revenue each growing around 38–39% month over month since October 2025, off undisclosed absolute figures. The Prague company grew out of a music school started in 2018 ([announcement coverage](https://www.musicbusinessworldwide.com/ai-piano-learning-startup-artmaster-previously-backed-by-robert-kyncl-raises-2-4m-seed-round-with-moises-among-new-investors/)).
- **TAM:** The company cites more than 700 million people learning music worldwide and 65 billion hours a year, about 50 billion of them solo practice. No source was given, so treat this as a marketing estimate, not a market size in dollars.
- **Moat:** Thin on technology; the defensible assets are the audience built through social video and a data set of how learners actually play. The question is retention: 500,000 users is reach, and a subscription at that price only works if beginners stick past the first month.

## What to watch next week

- Whether Enact names a first industrial partner or a lead investor, which would say how real the demand is behind the headline cheque.
- Whether more seed rounds go to components and interfaces rather than whole robots or whole quantum computers.
- Whether any of the company-reported numbers this week, from crop trials to subscriber growth, get an independent check.
