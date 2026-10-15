"""Fetch closed Snapshot proposals and votes for one DAO space (public GraphQL API).
Raw address-level output is written to _working/ (not published). Usage:
  python3 snapshot_fetch.py arbitrumfoundation.eth --months 24
"""
import argparse, json, os, time, urllib.request
API = "https://hub.snapshot.org/graphql"

def gql(query, variables):
    req = urllib.request.Request(API, json.dumps({"query": query, "variables": variables}).encode(),
                                 {"Content-Type": "application/json", "User-Agent": "metagov-research/0.1"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["data"]
        except Exception:
            time.sleep(2 ** attempt * 3)
    raise RuntimeError("Snapshot API failed")

P = """query($s:String!,$t:Int!,$skip:Int!){proposals(first:100,skip:$skip,orderBy:"created",orderDirection:desc,
where:{space:$s,state:"closed",created_gte:$t}){id title created end votes scores_total}}"""
V = """query($p:String!,$skip:Int!){votes(first:1000,skip:$skip,where:{proposal:$p}){voter vp created}}"""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("space"); ap.add_argument("--months", type=int, default=24)
    ap.add_argument("--max-proposals", type=int, default=400); ap.add_argument("--out", default="../_working/onchain_raw")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    since = int(time.time()) - a.months * 30 * 86400
    props, skip = [], 0
    while len(props) < a.max_proposals:
        batch = gql(P, {"s": a.space, "t": since, "skip": skip})["proposals"]
        if not batch: break
        props += batch; skip += 100
    for p in props[:a.max_proposals]:
        votes, skip = [], 0
        while True:
            b = gql(V, {"p": p["id"], "skip": skip})["votes"]
            votes += b
            if len(b) < 1000 or skip >= 5000: break  # Snapshot skip limit
            skip += 1000
        p["vote_rows"] = [{"voter": v["voter"], "vp": v["vp"]} for v in votes]
        p["votes_truncated"] = len(votes) < (p.get("votes") or 0)
    with open(os.path.join(a.out, f"{a.space}.json"), "w") as f:
        json.dump({"space": a.space, "fetched": int(time.time()), "proposals": props[:a.max_proposals]}, f)
    print(a.space, len(props[:a.max_proposals]), "proposals")

if __name__ == "__main__": main()
