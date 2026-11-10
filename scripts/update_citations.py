#!/usr/bin/env python3
"""Refresh the `citations` field of every entry in _bibliography/papers.bib that has an arXiv id,
using the Semantic Scholar Graph API (free, no key needed). Counts are only ever increased, so a
Google Scholar figure entered by hand is never lowered by the (usually smaller) S2 number.
Run: python3 scripts/update_citations.py  — exits 0 and prints the number of changed entries."""
import json, re, sys, time, urllib.request

BIB = "_bibliography/papers.bib"
text = open(BIB, encoding="utf-8").read()
ids = sorted(set(re.findall(r"^\s*arxiv\s*=\s*\{(\d{4}\.\d{4,5})\}", text, flags=re.M)))
counts = {}
for i in range(0, len(ids), 400):
    batch = ids[i:i + 400]
    req = urllib.request.Request(
        "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,externalIds",
        data=json.dumps({"ids": [f"ArXiv:{a}" for a in batch]}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "tianyizhou.github.io citation refresh"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
            break
        except Exception as e:  # rate limit / transient
            print("retry", attempt, e, file=sys.stderr); time.sleep(10 * (attempt + 1))
    else:
        sys.exit("Semantic Scholar unreachable; leaving papers.bib unchanged")
    for a, p in zip(batch, data):
        if p and p.get("citationCount") is not None:
            counts[a] = int(p["citationCount"])

changed = 0
def fix_entry(m):
    global changed
    body = m.group(0)
    am = re.search(r"^\s*arxiv\s*=\s*\{(\d{4}\.\d{4,5})\}", body, flags=re.M)
    if not am or am.group(1) not in counts: return body
    new = counts[am.group(1)]
    cm = re.search(r"^(\s*citations\s*=\s*\{)(\d+)(\},?)$", body, flags=re.M)
    if cm:
        if new > int(cm.group(2)):
            body = body[:cm.start(2)] + str(new) + body[cm.end(2):]; changed += 1
    elif new >= 10:  # add the field after the year line
        body = re.sub(r"(^\s*year\s*=\s*\{\d+\},?\n)", lambda y: y.group(1) + f"  citations   = {{{new}}},\n", body, count=1, flags=re.M); changed += 1
    return body
text2 = re.sub(r"@\w+\{[^@]*?\n\}\n", fix_entry, text, flags=re.S)
if changed:
    open(BIB, "w", encoding="utf-8").write(text2)
print(f"{len(counts)} papers looked up, {changed} entries updated")
