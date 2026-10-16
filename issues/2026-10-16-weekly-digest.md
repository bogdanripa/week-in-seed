![header](../assets/header.png)

# The Week in Seed: When AI Writes the Code, the Seed Money Goes to Whoever Tests It

### Three startups that test software, enterprise processes and corporate defenses with agents, a chip meant to replace a robot's whole processor stack, and a Stockholm bank that returns its fee income to customers

A week where the checks went to the people who verify things, plus two bets on rebuilding something old from the bottom.

## Testing is becoming the bottleneck, so testing is becoming the product

This is the third issue in a row where seed money has landed on verification, after the "check, not the output" week in September and last week's robot testers. The logic keeps getting stronger. Generating code, configurations and business logic with models is now cheap and fast; confirming that any of it works, safely, in a real environment, has not gotten cheaper at the same rate. When output volume rises and review capacity doesn't, the scarce thing is trust, and whoever sells trust at a predictable price has a business.

Three flavors are visible this week, and they attack three different budgets. Functional testing sells into engineering and QA, where the pitch is replacing hand-maintained scripts that break whenever a UI changes. Enterprise-process assurance sells into the teams running multi-year system migrations, where a missed edge case surfaces as a production outage in finance or supply chain. Offensive security sells into the CISO, where the argument is that an annual penetration test is a snapshot of an environment that changes daily, while attackers now use automation too.

Who wins? Vendors whose results a buyer will accept as evidence: an auditor, a regulator, a board. Who loses? Services firms that bill by the hour for manual test cycles, and point scanners that report noise. The skeptic's case is that testing is a feature the code-generation platforms will bundle, and a standalone vendor needs a reason to be the independent party. Independence is the whole product here, so that reason exists, but it must be earned in each sale.

