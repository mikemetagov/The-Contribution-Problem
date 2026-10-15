# Scripts (Python 3, standard library only)
| Script | Purpose | Tested |
|---|---|---|
| `search_arxiv.py` | arXiv API query → CSV | API reachable 2026-10-15 |
| `search_crossref.py` | Crossref query (2016+) → CSV | API reachable 2026-10-15 |
| `search_discourse.py` | Public Discourse forum search → CSV | Smoke-tested on Arbitrum forum |
| `snapshot_fetch.py` | Snapshot proposals + votes → `_working/` (raw, unpublished) | Smoke-tested on ens.eth |
| `onchain_metrics.py` | Aggregated DAO-quarter metrics → `data/onchain/` | Smoke-tested |
| `reliability.py` | Cohen's kappa, Gwet's AC1, weighted kappa | Tested on toy data |
