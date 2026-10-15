# The Contribution Problem: Current Landscape and Path Forward

This repository holds the full design protocol, codebook, sampling, analysis and outputs from the Metagov study "The Contribution Problem: Current Landscape and Path Forward": a public research repository for a mixed-methods evidence review (scoping review, realist synthesis, and descriptive on-chain demonstration) on the contribution problem in DAO governance.

**PI:** Michael Cooper, Research Director, Metagov
**Status:** Protocol v1.0 approved at Gate 1 (15 Oct 2026); Phase 1 (search, screening, codebook pilot) in progress
**Outputs:** SSRN working paper; Substack practitioner post; practitioner toolkit

## Research questions
1. What is the contribution problem in DAO governance, how significant is it to sustainable DAO maturity, and which other barriers co-occur with it?
2. What experiments have been attempted, and how rigorous was their testing relative to the problem's significance?
3. What solutions are emerging, and how should they be tested to justify modifying and scaling them within and across DAOs?
4. How will DAOs know the contribution problem is being managed, and how should they test and scale solutions to get there?

## Repository map
| Folder | Contents |
|---|---|
| `protocol/` | Protocol, amendment log |
| `search/` | Search strings, source registry, search log |
| `screening/` | Eligibility criteria, screening log, PRISMA-ScR flow |
| `codebooks/` | Codebook (human-readable and CSV), versioned |
| `coding/` | Coding templates, frozen coder prompts, final coding (after Gate 3) |
| `reliability/` | Reliability plan, statistics, human audit log |
| `scripts/` | Search, on-chain, and reliability scripts (Python 3, standard library only) |
| `data/` | On-chain extracts and final coded datasets |
| `synthesis/` | Synthesis plan and joint displays |
| `toolkit/` | Practitioner toolkit for DAO-run experiments (after Gate 4) |
| `outputs/` | Final SSRN paper and Substack post (after Gate 4) |
| `docs/` | AI-use disclosure, ethics and data handling |

## Versioning
Each gate approval is tagged (`gate-1`, `gate-2`, ...). Changes after a gate are recorded in `protocol/AMENDMENTS.md`. Working files not intended for publication stay outside this repository (see `.gitignore`).

## Licence
Text and data: CC BY 4.0 (`LICENSE-CC-BY-4.0.md`). Code in `scripts/`: MIT (`LICENSE-MIT`).
