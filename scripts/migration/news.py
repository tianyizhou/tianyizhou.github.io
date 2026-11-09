#!/usr/bin/env python3
import re, os, sys, shutil
src, outdir = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
items = re.findall(r"^\* (\d{4})/(\d{2}):\s*(.+?)\s*$", text, flags=re.M)
print(len(items), "news items", file=sys.stderr)
fixes = {
    "foundamental": "fundamental", "traning": "training", "vairous": "various", "acheived": "achieved",
    "Muiltimodal": "Multimodal", "has experienced": "have experienced", "We initialize": "We launched",
}
if os.path.isdir(outdir):
    for f in os.listdir(outdir): os.remove(os.path.join(outdir, f))
os.makedirs(outdir, exist_ok=True)
per_month = {}
for y, m, body in items:
    per_month.setdefault((y, m), []).append(body)
for (y, m), bodies in per_month.items():
    n = len(bodies)
    for i, body in enumerate(bodies):  # listed newest-first within a month
        day = 28 - i
        for a, b in fixes.items(): body = body.replace(a, b)
        body = body.replace('<span style="color:red">', '<span class="text-danger">')
        body = re.sub(r"\s+", " ", body).strip()
        if not body.endswith((".", "!", ")")): body += "."
        fn = f"{y}-{m}-{day:02d}-news.md"
        open(os.path.join(outdir, fn), "w", encoding="utf-8").write(
            f"---\nlayout: post\ndate: {y}-{m}-{day:02d}\ninline: true\nrelated_posts: false\n---\n\n{body}\n")
print("wrote", len(os.listdir(outdir)), file=sys.stderr)
