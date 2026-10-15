# Research Protocol: The Contribution Problem: Current Landscape and Path Forward

**Working title:** The Contribution Problem: Current Landscape and Path Forward
**Principal investigator:** Michael Cooper, Research Director, Metagov
**Protocol version:** 1.0 (locked at Gate 1, 15 October 2026; includes amendment A1)
**Date:** 15 October 2026
**Status:** Approved at Gate 1. Phase 1 released. Not pre-registered (by design decision); this public repository and its commit history serve as the protocol record.

**Purpose.** The study's end product is practical guidance that DAOs can use to run their own experiments on the contribution problem. The guidance has four parts:
- possible solutions;
- well-specified test-design parameters;
- clear success measures;
- a staged path from pilot to scale, so that trust in a solution builds alongside the evidence.

**Execution model:** LLM-executed research with human approval at four milestone gates.

---

## 1. Rationale

Most DAOs give decision rights in proportion to token holdings, while the work that keeps a DAO functioning (building, reviewing, analysing, moderating, overseeing) is done by a different and often smaller set of people. Existing empirical studies document high voting-power concentration and low participation. For example, one study of 216 DAOs found that the top 10% of voters hold 76% of voting power and average turnout is 6.3% ([Harvard Business School Working Knowledge](https://www.library.hbs.edu/working-knowledge/blockchains-promise-to-democratize-investor-power-faces-first-real-tests)). Another found that contributors held a working majority in only 7.5% of 872 DAOs ([Sharma et al., arXiv](https://arxiv.org/pdf/2309.14232)). Experiments meant to reward or empower contributors have produced mixed results. Delegate incentive programmes raised activity without dispersing power ([Cardano Forum review](https://forum.cardano.org/t/lessons-in-decentralized-governance-what-cardano-can-learn-from-dao-incentive-models/154264)). Optimism paused Retro Funding for at least 12 months in 2026 ([Optimism Governance Forum](https://gov.optimism.io/t/guide-to-season-9/10529)).

What is missing is a structured account of three things:

- how significant the contribution problem is for DAOs' long-term maturity;
- how rigorously the attempted solutions have been tested, relative to that significance;
- what level of evidence should be required before a solution is modified, scaled within a DAO, or transferred to other DAOs.

This protocol sets out a review designed to answer those questions.

## 2. Research questions and operational sub-questions

| RQ | Question | Operational sub-questions | Primary method |
|---|---|---|---|
| RQ1 | What is the contribution problem in DAO governance, and how significant is it to the sustainable maturity of DAOs? What other issues co-occur with this barrier? | 1a. How is the problem defined and described across sources, and which dimensions recur?<br>1b. What evidence links it to DAO maturity outcomes (Section 4.2), and how strong is that evidence?<br>1c. Which other barriers (identity, measurement, compensation, concentration, legal form, and so on) co-occur with it or are proposed as causes or consequences? | Scoping review (Section 5), with a descriptive on-chain demonstration (Section 9) |
| RQ2 | What experiments have been attempted to solve these problems, and how rigorous was the testing relative to the problem's significance? | 2a. Inventory of deliberate interventions with documented implementation.<br>2b. Rigour of each intervention's evaluation (Nesta level), plus implementation reporting quality.<br>2c. Alignment between problem significance (RQ1) and the evidence level of interventions addressing each dimension. | Scoping review plus experiment case coding |
| RQ3 | What solutions are emerging, and how should they be tested to build the evidence needed to modify and scale them within and across DAOs? | 3a. Emerging solution families and their programme theories: what works, for whom, in what contexts, and why.<br>3b. An evidence ladder linking evidence levels to decisions (modify, scale within, transfer across, adopt as standard).<br>3c. Design parameters for every solution family, plus two fully worked, ready-to-run test designs. | Realist synthesis (Section 8), plus evaluation design |
| RQ4 | How will DAOs know the contribution problem is being managed, and how should they test and scale solutions to get there? | 4a. What "managed" looks like for each dimension D1–D5 (Section 4.5).<br>4b. KPIs and reference ranges, benchmarked against public companies, cooperatives and best-performing DAOs.<br>4c. Paired metrics (guardrails), with a rationale for each pairing.<br>4d. Stage-gate criteria from pilot to transfer, including post-funding persistence tests.<br>4e. Lean and full versions of each design, for DAOs with different capacity. | Synthesis of RQ1–RQ3 with Module G, benchmark compilation, and the on-chain module (Section 8.4) |

**Terminology note.** In RQ1c, "correlated" means two barriers co-occur in coded sources or are proposed as linked through a causal pathway. It does not mean statistical correlation. The on-chain module (Section 9) reports descriptive associations only. No causal or inferential claims will be drawn from it.

## 3. Design overview

The study uses a sequential mixed-methods design with four components:

1. **Scoping review**, following JBI scoping review methodology and reporting to PRISMA-ScR ([Tricco et al., 2018](https://doi.org/10.7326/M18-0850)). This maps definitions, significance evidence, co-occurring barriers and experiments (RQ1, RQ2).
2. **Experiment case coding.** Up to 25 interventions are coded in depth for implementation detail and evaluation rigour, using the Nesta Standards of Evidence ([Nesta](https://www.nesta.org.uk/report/nesta-standards-of-evidence/)) and a short form of the TIDieR checklist ([Hoffmann et al., 2014](https://doi.org/10.1136/bmj.g1687)). This answers RQ2b and RQ2c.
3. **Realist synthesis** of emerging solutions, reported to RAMESES standards ([Wong et al., 2013](https://doi.org/10.1186/1741-7015-11-21)). It uses context–mechanism–outcome (CMO) configurations to build the evidence ladder and test designs (RQ3).
4. **Descriptive on-chain demonstration** using public Snapshot voting data for about 10 DAOs where the problem is documented as significant. It is for illustration only and is not a test of significance (RQ1). It also supplies baseline values for the RQ4 KPIs and the top-quartile DAO benchmark.
5. **Resolution framework and practitioner toolkit (RQ4).** This sets out what "managed" means, the KPIs and reference ranges, paired metrics, stage-gate criteria and tiered test templates that DAOs can use for their own experiments.

Results are brought together in joint displays (Section 10). Confidence in review findings is rated with an adapted version of GRADE-CERQual ([Lewin et al., 2018](https://doi.org/10.1186/s13012-017-0688-3)).

No single framework is used as the analytical lens. Concepts come from the evidence and from the working definition below. Ostrom's design principles are not a framing device for this study.

## 4. Key definitions

### 4.1 Working definition of the contribution problem

> The contribution problem is the misalignment between who creates value for a DAO (through work, expertise, oversight and stewardship) and who holds recognised standing, rewards and decision rights. It includes the difficulty of observing, valuing and sustaining those contributions over time.

**Core dimensions (D-codes):**

| Code | Dimension | Description |
|---|---|---|
| D1 | Decision-rights misalignment | Voting or proposal power follows token holdings or delegation, not contribution. |
| D2 | Recognition and measurement | Contributions are hard to observe, attribute or value, especially non-code and "invisible" work. |
| D3 | Compensation and incentives | Pay and reward schemes for contributors and delegates are inadequate, misaligned or open to gaming. |
| D4 | Participation and retention | Voter apathy, governance fatigue, information overload and contributor churn. |
| D5 | Contributor and delegate accountability | Weak mechanisms to evaluate, sanction or remove those who hold contribution-linked roles. |

The definition is provisional. It will be tested against how sources define the problem. Any revision is proposed at Gate 2 and locked at Gate 3.

### 4.2 Sustainable DAO maturity (outcome domains)

| Code | Outcome domain | Example indicators |
|---|---|---|
| M1 | Continuity | Governance remains active, without pauses, dissolution or reversion to company control. |
| M2 | Participation breadth and retention | Unique voters, repeat voting, and delegates' share of votes cast. |
| M3 | Distribution of decision rights | Gini coefficient, Nakamoto coefficient and top-10 share of voting power. |
| M4 | Contributor retention and capacity | Contributor tenure, churn, and the number of active workstreams. |
| M5 | Financial sustainability | Treasury runway and the ratio of spending to revenue. |
| M6 | Institutional capacity | Codified rules, dispute processes, layered bodies and oversight functions. |

### 4.3 Co-occurring barriers (B-codes)

| Code | Barrier |
|---|---|
| B1 | Identity and Sybil resistance (one person controlling many wallets) |
| B2 | Validity of contribution measurement |
| B3 | Token or voting-power concentration (plutocracy) |
| B4 | Centralisation of delegation |
| B5 | Vote-buying and governance attacks |
| B6 | Trade-off between security and decentralisation |
| B7 | Legal and regulatory form, including wrappers |
| B8 | Token price and treasury volatility |
| B9 | Information overload and coordination costs |
| B10 | AI agents as participants |
| B99 | Other, specified inductively |

### 4.4 Intervention ("experiment")

A deliberate, documented change to rules, incentives, roles or tooling, intended to address one or more D-dimensions, with evidence that it was implemented. Proposals that were never implemented go into the RQ3 "emerging" set, not the RQ2 inventory.

### 4.5 "Managed" as the target state

The study treats the contribution problem as something to be managed, not eliminated. Some tension between capital and contribution is built into token-governed organisations.

A DAO is considered to be managing the problem on a dimension when four conditions hold:
- its KPIs fall within the reference range for that dimension (Section 8.4);
- the paired guardrail metric has not worsened beyond its tolerance;
- the improvement has lasted at least two governance quarters;
- where incentives were paid, the improvement continues for at least one quarter after the incentives end.

## 5. Eligibility criteria

| Criterion | Include | Exclude |
|---|---|---|
| Population | DAOs and token- or on-chain-governed organisations of any type (protocol, grants or public goods, investment, social, service). Each is coded by type. | Corporate blockchain consortia without token governance, and purely theoretical voting-mechanism papers with no DAO application. |
| Concept | Addresses at least one D-dimension, or a B-barrier explicitly linked to contribution, recognition, rewards or decision rights. | General DAO governance with no link to contribution. Pure security exploits. |
| Context | Any jurisdiction or chain. | None |
| Period | January 2016 to the search date. | Before 2016 |
| Language | English | Other languages, recorded as excluded on language grounds. |
| Source type | Tiers T1 to T5 (Section 6.1). | X/Twitter threads (used only as pointers to other sources), Discord, Telegram, private channels and paywalled sources that can't be accessed. |

## 6. Evidence sources and search strategy

### 6.1 Source tiers

| Tier | Source type | Use in synthesis |
|---|---|---|
| T1 | Peer-reviewed journal articles and conference papers | Full weight, subject to appraisal |
| T2 | Preprints and working papers (arXiv, SSRN, university working papers) | Full weight, subject to appraisal, and flagged as not peer reviewed |
| T3 | Institutional grey literature: programme reports and evaluations, foundation and research-firm reports, official governance-forum programme documents, audits | Full weight, subject to appraisal |
| T4 | Informal practitioner sources: blogs, Substack, Mirror or Paragraph posts, opinion posts on governance forums | Lower weight. Can support a finding only alongside T1–T3, or when coded as practitioner perception. |
| T5 | Audio and video transcripts (podcasts, YouTube, conference talks) | Lowest-quality tier. Flagged in every table. Cannot support any finding alone; used for practitioner perception and to identify experiments. |
| Lead only | X/Twitter threads | Not coded as evidence. Followed only to locate T1–T5 sources. |

### 6.2 Search sources

**Academic**
- arXiv API, using the cs.CY, cs.CR, cs.GT, econ.GN and q-fin categories.
- Crossref API.
- SSRN and Google Scholar, reached through targeted web searches.
- OpenAlex and Semantic Scholar are not used. At Gate 1, the decision was to proceed without API keys; targeted web searches cover these indexes instead. This is recorded as a limitation.

**Governance forums** (public Discourse search):
- Arbitrum, Optimism, Uniswap, ENS, Compound, Aave, Gitcoin, Sky/Maker, Lido, Gnosis, Cardano Forum, Polkadot.
- The final list is set in `search/source-registry.csv`.

**Organisations and research groups:**
- Metagov, DAOstar, Gitcoin, the Optimism Foundation, the Arbitrum Foundation, Karma, Blockworks Research, Messari, a16z crypto research, Token Engineering Commons.
- Hats Protocol, Coordinape, SourceCred, Colony, Snapshot Labs and BanklessDAO.

**Informal:**
- Substack, Mirror and Paragraph, through web searches.
- Podcast and YouTube transcripts where publicly available (T5).

**Benchmarks (RQ4):**
- Public-company governance data, such as ownership concentration and shareholder voting turnout, from academic and proxy-advisory sources.
- Cooperative member-participation data, such as general-meeting turnout and member voting, from cooperative federations and the research literature.
- Search strings B01–B04 in `search/search-strings.csv`. These are capped at 30 screened items, and the benchmark sources are recorded in `synthesis/benchmarks.csv`.

**Snowballing:**
- Backward citation checks for every included T1–T2 source.
- Forward citation checks for the 10 most-cited included sources, where an index allows it.

### 6.3 Search strings

The search combines three concept blocks: (Population) AND (Concept) for RQ1, and (Population) AND (Intervention) for RQ2 and RQ3. The full strings for each database are in `search/search-strings.csv`. Every query is run as recorded and logged with its date and hit count in `search/search-log.csv`.

### 6.4 Search limits and stopping rules

- **Academic databases:** All hits are retrieved, then deduplicated by DOI, normalised title and URL.
- **Forums and grey literature:** Searching a given forum or site stops once two consecutive result pages add no new eligible items. There is a hard cap of 60 screened items per forum.
- **Informal sources (T4, T5):** These stop when theoretical saturation is reached, meaning no new D/B code or intervention appears in 10 consecutive eligible items. There is a hard cap of 80 screened items.
- **Overall cap:** No more than 400 records go to dual title and abstract screening, after a scripted, logged keyword pre-filter. If more than 400 remain, records are prioritised by tier (T1 > T2 > T3 > T4 > T5), then coverage of under-represented DAO types, then recency. The prioritisation rule is applied by script, and everything excluded by it is logged.

## 7. Screening, data extraction and appraisal

### 7.1 Screening

There are two stages: title and abstract screening, then full text. Each record is screened by two independent LLM coders (Coder A and Coder B). Each runs in a separate session that sees only the eligibility criteria and the record, not the other coder's decisions. Disagreements go to an adjudicator pass that records a written rationale. The full-text inclusion cap is about 120 sources. Flow is reported in a PRISMA-ScR diagram.

### 7.2 Codebook and extraction

The codebook (`codebooks/codebook.md`, machine-readable in `codebooks/codebook.csv`) has six modules:

- **A. Source metadata and tier**
- **B. Problem definition and dimensions (D1–D5)**
- **C. Significance and maturity links (M1–M6)**, including direction and strength of the claim
- **D. Co-occurring barriers (B1–B10)**, including the proposed linkage type
- **E. Intervention case** (TIDieR-lite and Nesta level), for RQ2 sources only
- **F. CMO configurations** for RQ3
- **G. Success criteria and benchmarks** for RQ4: success criteria, KPIs, thresholds, benchmark values, guardrails, time horizons and post-incentive persistence that sources state or report

Coders record a verbatim excerpt of no more than 50 words, plus a location, for every substantive code.

### 7.3 Quality appraisal

- **T1–T2 empirical studies** are appraised with the Mixed Methods Appraisal Tool (MMAT, [Hong et al., 2018](https://doi.org/10.3233/EFI-180221)).
- **T3–T5 sources** are appraised with the AACODS checklist for grey literature ([Tyndall, 2010](https://dspace.flinders.edu.au/xmlui/handle/2328/3326)).
- Appraisal results are reported for every source. They inform confidence ratings but are not used to exclude sources, as is standard in scoping reviews.

### 7.4 Evaluation rigour (RQ2b)

Each experiment case receives a Nesta Standards of Evidence level:

| Level | Meaning |
|---|---|
| 1 | Clear account of why the intervention should work |
| 2 | Data showing change, but causality not established |
| 3 | Causal evidence using a control or comparison group |
| 4 | Independent evaluation explaining why and how the impact occurs, at reasonable cost |
| 5 | Replicated by others in other settings, while staying viable |

Two further fields are added:

- **Level 0** for interventions with no evaluation at all.
- **An independence flag:** self-reported, foundation-commissioned, or independent.

Implementation reporting quality is scored 0–7 on TIDieR-lite. One point is given for each of: what was done; who delivered it; mechanism; dose or amount; duration; outcomes measured; and comparison or baseline.

### 7.5 Coding reliability

- **Pilot:** Before full coding, 12 deliberately contrasting sources are double-coded. They span tiers T1–T5, at least four DAO types, and both RQ1 and RQ2 content.
- **Statistics:**
  - Cohen's kappa ([Cohen, 1960](https://doi.org/10.1177/001316446002000104)) and Gwet's AC1 ([Gwet, 2008](https://doi.org/10.1348/000711006X126600)) for nominal codes. Gwet's AC1 is reported because it is robust when one code is very common or very rare.
  - Quadratic-weighted kappa for ordinal codes such as Nesta level and appraisal ratings.
- **Threshold:** At least 0.70 on both statistics for each module. If a module falls below the threshold, a versioned codebook amendment is proposed with its recoding cost, and the pilot is recoded (maximum two rounds).
- **Human audit:** Michael Cooper audits a stratified random sample of 10–15% of coded sources at Gates 2 and 3. Audit disagreements are logged in `reliability/audit-log.csv`. If more than 20% of audited items disagree on any module, that module is recoded.
- **Implementation:** The coder sessions are isolated: separate agent sessions share no context and use frozen prompts stored in `coding/prompts/`. Model identity and version are recorded for every coding pass.

## 8. Synthesis

### 8.1 RQ1: definition, significance and co-occurrence

1. **Definitions:** Definitions are compared through content analysis of Module B. The output is a frequency of D-dimensions by tier and DAO type, plus a revised definition.
2. **Significance:** The significance of each D-dimension is rated High, Moderate or Low on four criteria:
   - **Prevalence:** how many sources, DAO types and years it appears in.
   - **Severity:** the strength and direction of evidence linking it to the M-outcomes.
   - **Persistence:** whether it continues after interventions.
   - **Practitioner salience:** how often T3–T5 sources raise it.
3. **Confidence:** Each significance rating receives a CERQual-style confidence rating (High, Moderate, Low or Very Low). It is based on methodological limitations, coherence, adequacy and relevance.
4. **Co-occurrence:** A B-by-D co-occurrence matrix and network are built. Linkage types (cause, consequence, precondition, co-symptom) are coded separately from simple co-occurrence.

### 8.2 RQ2: rigour relative to significance

For each D-dimension, the significance rating is set against the highest, typical and independent-only Nesta level of the interventions that target it. The result is an alignment matrix. An evidence deficit is flagged where significance is High and the highest independent evaluation is at Level 2 or below.

### 8.3 RQ3: realist synthesis and evidence ladder

1. **Initial programme theories.** At Gate 3, initial theories are drafted for the candidate solution families:

   | Code | Solution family |
   |---|---|
   | S1 | Non-transferable reputation and citizenship |
   | S2 | Proof of personhood, with quadratic or one-person-one-vote |
   | S3 | Delegate pay and accountability |
   | S4 | Retroactive or metrics-based contribution rewards |
   | S5 | Peer allocation of rewards (Coordinape-style) |
   | S6 | Role-based and structural designs (councils, roles, optimistic governance, splitting entities) |
   | S7 | AI-assisted contribution measurement and AI delegates |

2. **CMO evidence.** CMO configurations from Module F are used to confirm, refine or refute each theory.
3. **Evidence ladder.** The ladder links evidence levels to decisions. Draft thresholds, to be locked at Gate 3:

   | Decision | Minimum evidence | Additional requirements |
   |---|---|---|
   | Modify within a DAO | Nesta Level 2 | Pre-specified metrics, a baseline, and harms monitoring |
   | Scale within a DAO | Nesta Level 3 | A comparison group or credible counterfactual (staggered rollout, regression discontinuity, synthetic control) |
   | Transfer across DAOs | Nesta Level 4 | Independent evaluation, replication in at least two DAO types, and documented contextual conditions from the CMO evidence |
   | Recommend as a default standard | Nesta Level 5 | Fidelity manual, multiple replications, cost data and sustainability evidence |

4. **Test designs.** Two test designs are selected at Gate 3 for solution families with high significance and low evidence. Candidates include:
   - a regression-discontinuity evaluation around the eligibility threshold of a voting-power-gated delegate programme (for example, Arbitrum's 200,000 ARB threshold, [Arbitrum community dashboard](https://arbitrum-community-dashboard.generalmagic.io/history));
   - a staggered (stepped-wedge) rollout of non-transferable contributor credentials in a grants or service DAO, analysed by difference-in-differences.

   Each design specifies its hypothesis, outcomes, data sources, sample and power considerations, threats to validity, harms monitoring and decision rules.

   In addition, every solution family S1–S7 gets a design-parameter sheet covering:
   - hypothesis;
   - primary KPI and paired guardrail;
   - minimum duration;
   - comparison options, from strongest to weakest: randomisation, staggered rollout, regression discontinuity, synthetic control, before-and-after with a baseline;
   - minimum sample considerations;
   - post-funding test;
   - harms to monitor.

### 8.4 RQ4: resolution framework

1. **What "managed" means.** For each dimension D1–D5, the framework states the managed state and one or two KPIs for it. KPIs are measured from public data where possible. Some KPIs need data DAOs collect themselves; these are marked as such.

2. **Reference ranges, not pass/fail targets.** For each KPI, the framework shows reference values from three comparators:
   - **Public companies:** for example, ownership concentration and shareholder voting turnout.
   - **Cooperatives:** for example, member participation in general meetings.
   - **Best-performing DAOs:** the top quartile of the on-chain sample (Section 9), plus DAOs that the evidence base reports as strong performers.

   DAOs set their own targets within these ranges. For each comparator, the framework explains why it is only partly comparable: different ownership rules, different legal obligations, and different costs of participating.

3. **Paired metrics (guardrails).** Every primary KPI is paired with a guardrail metric that would reveal a trade-off. Each pairing comes with a written explanation of why it is needed. Examples:

   | Primary KPI | Guardrail | Why the pairing is needed |
   |---|---|---|
   | Contributors' share of decision rights | Insider concentration | Shifting power to contributors can let a small insider group capture control. |
   | Delegate participation rate | Quality of vote rationales | Paying delegates can raise participation through box-ticking. |
   | Number of contributors rewarded | Spending per verified contribution | Wider rewards can inflate costs without more real work. |
   | Sybil resistance | Participation of eligible members | Identity checks can exclude legitimate members. |

   Pairings are added only where the evidence or a mechanism suggests a trade-off.

4. **Stage gates from pilot to scale.** Each stage runs for at least two governance quarters and has go/no-go criteria tied to the evidence ladder (Section 8.3):

   | Stage | Go criteria |
   |---|---|
   | Pilot | Feasibility and an initial signal on the KPI |
   | Modify | KPI moves in the expected direction against a baseline, with guardrails within tolerance |
   | Scale within the DAO | Comparison-based evidence |
   | Transfer to other DAOs | Independent or replicated evidence, plus the contextual conditions from the realist synthesis |

5. **Post-funding test.** Any solution that relies on paid incentives must show the KPI persists for at least one quarter after incentives end before it can move to the next stage.

6. **Two versions of each design.**
   - **Lean:** for DAOs without analysts. It uses public dashboards and Snapshot data, before-and-after comparisons with a baseline or staggered rollout, and a short list of KPIs.
   - **Full:** for well-resourced DAOs. It uses randomised or quasi-experimental designs, power calculations, independent evaluators and survey measures.

7. **Measures DAOs collect themselves.** This study uses public data only. The guidance will still recommend measures DAOs can collect in their own experiments, such as contributor surveys on recognition, fairness and intention to stay. Each recommendation includes guidance on consent, privacy and the ethics of randomising incentives among members.

8. **Status of the framework.** Reference ranges and thresholds are a proposed standard built from the evidence, not findings of the evidence. They are labelled that way in every output.

## 9. On-chain demonstration module (RQ1)

- **Purpose:** To illustrate the problem with current data. It is demonstrative only and is not a test of significance, since the problem is already well documented.
- **Sample:** About 10 DAOs, chosen purposively from DAOs that the included evidence identifies as having a significant contribution problem, and that have public Snapshot data. The final list is approved at Gate 2. Candidates include Arbitrum, Optimism, Uniswap, ENS, Aave, Gitcoin, Lido, Gnosis, Balancer and CoW DAO.
- **Data:** The public Snapshot GraphQL API (hub.snapshot.org). Its accessibility was verified on 15 October 2026. The window is the most recent 24 months of closed proposals.
- **Metrics:** For each DAO, by quarter:
  - proposals;
  - median unique voters;
  - Gini coefficient of voting power;
  - Nakamoto coefficient (the minimum number of voters needed to reach 50% of the voting power cast);
  - top-10 voters' share of voting power;
  - voter retention (the share of voters active in quarter t who vote again in quarter t+1);
  - where public lists exist, the share of voting power cast by known compensated delegates or contributor roles.
- **Limitations:** Votes held on-chain through Governor contracts are not covered unless the DAO also mirrors them to Snapshot. Address-level data says nothing about the people behind addresses. Descriptive statistics only.
- **Code:** `scripts/snapshot_fetch.py` and `scripts/onchain_metrics.py`. Outputs go to `data/onchain/`.

## 10. Integration and outputs

**Joint displays:**
1. A D-dimension by significance by confidence table.
2. A B-by-D co-occurrence matrix.
3. An alignment matrix of significance against evidence level.
4. A table of solution families by CMO, evidence level and ladder rung.
5. On-chain illustration panels.
6. A resolution scorecard for each dimension D1–D5, showing the managed state, KPIs, reference ranges by comparator, guardrails, and stage-gate criteria.

**Outputs:**
- **An SSRN working paper** of about 8,000–10,000 words. It includes a methods section with an AI-use statement, all joint displays, and links to this repository.
- **A Substack post** of about 2,000–2,500 words, written for practitioners. Every table is supplied as a generated image.
- **A practitioner toolkit** in `toolkit/`:
  - a solution menu;
  - design-parameter sheets for S1–S7;
  - two worked test designs;
  - a KPI and guardrail scorecard with reference ranges;
  - stage-gate checklists;
  - lean and full templates;
  - consent and ethics guidance for DAO experiments.
- **A public repository** containing the protocol, codebooks, search logs, screening decisions, final coding, reliability statistics, on-chain data and scripts.

## 11. Gates

| Gate | Work completed before review | Decision required | What approval locks | Next phase released |
|---|---|---|---|---|
| G1 | Protocol v0.1, codebook v0.1, search strings, source registry, scripts and repository structure | Approve protocol; choose API-key option, licences and working title | Protocol v1.0, eligibility criteria, source tiers, caps, gate plan | Phase 1: search, deduplication, screening, codebook pilot |
| G2 | Search log, PRISMA flow, included set, 12-source pilot with reliability statistics, proposed codebook amendments, DAO shortlist for the on-chain module, audit sample | Approve included set, codebook amendments and DAO list | Codebook v1.0, included corpus, on-chain sample | Phase 2: full coding, appraisal, experiment cases, on-chain analysis |
| G3 | Final coding with reliability results, audit results, significance ratings, co-occurrence and alignment matrices, initial programme theories and CMO evidence, draft ladder thresholds, two candidate test designs, design-parameter sheets, draft resolution framework (KPIs, reference ranges, guardrails, stage gates), list of corrections to starting premises | Approve synthesis logic, ladder thresholds, resolution framework and choice of test designs | Synthesis rules, ladder, resolution framework, test designs, list of major claims | Phase 3: drafting the SSRN paper, Substack post and toolkit |
| G4 | SSRN draft, Substack draft with table images, practitioner toolkit, repository release candidate | Approve for publication, or request revisions | Final text and public data release | Publication, carried out by the PI |

Work inside a released phase continues without interim approvals. Each gate packet includes a one-page decision memo with numbered options.

## 12. Resource constraint

The PI has set a ceiling of 1,000 Computer credits for the full study. The executing agent can't track credit use precisely. The protocol therefore relies on hard caps:

- 400 records screened;
- about 120 included sources;
- 25 experiment cases;
- 10 DAOs in the on-chain module;
- two codebook-pilot rounds at most.

It also relies on the saturation-based stopping rules in Section 6.4. At each gate, the agent reports the work completed and what remains, so the PI can check usage in their account before releasing the next phase. If usage is approaching the ceiling, the fallback order is:

1. Reduce T4–T5 coverage.
2. Reduce experiment cases to 15.
3. Reduce on-chain DAOs to 6.
4. Single-code T4–T5 sources, with a 20% double-coded check.

## 13. Ethics, data handling and transparency

- Only publicly accessible data is used. There are no private channels and no interaction with human participants.
- Pseudonymous individuals are reported only in aggregate. Named attribution is limited to authors of published works and holders of formal public governance roles acting in that role.
- Excerpts are limited to 50 words. Every source has a URL and, where possible, an archived snapshot.
- API terms and rate limits are respected.
- **AI-use disclosure:** All search, screening, coding and drafting are performed by large language model agents. Human oversight happens at four gates, with sample audits. See `docs/ai-use-disclosure.md`.
- **Amendments:** Any change after a gate is logged in `protocol/AMENDMENTS.md`, with its rationale and recoding consequences.

## 14. Limitations anticipated

- Publication and visibility bias towards large, well-documented DAOs, and towards successful or controversial programmes.
- Heavy reliance on grey and informal sources, given how early-stage the field is. Tiering and confidence ratings make this visible but can't fix it.
- LLM coding errors. These are mitigated by independent dual coding, reliability thresholds and human audits.
- The on-chain module is purposive and descriptive. It can't establish prevalence or causation.
- This study uses public data only. It can't observe contributors' own views of recognition and fairness, which are central to whether the problem is being managed. The guidance recommends that DAOs collect these measures in their own experiments.
- Public companies and cooperatives are only partly comparable to DAOs, so reference ranges are guidance, not standards.
- OpenAlex and Semantic Scholar are not searched directly (Gate 1 decision), which may reduce academic recall.
- English-language restriction.

## References (methods)

- Cohen, J. (1960). A coefficient of agreement for nominal scales. https://doi.org/10.1177/001316446002000104
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. https://doi.org/10.1348/000711006X126600
- Hoffmann, T. C., et al. (2014). Better reporting of interventions: TIDieR checklist and guide. https://doi.org/10.1136/bmj.g1687
- Hong, Q. N., et al. (2018). The Mixed Methods Appraisal Tool (MMAT) version 2018. https://doi.org/10.3233/EFI-180221
- Lewin, S., et al. (2018). Applying GRADE-CERQual to qualitative evidence synthesis findings. https://doi.org/10.1186/s13012-017-0688-3
- Puttick, R., and Ludlow, J. (2012). Standards of Evidence for Impact Investing. Nesta. https://www.nesta.org.uk/report/standards-of-evidence-for-impact-investing/
- Tricco, A. C., et al. (2018). PRISMA Extension for Scoping Reviews (PRISMA-ScR). https://doi.org/10.7326/M18-0850
- Tyndall, J. (2010). AACODS Checklist. Flinders University. https://dspace.flinders.edu.au/xmlui/handle/2328/3326
- Wong, G., et al. (2013). RAMESES publication standards: realist syntheses. https://doi.org/10.1186/1741-7015-11-21