### [Klarent](https://klarent.ai) — $8M seed (led by Mosaic Ventures)
- **Problem:** AI coding tools are raising the volume of code teams ship, while the test suites that guard it are still scripted and maintained by hand, and break whenever the interface moves.
- **Product:** A multi-agent platform that explores an app, plans test cases, writes the test code, runs it on a schedule or in CI, and proposes a fix with a diff for human review when a UI change breaks a test. Language models write the tests, which then run deterministically.
- **Customer:** Enterprise engineering and QA teams, with the company pointing at finance, insurance, travel, retail and media, who ship web and mobile apps frequently and cannot staff manual regression testing.
- **Stage:** $8M seed from Zurich; reported at €7.13M in euro-denominated coverage, probably a currency conversion. Moonfire Ventures and angels including a former Google director participated. Founders Asheem Panakkat and Momchil Ivanov are former Google engineers. The company names NZZ, Sixt and JD Sports as customers; revenue and contract sizes are not disclosed ([announcement coverage](https://angelinvestorsnetwork.com/startups/klarent-raises-8-million-seed-round-to-expand-ai-powered-software-testing-in-the)).
- **TAM:** Analyst estimates for automation testing range from roughly $25–30B in 2025 to $60–136B by 2029–2030 depending on the publisher and scope (ResearchAndMarkets, Grand View Research). Treat all as estimates; definitions differ widely and much of it is services spend.
- **Moat:** Thin on technology, since the pieces are available to any competent team. The case rests on accumulated app-specific test history and on reliability: it only works if the self-healing fixes are right most of the time. The company says it bills on verified test outcomes, which would be a sharp alignment if accurate, but that is a third-party description.

### Shamrock AI — $5M seed (led by Endiya Partners)
- **Problem:** Large enterprises migrating ERP systems, such as SAP S/4HANA, must test enormous numbers of interlinked business processes, and the teams who understand those processes rarely sit with the teams who write the tests.
- **Product:** An "agentic assurance" platform built around an enterprise knowledge graph that links business processes, systems, data and configurations, initially used to automate ERP-migration testing. The company plans to extend into data observability and process automation.
- **Customer:** Programme owners and IT leaders at large enterprises running a major ERP transformation, where a failed cutover has a visible cost.
- **Stage:** $5M seed, its first institutional round, with Capria Ventures participating; the company was founded in 2026 by Sarat Addanki, Anuraag Nallapati and Michael Gallagher, and is based in Shillong with offices in Hyderabad and San Francisco. It says it serves multiple Fortune 500 customers, including a Fortune 100 AI hardware maker and a Fortune 100 healthcare company, unnamed and with no revenue disclosed ([announcement coverage](https://inc42.com/buzz/shamrock-ai-bags-5-mn-to-help-enterprises-deploy-ai-agents-reliably/)). We could not locate an official website, so the name is unlinked.
- **TAM:** Not stated by the company. The nearest anchor is the same automation-testing estimate range above, of which ERP-migration testing is one segment; sizing for that segment alone was not found.
- **Moat:** The knowledge graph is the claim: each deployment encodes how a specific enterprise's processes actually run, and that context is hard to copy. The underwriting question is whether it stays a graph owned by the vendor or whether SAP and the large integrators build the same layer into their own migration tooling.

### [CodeWall](https://codewall.ai) — $4M pre-seed (led by Osney Capital)
- **Problem:** Periodic penetration tests leave gaps between assessments, and attackers can now automate entire attack chains.
- **Product:** Autonomous attack agents that probe an enterprise from the outside, with no credentials, source code or internal access, sharing findings through a persistent investigation graph so defenders can verify which paths are actually exploitable.
- **Customer:** CISOs and security teams at banks and other regulated enterprises that need continuous proof of exposure, not a yearly report.
- **Stage:** $4M pre-seed announced October 14, with InReach Ventures, Antler and angels also in, from a London base. CEO Paul Price is the only founder named. Axos Financial is a named customer through its CISO, and unnamed banks are also cited; revenue is not disclosed. The company's public profile rests on its own research, including the claim that its agent gained read and write access to the database behind McKinsey's internal AI platform within two hours, which are company claims, and one analyst called the write-up overstated ([announcement](https://codewall.ai/news/codewall-emerges-from-stealth-with-4m)).
- **TAM:** Analyst estimates for penetration testing are about $2B in 2025 rising to roughly $4.4B by 2031 (MarketsandMarkets), though the figure is roughly doubled or halved under other definitions. If agents replace consulting hours and expand coverage, the spend base is larger than the product category.
- **Moat:** Unproven. A reputation for finding real vulnerabilities is the early asset, and agent quality should compound with run data. The risk is that attack-agent capability is a model-driven commodity, and that buyers need the same independent standing as in any audit.

## Physical AI still runs on chips designed for something else

Autonomous machines carry a patchwork: one processor for sensing and signal handling, one for neural-network inference, one for real-time control, with data shuttled among them. That architecture was inherited from earlier products and it costs power, latency, board space and software complexity, all of which hurt most in drones and small robots. The case for a single reconfigurable processor is therefore easy to state and extremely hard to execute.

Why now: demand for autonomous hardware has become credible enough that a startup can pitch a new instruction-set-adjacent architecture without being laughed out of the room, and open RISC-V tooling lowers the software-ecosystem cost that has killed most challenger chips. Who wins if it works? Machine makers who want to cut bill-of-materials cost and power. Who loses? The incumbent suppliers of discrete parts, though they are large, entrenched and well-capitalised.

Chip rounds are priced as a bet on a long, capital-hungry sequence: first silicon, a commercial part, then design wins that take years to convert into volume. Seed money in semiconductors is mostly buying the right to be taken seriously at the next, much larger round.

### [Ubitium](https://www.ubitium.com) — $14M seed (led by Ibex Investors)
- **Problem:** Robots, drones and vehicles need separate chips for sensing, AI inference and real-time control, and moving data between them adds cost, power draw and software complexity.
- **Product:** A reconfigurable RISC-V processor that runs all three workloads on one array with unified memory and standard RISC-V tools. The first chip, the UB108, has 256 processing elements and is built on Samsung's 8nm process; the commercial UB410 with 4,096 elements is planned to tape out in 2027.
- **Customer:** Hardware and platform teams at makers of drones, robots and industrial machines, starting with high-resolution radar and audio systems, who are frustrated by multi-chip designs and want a single software stack.
- **Stage:** $14M seed from Düsseldorf, bringing total seed funding to $18M. OpenOcean joined, existing investors KBC Focus Fund, Runa Capital and Inflection returned, and Quantum Systems co-founder Florian Seibel invested personally. Founded in 2024 by CEO Hyun Shin Cho and CTO Martin Vorbach. First silicon has run all three workloads on one array; no customers are named and no revenue is disclosed ([announcement coverage](https://tech.eu/2026/10/13/ubitium-lands-14m-to-bring-universal-computing-to-physical-ai/)).
- **TAM:** Not stated. Analyst estimates for edge-AI processors run from about $6.7B (Global Industry Analysts) to $19.9B (Lucintel) by 2030, and far higher if broader edge-AI hardware is counted; the spread reflects different definitions, not different views of growth.
- **Moat:** Architecture IP and silicon-proven know-how are real but only matter if customers adopt the software model. The underwriting question is whether any machine maker will bet a product on a first-generation architecture from a startup before volume parts exist.

## A banker's incentive problem is back as a seed-stage pitch

Consumer banks earn more fee and interest income from customers who handle money badly: overdraft charges, credit and foreign-exchange spreads. Challenger banks spent a decade learning that growth without a distinct economic model just produces an app with a card. The modern pitch inverts the incentive: charge a flat subscription, hand fee income back, and build an advisor that nudges behavior in the customer's favor.

Why now: language models make a personalized money advisor cheap to run, and a decade of failed neobank unit economics has taught investors to ask where revenue comes from. The hurdle has not moved. A bank is a licence, a compliance programme and a capital structure first and an interface second, and the first customers are the expensive ones to acquire.

### [Matters](https://matters.inc) — $5M pre-seed (led by Swedish angel Jakob Johansson)
- **Problem:** Conventional banks profit when customers manage money badly, according to the company, and a large share of young adults say they don't know where their money goes.
- **Product:** A neobank for a flat monthly subscription with an AI Advisor aimed at spending decisions and saving goals. Interchange and foreign-exchange fees would flow back to users as cashback. The first consumer product is due "in the coming weeks."
- **Customer:** Younger consumers in the Nordics and then the EU who are financially stressed and distrust fee-driven banking.
- **Stage:** $5M pre-seed, emerging from stealth in Stockholm, with angels including former Klarna COO Knut Frängsmyr and Voi co-founder Douglas Stark. CEO Per Österström previously built consumer-loan broker Sambla Group, sold to Nordic Capital in early 2021; chair Lars-Åke Norling is the former Nordnet CEO. The team is 14 people; no product, customers or licence is yet disclosed ([announcement coverage](https://tech.eu/2026/10/15/matters-emerges-from-stealth-with-5m-in-pre-seed-funding-to-build-ai-native-consumer-bank)).
- **TAM:** No reliable estimate found. Published neobank forecasts differ by an order of magnitude depending on whether they count revenue or transaction value, so any single number would mislead.
- **Moat:** Today it is the team's credibility and distribution know-how, not a defensible asset. The underwriting question is whether a subscription-plus-cashback model covers the cost of a licence, fraud losses and customer acquisition, without the fee income it gives away.

## What to watch next week

- Whether a code-generation platform announces bundled testing, which would test the independence argument above.
- Whether Matters wins its licence path and ships the first product on schedule.
- Whether more chip startups get seed-sized rounds for physical AI, or Ubitium stays the exception.
