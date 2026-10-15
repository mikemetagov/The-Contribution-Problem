# Codebook v0.1 (pilot version — to be frozen as v1.0 at Gate 2)

General rules
- Code only what the source states or directly reports; mark inference with `claim_type = inferred`.
- Every substantive code needs `excerpt` (≤50 words, verbatim) and `locator` (page, section, post number, or timestamp).
- Use `NR` (not reported) rather than guessing. Use `B99`/`S99` with a label for inductive codes; log candidates for amendment.
- One row per source in Modules A–D; one row per intervention in Module E; one row per CMO configuration in Module F.

## Module A — Source metadata and tier
| Variable | Values |
|---|---|
| A1 source_id | Unique ID from screening |
| A2 citation | Author, year, title, outlet |
| A3 url / archive_url | URLs |
| A4 tier | T1 peer-reviewed; T2 preprint/working paper; T3 institutional grey; T4 informal practitioner; T5 audio/video transcript (lower quality) |
| A5 evidence_type | empirical-quantitative; empirical-qualitative; mixed; case description; programme report; conceptual/opinion |
| A6 dao_types | protocol; grants/public-goods; investment; social; service; multiple; general |
| A7 daos_named | List |
| A8 period_covered | Years of data or events |
| A9 author_role | academic; foundation/DAO staff; delegate/contributor; vendor; journalist; other |
| A10 conflict_of_interest | none stated; possible (author affiliated with intervention/DAO); declared |
| A11 appraisal | MMAT score (T1–T2 empirical) or AACODS rating (T3–T5): high / moderate / low |

## Module B — Problem definition (RQ1a)
| Variable | Values |
|---|---|
| B1 defines_problem | explicit definition / implicit description / not addressed |
| B2 definition_text | Excerpt |
| B3 dimensions | Multi-select D1 decision-rights misalignment; D2 recognition & measurement; D3 compensation & incentives; D4 participation & retention; D5 contributor/delegate accountability |
| B4 terms_used | Labels the source uses (e.g., plutocracy, voter apathy, contributor gap) |

## Module C — Significance and maturity links (RQ1b)
One entry per claimed link (repeatable).
| Variable | Values |
|---|---|
| C1 dimension | D1–D5 |
| C2 outcome | M1 continuity; M2 participation breadth/retention; M3 decision-rights distribution; M4 contributor retention/capacity; M5 financial sustainability; M6 institutional capacity |
| C3 direction | negative effect on maturity; positive; mixed; none found |
| C4 claim_basis | measured association; causal design; case observation; practitioner judgement; theoretical |
| C5 claim_type | reported / inferred |
| C6 magnitude | Quantity if reported (e.g., "top 10% hold 76% of VP") |
| C7 persistence | persists after intervention / resolved / NR |

## Module D — Co-occurring barriers (RQ1c)
Repeatable per barrier.
| Variable | Values |
|---|---|
| D1 barrier | B1 identity/Sybil; B2 contribution-measurement validity; B3 token concentration; B4 delegation centralisation; B5 vote-buying/attacks; B6 security–decentralisation trade-off; B7 legal/regulatory form; B8 token-price/treasury volatility; B9 information overload/coordination cost; B10 AI agents as participants; B99 other |
| D2 linked_dimension | D1–D5 |
| D3 linkage_type | cause; consequence; precondition; co-symptom; co-mention only |
| D4 basis | as C4 |

## Module E — Intervention case (RQ2) — one row per intervention
| Variable | Values |
|---|---|
| E1 intervention_id / name | e.g., Arbitrum DIP v1.5 |
| E2 dao | Name; DAO type |
| E3 solution_family | S1 non-transferable reputation/citizenship; S2 proof-of-personhood + QV/1p1v; S3 delegate compensation/accountability; S4 retroactive/metrics-based rewards; S5 peer allocation; S6 role-based/structural; S7 AI-assisted measurement/agents; S99 other |
| E4 dimensions_targeted | D1–D5 |
| E5 status | active; ended; paused; replaced |
| E6 dates | start–end |
| E7 TIDieR-lite (0/1 each, sum 0–7) | what; who delivered; mechanism; dose/amount; duration; outcomes measured; comparison/baseline |
| E8 outcomes_reported | Free text + M-codes |
| E9 result_direction | improved; no change; worsened; mixed; not evaluated |
| E10 nesta_level | 0 none; 1 account of impact; 2 data shows change, no causality; 3 comparison/control group; 4 independent evaluation explaining how/why at reasonable cost; 5 replicated elsewhere by others, viable at scale |
| E11 evaluator_independence | self-reported; foundation/DAO-commissioned; independent |
| E12 unintended_effects | Free text (e.g., incumbent entrenchment, box-ticking) |
| E13 sources | source_ids supporting this case |

## Module F — CMO configurations (RQ3)
| Variable | Values |
|---|---|
| F1 cmo_id | Unique |
| F2 solution_family | S1–S7, S99 |
| F3 context | Conditions (DAO type, size, token distribution, legal form, identity infrastructure, treasury) |
| F4 mechanism_resource | What the intervention provides |
| F5 mechanism_response | How participants respond (reasoning/behaviour) |
| F6 outcome | Intended/unintended outcome; M-codes |
| F7 evidence_basis | as C4 + nesta_level if applicable |
| F8 programme_theory_link | IPT ID; supports / refines / refutes |

## Module G — Success criteria and benchmarks (RQ4; added by amendment A1)
Repeatable per criterion or benchmark.
| Variable | Values |
|---|---|
| G1 criterion_text | Excerpt stating a success criterion, target, KPI or benchmark |
| G2 dimension | D1–D5 |
| G3 indicator | Indicator name (e.g., Nakamoto coefficient, delegate rationale rate, contributor tenure) |
| G4 metric_role | primary KPI; guardrail; both |
| G5 value_reported | Threshold or observed value, with units |
| G6 comparator_type | public company; cooperative; DAO; normative (proposed by author); other |
| G7 time_horizon | Period over which success is assessed |
| G8 post_incentive_tested | yes; no; NR |
| G9 data_access | public (on-chain/forum); non-public (survey, internal) |
| G10 tradeoff_noted | Free text describing any trade-off the source reports |
