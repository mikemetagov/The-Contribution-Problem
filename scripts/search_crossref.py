"""Run a Crossref bibliographic query (2016+) and write records to CSV. Usage: python3 search_crossref.py "QUERY" out.csv [--max 500]"""
import sys, csv, json, urllib.parse, urllib.request
q, out = sys.argv[1], sys.argv[2]; mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 500
rows, offset = [], 0
while offset < mx:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": q, "filter": "from-pub-date:2016-01-01",
          "rows": 100, "offset": offset, "select": "DOI,title,issued,type,container-title,abstract", "mailto": "research@metagov.org"})
    items = json.load(urllib.request.urlopen(url, timeout=60))["message"]["items"]
    if not items: break
    for it in items:
        rows.append({"source": "Crossref", "id": it.get("DOI"), "title": (it.get("title") or [""])[0],
                     "year": (it.get("issued", {}).get("date-parts") or [[None]])[0][0], "type": it.get("type"),
                     "venue": (it.get("container-title") or [""])[0], "abstract": it.get("abstract", "")})
    offset += 100
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["source", "id", "title", "year", "type", "venue", "abstract"]); w.writeheader(); w.writerows(rows)
print(len(rows), "records")
