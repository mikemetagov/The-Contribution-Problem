"""Compute aggregated, publishable metrics per DAO-quarter from snapshot_fetch.py output.
Usage: python3 onchain_metrics.py ../_working/onchain_raw/*.json --out ../data/onchain/metrics.csv
Metrics: proposals, median unique voters, median Gini of VP, median Nakamoto coefficient (50% of VP cast),
median top-10 VP share, voter retention to next quarter. Descriptive only.
"""
import argparse, csv, json, statistics, datetime
from collections import defaultdict

def gini(x):
    x = sorted(v for v in x if v > 0); n = len(x)
    if n == 0: return None
    cum = sum((i + 1) * v for i, v in enumerate(x))
    return (2 * cum) / (n * sum(x)) - (n + 1) / n

def nakamoto(x, thr=0.5):
    x = sorted((v for v in x if v > 0), reverse=True); tot = sum(x); run = 0
    for i, v in enumerate(x, 1):
        run += v
        if run > thr * tot: return i
    return None

def top_share(x, k=10):
    x = sorted(x, reverse=True); tot = sum(x)
    return sum(x[:k]) / tot if tot else None

def q(ts):
    d = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc); return f"{d.year}Q{(d.month-1)//3+1}"

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="+"); ap.add_argument("--out", default="../data/onchain/metrics.csv")
    a = ap.parse_args(); rows = []
    for fn in a.files:
        d = json.load(open(fn)); byq = defaultdict(list); voters_q = defaultdict(set)
        for p in d["proposals"]:
            vps = [r["vp"] for r in p["vote_rows"]]
            if not vps: continue
            k = q(p["created"]); byq[k].append((len(vps), gini(vps), nakamoto(vps), top_share(vps), p["votes_truncated"]))
            voters_q[k].update(r["voter"] for r in p["vote_rows"])
        qs = sorted(byq)
        for i, k in enumerate(qs):
            m = byq[k]; med = lambda j: statistics.median([r[j] for r in m if r[j] is not None])
            ret = (len(voters_q[k] & voters_q[qs[i+1]]) / len(voters_q[k])) if i + 1 < len(qs) and voters_q[k] else None
            rows.append({"space": d["space"], "quarter": k, "proposals": len(m), "median_unique_voters": med(0),
                         "median_gini_vp": round(med(1), 4), "median_nakamoto_50": med(2), "median_top10_share": round(med(3), 4),
                         "voter_retention_next_q": round(ret, 4) if ret is not None else "", "any_truncated": any(r[4] for r in m)})
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(len(rows), "DAO-quarter rows ->", a.out)

if __name__ == "__main__": main()
