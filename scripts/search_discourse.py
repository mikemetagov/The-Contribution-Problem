"""Search a public Discourse governance forum. Usage: python3 search_discourse.py https://forum.arbitrum.foundation "delegate incentive" out.csv [--pages 3]"""
import sys, csv, json, time, urllib.parse, urllib.request
base, term, out = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3]
pages = int(sys.argv[sys.argv.index("--pages") + 1]) if "--pages" in sys.argv else 3
rows, seen = [], set()
for page in range(1, pages + 1):
    url = f"{base}/search.json?" + urllib.parse.urlencode({"q": term, "page": page})
    req = urllib.request.Request(url, headers={"User-Agent": "metagov-research/0.1"})
    d = json.load(urllib.request.urlopen(req, timeout=60)); topics = {t["id"]: t for t in d.get("topics", [])}
    new = 0
    for p in d.get("posts", []):
        tid = p.get("topic_id")
        if tid in seen: continue
        seen.add(tid); new += 1; t = topics.get(tid, {})
        rows.append({"forum": base, "term": term, "topic_id": tid, "title": t.get("title", ""), "created": p.get("created_at"),
                     "url": f"{base}/t/{t.get('slug','')}/{tid}", "blurb": p.get("blurb", "")})
    if new == 0: break
    time.sleep(1)
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["forum", "term", "topic_id", "title", "created", "url", "blurb"]); w.writeheader(); w.writerows(rows)
print(len(rows), "topics")
