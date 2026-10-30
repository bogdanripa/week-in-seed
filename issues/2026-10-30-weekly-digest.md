![header](../assets/header.png)

# The Week in Seed: The Money Went to Software That Can Be Checked, Not Just Software That Can Do the Work

### An AI architect of record, an accounting platform, a code-proof company, an agent control plane and a genetics-first drug discovery startup

A week when the seed cheques went to AI that comes with its own audit trail, in trades where a signature carries liability.

## Licensed trades are being rebuilt around the signature, not the spreadsheet

The professions that sell a signed judgement, accounting and building design among them, have spent a decade adding software around the edges while the core product, an expert's time, stayed unchanged. That is why growth in these firms is still gated by headcount. The new generation of startups goes after the unit of work itself: the file review, the code check, the drawing set. The commercial logic is simple. If the output is a deliverable someone has to sign, the startup that can show its work wins the buyer, and the one that only produces fluent text does not.

This is a recurring theme in this newsletter, and the shape has changed. Earlier rounds were AI-native challengers competing with the licensed firm. This week's are selling to the firm, or becoming the firm of record, and betting that the incumbent tools were built for drafting, not for reasoning. The open question for investors is distribution: who owns the client relationship once the work is automated, and does the software vendor capture the saving or does the firm keep it?

### [Dream](https://www.dreamhq.com/) — $17M seed (led by Andreessen Horowitz)
- **Problem:** Commercial buildings take over a year of design and engineering before a contractor can build, and design tools such as AutoCAD and Revit assist a human rather than produce a buildable answer. The founders argue the U.S. builds less than it used to; TechCrunch cites a Richmond Fed brief for the decline in construction.
- **Product:** "Built world models" that generate layouts, structure and building systems such as HVAC and plumbing, checked against code, ending in a drawing set a general contractor can build from. Dream says it acts as architect of record, starting with offices, storefronts and data centers. It reports training on more than 100 million square feet of building data from U.S. permit archives.
- **Customer:** Developers and AEC (architecture, engineering, construction) teams that repeat a building type across many sites and feel the design bottleneck in their schedule.
- **Stage:** Seed, emerged from stealth, with SV Angel, XYZ and Zigg Capital also in; the company says it is deployed on 10 active projects in Texas and California; whether those are paid is not disclosed ([announcement](https://techcrunch.com/2026/10/29/ex-palantir-execs-launch-dream-with-17m-from-a16z-to-build-ai-world-models-for-construction/)).
- **TAM:** The coverage gives no figure. Analyst estimates of AEC software run about $10.7B to $14.2B for 2026 depending on definition (Grand View Research is the high end), and a design-as-a-service model could reach into fees beyond software.
- **Moat:** The permit-archive dataset is a real head start, but permit data is public and replicable. The harder asset is liability: being architect of record means carrying professional risk, and that is both the barrier to entry and the underwriting question.

### [Ravical](https://ravical.com/) — $17M seed (led by MMC Ventures)
- **Problem:** At an accounting firm each employee uses their own AI assistant their own way, so individuals get faster while the firm's judgement stays locked in senior heads. CEO Joris Van Der Gucht put it as: "the individual gets better, but the firm doesn't."
- **Product:** A platform for accounting and tax firms that captures how a firm's experienced staff assess cases and applies that approach across clients, connecting to CRM tools, financial software and internal databases to support file reviews and flag client risks and advisory opportunities.
- **Customer:** Mid-sized accounting and tax practices whose growth is capped by how many reviewers they can hire.
- **Stage:** Seed, $25M total raised, with existing investors Lakestar and Pitchdrive and new investor Shapers; reports cite more than 100 accounting firms as customers, mostly in Europe, and the company was founded in 2025 ([announcement](https://tech.eu/2026/10/29/ravical-raises-17m-to-break-the-link-between-accounting-firms-growth-and-hiring/)).
- **TAM:** Accounting software estimates for 2026 span roughly $8B to $23.5B (Fortune Business Insights at the low end, Mordor Intelligence at the high end); that excludes the larger pool of fee revenue the product is aimed at. Treat all as directional.
- **Moat:** Encoded firm know-how is sticky once embedded in review workflows. The test is whether the codified judgement belongs to Ravical or to each client firm, and whether a general-purpose assistant can copy the pattern.

## Trust is becoming a product category of its own

Two years of "deploy agents" have produced the obvious second-order problem: nobody can say what the agents did, or whether the code they wrote is right. Testing and security each had their moment in recent issues; the layer being funded now sits underneath both. One approach is to prove, mathematically, that code does what its specification says. The other is operational: put a control plane between the agent and everything it can touch, with identity, permissions, cost limits and a log.

These are different bets on the same buyer anxiety. Proof is rigorous but slow to adopt, and only as good as the specification someone writes. Governance is easy to deploy but is a feature the big platform vendors and identity incumbents will want to own. The most likely outcome is that both get pulled into the same procurement conversation as AI spend rises, and the winner is whoever is already inside the enterprise when the audit request arrives.

### [&Truth](https://andtruth.com) — $70M seed (lead not disclosed)
- **Problem:** AI writes code faster than anyone can review it, and testing only shows the presence of bugs, not their absence.
- **Product:** A verification platform aimed at mathematically proving code in any language is safe, secure and correct, with proofs others can check independently. It builds on the Lean proof system, includes automation for proofs and a "specification factory" for turning business requirements into formal specifications, and plans to open-source its foundational libraries.
- **Customer:** Teams shipping code where a failure is costly: infrastructure, security-critical and regulated software. Customers are not named.
- **Stage:** $70M seed from what the release calls "a group of formative AI safety and venture capital leaders", with no lead or individual investors named; no revenue or customer metrics disclosed. Founders are Stanford professor Clark Barrett, NUS researcher Ilya Sergey and Chris Hsu; the claim that proofs drop from months or years to hours or minutes is the company's own ([announcement](https://www.financialcontent.com/article/bizwire-2026-10-29-and-truth-emerges-from-stealth-pioneering-the-universal-verification-machine-for-code)).
- **TAM:** Not disclosed, and I did not find a credible market estimate for formal verification as a category.
- **Moat:** Scarce talent and a head start in making proofs cheap are the only assets visible today. The underwriting question is whether specifications, not proofs, are the real bottleneck, and whether a $70M seed with no named lead and no customers can find product-market fit before the claim is tested.

### [Mintive](https://www.mintive.com/) — $7M seed (led by Cowboy Ventures)
- **Problem:** Companies are letting agents reach internal tools and models without a clear picture of who can do what, or what it costs.
- **Product:** An agent management platform: an MCP gateway controlling what agents can access and do, an LLM gateway that routes across models and caps cost, agent identity and authorization, an agent monitor, and support for long-running proactive agents.
- **Customer:** Enterprise platform and security teams rolling out agents across many teams that need role-based control and logging.
- **Stage:** Seed, $11M raised in total, with Coatue, Operator Collective and Hustle Fund plus angels including Okta co-founder Frederic Kerrest, Jeff Dean and Andrej Karpathy; more than 50 enterprise customers since a February product launch, including Ro, Modern Treasury, the University of Michigan and Coursera ([announcement](https://techcrunch.com/2026/10/29/agent-identity-startup-mintive-lands-cowboy-ventures-coatue-angels-jeff-dean-andrej-karpathy/)).
- **TAM:** Highly definition-dependent. Meticulous Research sizes the broad agent-governance category (management, gateways, identity, observability) at about $1.0B to $1.5B for 2026; Astute Analytica's agent-identity-only estimate implies well under $1B. SailPoint's $90B figure covers all identity, not this.
- **Moat:** Being in the request path creates switching costs, but gateways are a thin layer that cloud and identity vendors can bundle. The founders' TensorFlow and Coursera pedigree helps with trust; durable differentiation is not yet clear.

## Drug discovery's seed bet is on generating the data, not tuning the model

The weakness in AI for drug discovery has long been inputs: models trained on thin or noisy biological data produce plausible candidates that fail in the lab. The seed response is to treat data generation as the product, running experiments at a scale and structure that produce the training set no public database has. That moves the capital intensity from compute to wet labs, and it changes the underwriting from "is the model good" to "is the dataset proprietary and does it point to a drug target worth chasing".

### [ALLOX](https://www.allox.bio/) — $10.5M seed (led by Asabys)
- **Problem:** Many disease-relevant proteins, such as those acting through protein-protein interactions and transcription factors, are hard to drug with small molecules.
- **Product:** A platform combining high-throughput genetics, experimental biology and AI to measure the effects of thousands of genetic mutations in parallel and map regulatory sites on proteins, aimed at finding allosteric sites for small-molecule drugs.
- **Customer:** Pharma and biotech partners; the company says it plans to build its internal team and partner with them. CEO and co-founder Júlia Domingo is named in the release.
- **Stage:** Seed through the Sabadell Asabys II fund, with CDTI (via SICC Innvierte) and the Institut Català de Finances; no pipeline, revenue or partner metrics disclosed ([announcement](https://tech.eu/2026/10/29/allox-closes-105m-seed-financing-to-scale-drug-discovery-platform/)).
- **TAM:** Published estimates of AI drug discovery for 2026 range from about $4B (Global Market Insights) to $8.6B (Roots Analysis), with one outlier near $24.5B (Towards Healthcare); small molecules are the largest segment in most reports. The real prize is pharma milestone and royalty economics, which these estimates don't capture.
- **Moat:** Proprietary experimental data would be the asset, but nothing disclosed shows it yet. The question is whether the platform reaches an actual partnered program before the seed runs out.

## What to watch next week

- Whether Dream names paying projects, or a licensed-professional partner, which would show how its architect-of-record model works in practice.
- Whether &Truth discloses a lead investor or a first customer, given the size of the seed against what has been shown.
- Whether another agent-governance startup raises at seed, which would confirm this is a category rather than a single deal.
