![header](../assets/header.png)

# The Week in Seed: The Biggest Checks Went to Factories, Not Models

### Robot software for defense wiring lines, truck-delivered data centers, cloud apps built to be rebuilt, a voice test for humans, and AI sold to accounting firms instead of against them

The week's biggest early-stage money went into making physical things faster. Most of the rest bet that AI agents will break things that someone then has to fix. None of the rounds below are Bay Area companies, and that is just how the deals fell.

## Industrial capacity is the scarce input, and seed rounds are now priced like it

The AI story has been about models for three years. The constraint has moved down the stack to things that have to be manufactured: the buildings that hold the compute, and the factories that build the hardware governments now want in volume. Neither scales like software. Both are limited by skilled labor, custom construction and supply chains that were thinned out over decades, and that is the problem investors are now paying to solve.

The new thing is check size. Rounds labelled "seed" are arriving at a scale that used to mean a Series B, for companies a few months old, because the bet is on a team that can industrialize a process. It is not on a product that has already found buyers. We wrote in September about the money going into AI's own supply chain. This week takes that further: the product is the factory method itself, whether that means teaching existing robot arms new assembly tasks or building data centers on a production line instead of on site.

The winners, if this works, are buyers who need capacity faster than a construction or hiring cycle can supply it: defense manufacturers short of skilled assemblers, and labs and clouds short of powered sites. The losers are bespoke integrators and general contractors whose margin depends on every job being different. The risk is equally plain. Hardware and factory businesses burn capital before they prove unit economics, and a big seed valuation leaves very little room for a slipped production date.

### [Nidus](https://nidus.tech) — $30M pre-seed and seed (seed led by Kleiner Perkins; pre-seed led by Costanoa)
- **Problem:** Defense manufacturers can't hire enough skilled workers for fiddly, hand-done assembly steps, and a reliance on overseas supply chains makes that shortage a national-security problem.
- **Product:** AI models that let industrial robot arms customers already own do precision assembly. Teleoperation rigs collect training data and Nidus fine-tunes existing foundation robotics models on it. The first task is wire-harness preparation, with kitting, pre-assembly and circuit-board work next. Each customer's training data stays with that customer.
- **Customer:** US defense manufacturers and their suppliers with labor-bound assembly lines, where adding output today means hiring scarce technicians.
- **Stage:** $30M across a pre-seed and a seed; the split between them was not disclosed. Ludlow Ventures, SF1, Absolute Partners and Tau also participated, plus angels including Hadrian founder Chris Power. Founded in March 2026 by four engineers from Vannevar's hardware team, with about a dozen staff. The company says it passed seven figures in revenue (Upstarts reports "bookings") with unnamed defense customers in its first four months. No customer is named ([announcement](https://www.upstartsmedia.com/p/nidus-ai-robotics-raises-30m)).
- **TAM:** All-sector wire-harness forecasts run from roughly $150B to $164B by 2030. That is the value of the harnesses themselves, though, not of automating their assembly, which no published estimate I found sizes. Treat the big number as a ceiling, not a market.
- **Moat:** The pitch is proprietary task data gathered inside cleared defense plants, which generalist robotics labs can't easily collect. That holds only if Nidus gets in faster and deeper than better-funded rivals, which Upstarts names as Physical Intelligence, Skild AI and Figure. The underwriting question is whether early revenue is repeatable product or custom integration work.

