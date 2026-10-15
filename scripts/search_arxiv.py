"""Run an arXiv API query and write records to CSV. Usage: python3 search_arxiv.py "QUERY" out.csv [--max 500]"""
import sys, csv, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
NS = {"a": "http://www.w3.org/2005/Atom"}
q, out = sys.argv[1], sys.argv[2]; mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 500
rows, start = [], 0
while start < mx:
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "start": start, "max_results": 100})
    root = ET.fromstring(urllib.request.urlopen(url, timeout=60).read()); entries = root.findall("a:entry", NS)
    if not entries: break
    for e in entries:
        rows.append({"source": "arXiv", "id": e.find("a:id", NS).text, "title": " ".join(e.find("a:title", NS).text.split()),
                     "year": e.find("a:published", NS).text[:4], "abstract": " ".join(e.find("a:summary", NS).text.split())})
    start += 100; time.sleep(3)
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["source", "id", "title", "year", "abstract"]); w.writeheader(); w.writerows(rows)
print(len(rows), "records")
