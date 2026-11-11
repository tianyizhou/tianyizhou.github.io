#!/usr/bin/env python3
"""Refresh the Google Scholar totals (citations, h-index, i10-index) shown in the CV's
Publication Summary (_data/cv.yml). Google Scholar has no API, so this reads the public
profile page. If the page cannot be fetched or parsed (Scholar sometimes blocks cloud
runners), the file is left unchanged and the script exits 0.
Run: python3 scripts/update_scholar.py"""
import re, sys, time, urllib.request

USER = "OKvgizMAAAAJ"
CV = "_data/cv.yml"
URL = f"https://scholar.google.com/citations?user={USER}&hl=en"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

html = None
for attempt in range(4):
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", "replace")
        break
    except Exception as e:
        print("retry", attempt, e, file=sys.stderr)
        time.sleep(15 * (attempt + 1))
if not html:
    print("Google Scholar unreachable; cv.yml unchanged"); sys.exit(0)

# The stats table lists: citations (all, recent), h-index (all, recent), i10-index (all, recent)
vals = [int(v) for v in re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)]
if len(vals) < 6:
    print("Could not parse the Scholar stats table; cv.yml unchanged"); sys.exit(0)
cites, h, i10 = vals[0], vals[2], vals[4]

text = open(CV, encoding="utf-8").read()
pat = re.compile(r'(details: ")([\d,]+) total; h-index (\d+); i10-index (\d+)(")')
m = pat.search(text)
if not m:
    sys.exit("Citations line not found in _data/cv.yml")
old = int(m.group(2).replace(",", ""))
if cites < old * 0.9 or h < 1:  # sanity check against a bad page
    print(f"Suspicious values ({cites}, {h}, {i10}); cv.yml unchanged"); sys.exit(0)
new = pat.sub(lambda m: f'{m.group(1)}{cites:,} total; h-index {h}; i10-index {i10}{m.group(5)}', text, count=1)
if new != text:
    open(CV, "w", encoding="utf-8").write(new)
print(f"citations {cites:,}; h-index {h}; i10-index {i10}")
