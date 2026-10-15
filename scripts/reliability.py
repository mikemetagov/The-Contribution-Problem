"""Inter-coder reliability: Cohen's kappa, Gwet's AC1 (nominal), quadratic-weighted kappa (ordinal).
Input CSV columns: item_id, variable, coder_a, coder_b. Usage: python3 reliability.py pairs.csv [--ordinal var1,var2]
"""
import argparse, csv
from collections import Counter, defaultdict

def cohen(a, b):
    n = len(a); cats = set(a) | set(b); po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b); pe = sum(ca[c] * cb[c] for c in cats) / n**2
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

def ac1(a, b):
    n = len(a); cats = sorted(set(a) | set(b)); q = len(cats); po = sum(x == y for x, y in zip(a, b)) / n
    if q < 2: return 1.0
    pi = {c: (a.count(c) + b.count(c)) / (2 * n) for c in cats}
    pe = sum(p * (1 - p) for p in pi.values()) / (q - 1)
    return (po - pe) / (1 - pe)

def wkappa(a, b):
    a = [float(x) for x in a]; b = [float(x) for x in b]; cats = sorted(set(a) | set(b)); k = len(cats)
    if k < 2: return 1.0
    idx = {c: i for i, c in enumerate(cats)}; n = len(a)
    w = lambda i, j: ((i - j) ** 2) / ((k - 1) ** 2)
    obs = sum(w(idx[x], idx[y]) for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    exp = sum(ca[x] * cb[y] * w(idx[x], idx[y]) for x in cats for y in cats) / n**2
    return 1 - obs / exp if exp else 1.0

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pairs"); ap.add_argument("--ordinal", default="")
    a = ap.parse_args(); ordv = set(filter(None, a.ordinal.split(","))); data = defaultdict(lambda: ([], []))
    for r in csv.DictReader(open(a.pairs)):
        data[r["variable"]][0].append(r["coder_a"]); data[r["variable"]][1].append(r["coder_b"])
    print("variable,n,statistic,value,meets_0.70")
    for v, (x, y) in data.items():
        stats = [("weighted_kappa", wkappa(x, y))] if v in ordv else [("cohen_kappa", cohen(x, y)), ("gwet_ac1", ac1(x, y))]
        for s, val in stats: print(f"{v},{len(x)},{s},{val:.3f},{val >= 0.70}")

if __name__ == "__main__": main()