### [Mavria](https://mavria.com) — $130M across pre-seed and seed at a $1B valuation (latest round led by Paradigm)
- **Problem:** Data center construction lags AI demand because every site is a custom build, and large blocks of grid power are scarce.
- **Product:** Terrain, a factory-built data center platform. Bisnow describes each unit as 5 MW, truck-delivered, and shipped with power distribution, liquid cooling, controls and server racks built in. Units can be clustered into a larger facility or placed singly where small pockets of grid capacity exist. Mavria plans to sell units and also develop and operate its own sites.
- **Customer:** Frontier AI labs, cloud providers and data center developers who need compute online on a predictable schedule, especially at power-constrained sites a full campus can't use.
- **Stage:** $130M raised to date, with AMP PBC, Liquid 2, Critical Frontier and Dream Ventures also in the latest round. Founded this summer by three people who met at the US Department of Energy; about 35 staff and a factory in Houston. The company says Terrain 01 is in production, while Bisnow reports that testing is planned for 2027 with the production ramp later that year. No customers are named ([announcement](https://mavria.com/introducing)).
- **TAM:** Analyst estimates for modular data centers range from about $73B to $88B by 2030. JLL's narrower figure for modular and micro data centers is about $48B. All are estimates built on different definitions.
- **Moat:** Manufacturing know-how and secured supply chains are real advantages if Mavria builds them before Vertiv, Schneider Electric and Eaton, which already sell modular power and cooling, close the gap. A $1B valuation before a tested unit is a bet on execution. The question to ask is how many megawatts it delivers in 2027, and at what cost per megawatt compared with stick-built sites.

## The agent era's insurance policy: prove who's human, and be able to rewind

We have covered trust as a product category before, mostly as security for the agents themselves. This week's rounds approach it from the other side. They assume agents and bots are already acting inside production systems and at the front door, and they sell the two things that matter after something goes wrong: knowing whether a human was really there, and getting a working system back.

The timing comes from a basic change. Bots now account for more than half of web traffic, by a Cloudflare figure the vendors cite. Agents also change cloud infrastructure around the clock, so last month's recovery plan describes a system that no longer exists. CAPTCHAs and document checks were built to catch crude scripts and cheap fraud. Backup tools were built for data, not for the tangle of configuration and permissions that makes a modern application run. Both are now being outrun.

This is an old, budgeted category with new founders, not a new market. Data protection and fraud prevention already have incumbents with large revenue. The startups' edge has to be that agents broke the old assumption, and the risk is that an incumbent can add the feature without having to sell a new platform.

### [Dreeze](https://www.dreeze.com) — $33M seed (co-led by Norwest and Bessemer Venture Partners)
- **Problem:** After an outage, a cyberattack or a bad agent action, restoring cloud *data* doesn't restore the *application*. Infrastructure, configuration, keys and dependencies have to be rebuilt in the right order, and recovery plans go stale as people and agents change things.
- **Product:** "Application Revival." It maps an application's resources and dependencies automatically, keeps them in an immutable air-gapped vault, rebuilds them in dependency order, and runs the full recovery plan as an automated end-to-end test, producing evidence that can be audited.
- **Customer:** Enterprises running critical applications on AWS (Azure later), especially regulated firms that have to prove recoverability to auditors and customers under their SLAs.
- **Stage:** Seed, announced on exit from stealth, with Claltech also participating. AWS version generally available; Azure in early access, with general availability planned for early 2027. About 70 staff in Israel and the US. The founders previously built Kashya (bought by EMC) and Zerto (bought by HPE). No customers named ([announcement](https://www.blocksandfiles.com/data-protection/2026/11/10/startup-dreeze-revives-complete-cloud-apps-not-just-their-data/5308847)).
- **TAM:** Disaster-recovery-as-a-service forecasts range from roughly $27B to $75B by 2030, depending on scope. Bessemer cites a Gartner projection that application-level recovery adoption rises from under 5% of organizations in 2026 to 35% by 2030. All of these are estimates.
- **Moat:** The founders have built and sold this kind of company twice, and that track record with enterprise buyers is the strongest asset here. The product, though, sits next to everything large backup vendors already sell. The question is whether "revival" stays a standalone purchase or becomes a checkbox in a backup suite, and the founders' history suggests they know how both of those endings work out.

### [Helix](https://helix.id/) — $6.2M pre-seed (led by Chicago Ventures)
- **Problem:** Bots and AI-generated fakes defeat CAPTCHAs and document checks, while age-verification rules push platforms toward collecting ID scans that users dislike and that create stores of sensitive data.
- **Product:** A voice-based human-verification SDK. The user reads four numbers aloud, and the check runs on the device without storing biometric data or personal information on Helix's servers. One SDK covers bot management, biometric multi-factor authentication and age assurance. The company says the method is patented and holds ISO/IEC 27566-1, Age Check Certification Scheme and IEEE age-verification certifications.
- **Customer:** Consumer platforms where bots or under-age users cost money or create regulatory exposure: ticketing, dating, gaming, gambling and fintech.
- **Stage:** Pre-seed; BAM Ventures, Aglaé Ventures, Corazon Capital, Tusk Ventures and others also participated. Live in beta with first partners, with in-home wellness platform Zeel named as a launch partner. No usage or revenue figures disclosed. Former Ticketmaster president Jared Smith sits on the board ([announcement](https://www.prnewswire.com/news-releases/helix-secures-6-2-million-in-pre-seed-capital-and-launches-voice-based-human-verification-for-the-ai-era-302936742.html)).
- **TAM:** Bot-management forecasts run from about $1.8B to $4.9B by 2030 depending on how the category is drawn. Adjacent identity and age-assurance spending widens that, but those are analyst estimates with inconsistent definitions.
- **Moat:** A ticketing pedigree is a credible route to the first big customer, since ticketing is where bot fraud costs the most. The hard question is durability: voice is exactly what generative models are getting better at faking. On-device liveness has to stay ahead of voice-cloning tools, and Helix has not published false-accept rates.

## The incumbents are buying the AI that was supposed to replace them

Last week's issue covered AI-native challengers in professional services that charge by the result to undercut firms that bill by the hour. This week's counterpoint: some of the larger seed money in the category is going to vendors who sell to the incumbents instead. The bet is that established accounting firms, short on staff and under fee pressure, will automate their own back office before an AI-native rival takes their clients.

That route has real advantages. Large firms already own the client relationships, the professional sign-off and the regulatory standing that a challenger has to build from scratch. A vendor that makes those firms faster can grow on their distribution instead of fighting it. The cost is that the vendor's upside is limited by how fast conservative partnerships change how they work, and by how much of the saving the firms keep for themselves rather than pass on.

Both models will probably coexist for a while. The signal to watch is whether incumbents that buy the tools start pricing like the challengers, by fixed fee, or keep billing hours and simply keep the margin.

### [Sumary](https://sumary.com/) — $25M seed (led by Singular)
- **Problem:** European accounting firms still do month-end closes, VAT returns and year-end preparation largely by hand while facing talent shortages and pressure to serve more clients without hiring.
- **Product:** An AI system for accounting firms that sits on top of clients' existing bookkeeping software, prepares the closing, VAT and year-end tasks, and routes them to accountants for review and approval. A Copenhagen research team built an accounting-task benchmark that Sumary uses to test model outputs before deploying them.
- **Customer:** Mid-sized to large accounting practices, starting in the Nordics and the UK, whose growth is limited by staff capacity during deadline periods.
- **Stage:** Seed, about a year after a $4.2M pre-seed, for roughly $29M raised in total. byFounders, Partech and Tenity followed on, with angels from Qonto, Linear and Synthesia. The company says it works with most of the Nordics' 20 largest accounting firms and has UK contracts with Deloitte, Grant Thornton and Baker Tilly. Reported savings of 50% on monthly closes and 75% on VAT returns are company figures. It is making London its commercial hub and expanding to Benelux next ([announcement](https://tech.eu/2026/11/10/sumary-secures-25m-to-expand-its-accounting-software-across-europe/)).
- **TAM:** Accounting-software forecasts for 2030 range from about $13B to $70B, with most clustering between $22B and $32B. Software sold *to* firms is a slice of that, not the whole.
- **Moat:** Named large-firm logos and a task benchmark are a decent start, and integration into firm workflows makes the product sticky once it is adopted. Large firms build in-house tools and run vendor bake-offs, though, and "most of the top 20" says nothing about contract size. The question is whether these are firm-wide deployments or departmental pilots.

## What to watch next week

- Whether Mavria names a first customer or a delivery date for a tested Terrain unit, which would settle the gap between "in production" and "testing in 2027."
- Whether Nidus says which defense manufacturers make up its early revenue, and whether it moves from wire harnesses to a second task.
- Whether Helix publishes false-accept rates against cloned voices; without them the core claim can't be checked.

*Header photo: "Bizerte. Besma works on the assembly" by U.S. Agency for International Development, CC0, via [Openverse](https://www.rawpixel.com/image/4051109/image-public-domain-person-woman).*
