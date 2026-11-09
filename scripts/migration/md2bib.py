#!/usr/bin/env python3
"""Convert Tianyi Zhou's markdown publication lists into an al-folio papers.bib."""
import re, sys, json, unicodedata
from collections import OrderedDict

PUB_MD = sys.argv[1]
RES_MD = sys.argv[2]
OUT = sys.argv[3]

SELECTED_PATTERNS = [
    "HallusionBench", "BLIP3-o", "Program-of-Layers", "Schoenfeld", "WALL-E 2.0|WALL-E: World",
    "Your Mixture-of-Experts LLM Is Secretly", "Superfiltering", "InstructZero", "FedProto",
    "Robust Curriculum Learning", "Curriculum-guided Hindsight", "DiSAN", "Divide-and-Conquer Learning by Anchoring",
    "GoDec", "Item Difficulty Modeling Using Fine-tuned",
]
SELECTED_PATTERNS = [p.replace("WALL-E 2.0|WALL-E: World", "WALL-E: World Alignment by NeuroSymbolic") for p in SELECTED_PATTERNS]
SELECTED_PATTERNS = [p for p in SELECTED_PATTERNS if p != "Schoenfeld"] + ["Schoenfeld's Anatomy"]
EXTRA_AWARDS = {"Item Difficulty Modeling Using Fine-tuned": ("eAA Best Research", "2026 Best Research Award, International e-Assessment Association (eAA)"),
                "Schoenfeld's Anatomy": ("Oral · SAC Highlight", "Oral; SAC Highlight Award")}
EXTRA_ABBR = {"Educational and Psychological Measurement": "EPM"}

LINK_MAP = {  # markdown label -> bib field
    "pdf": "pdf", "code": "code", "dataset": "website", "data": "website", "model": "website",
    "demo": "website", "demo videos": "video", "slides": "slides", "poster": "poster",
    "appendix": "supp", "talk": "video", "supp": "supp", "video": "video",
}

def strip_md(s):
    s = re.sub(r"<span[^>]*>", "", s); s = s.replace("</span>", "")
    s = s.replace("\\*", "*")
    return s.strip()

def norm_title(t):
    t = unicodedata.normalize("NFKD", t).lower()
    return re.sub(r"[^a-z0-9]+", "", t)

def join_continuations(text):
    out = []
    for line in text.splitlines():
        if re.match(r"^\s*(1\.|\*|-)\s", line) or re.match(r"^\s*#", line) or not line.strip() or line.lstrip().startswith("<!--") or line.lstrip().startswith("{%") or line.lstrip().startswith("---"):
            out.append(line)
        elif out and re.match(r"^\s*1\.\s", out[-1]):
            out[-1] = out[-1].rstrip() + " " + line.strip()
        else:
            out.append(line)
    return "\n".join(out)

ENTRY_RE = re.compile(r'^\s*1\.\s+(?P<pre>.*?)"\*\*\*(?P<title>.+?)\*\*\*"\s*,?\s*(?P<post>.*)$')

def parse_authors(pre):
    pre = strip_md(pre).rstrip(", ").strip()
    pre = pre.replace(" and ", ", ").replace(", and ", ", ")
    # known broken entry
    pre = pre.replace("Dang Nguyen Tianyi Zhou", "Dang Nguyen, Tianyi Zhou")
    names = [n.strip() for n in re.split(r",\s*", pre) if n.strip()]
    bib = []
    for n in names:
        n = re.sub(r"\s+", " ", n)
        star = ""
        m = re.match(r"^(.*?)([\*†‡]+)$", n)
        if m:
            n, star = m.group(1).strip(), m.group(2)
        parts = n.split(" ")
        if len(parts) == 1:
            bib.append(n + star)
        else:
            bib.append(f"{parts[-1]}{star}, {' '.join(parts[:-1])}")
    return " and ".join(bib), any(("*" in b) for b in bib)

def parse_post(post):
    """post: 'VENUE..., YEAR. (award) [PDF](url), [CODE](url)'"""
    links = OrderedDict()
    for label, url in re.findall(r"\[([^\]]+)\]\(([^)\s]+)\)", post):
        key = LINK_MAP.get(label.strip().lower())
        if key and key not in links:
            links[key] = url
    body = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", "", post)
    body = body.replace(",,", ",")
    award = None
    m = re.search(r"\(\s*<span[^>]*>\s*\*?(.*?)\*?\s*</span>\s*\)", body)
    if m:
        award = m.group(1).strip(" *")
        body = body[:m.start()] + body[m.end():]
    # inline markers like <span style="color:red">*Oral*</span> inside venue
    m2 = re.search(r"<span[^>]*>\s*\*?([^<]*?)\*?\s*</span>", body)
    if m2:
        if not award: award = m2.group(1).strip(" *")
        body = body[:m2.start()] + body[m2.end():]
    body = strip_md(body)
    body = re.sub(r"\(\s*\)", "", body)
    yms = list(re.finditer(r"\b(20[0-2]\d|19\d\d)\b", body))
    ym = yms[-1] if yms else None
    year = ym.group(1) if ym else ""
    venue = body
    if ym:
        venue = body[:ym.start()].rstrip(" ,.")
    venue = re.sub(r",?\s*pp\.\s*(\d+-\d+)?,?", lambda m: (", pp. "+m.group(1)) if m.group(1) else "", venue)
    venue = re.sub(r"\s+", " ", venue).strip(" ,.")
    return venue, year, award, links

def classify(venue):
    """Return (abbr, type, cleaned venue, note)."""
    note = None
    v = venue
    if re.search(r"arxiv", v, re.I):
        m = re.search(r"arxiv:\s*([\d.]+)", v, re.I)
        return "arXiv", "preprint", (m.group(1) if m else None), note
    ms = re.findall(r"\(([A-Z][A-Za-z0-9/\- ]*?)\)", v)
    abbr = ms[-1] if ms else None
    if re.search(r"findings", v, re.I):
        note = "Findings"
    if re.search(r"datasets and benchmarks", v, re.I):
        note = "Datasets & Benchmarks Track"
    if re.search(r"workshop", v, re.I):
        note = (note + "; " if note else "") + "Workshop"
    typ = "journal" if re.search(r"transactions|journal|IEEE T|Measurement|TPAMI|T-PAMI|Machine Learning \(Springer\)|Psychological", v, re.I) and not re.search(r"conference|proceedings", v, re.I) else "conference"
    if abbr is None:
        if re.search(r"TMLR|Transactions on Machine Learning", v): abbr = "TMLR"
        elif re.search(r"Pattern Analysis", v): abbr = "TPAMI"
        elif re.search(r"Lecture notes", v, re.I): abbr = "Notes"; typ = "misc"
        else: abbr = ""
    abbr = {"T-PAMI": "TPAMI", "T-IP": "TIP", "T-NNLS": "TNNLS", "T-KDE": "TKDE", "ECML/PKDD": "ECML-PKDD", "AIME-Con": "AIME", "NAACL Findings": "NAACL"}.get(abbr, abbr)
    if abbr == "Springer":
        abbr = "WWWJ" if "Web" in v else "MLJ" if "Machine Learning" in v else "DMKD" if "Data Mining" in v else "Springer"
    # clean venue: remove the oral/findings markers already captured & location strings
    v = re.sub(r"\s*(Oral|Spotlight)\s*", " ", v).strip(" ,")
    v = re.sub(r"\s+", " ", v)
    if typ == "conference" and abbr and ms:
        i = v.find("(" + ms[-1] + ")")
        if i > 0: v = v[: i + len(ms[-1]) + 2]
    v = v.replace("Twentyth", "Twentieth")
    return abbr, typ, v, note

def mk_key(bibauthors, year, title, used):
    first = bibauthors.split(" and ")[0].split(",")[0]
    first = re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", first).lower())
    word = next((w for w in re.findall(r"[A-Za-z]+", title) if w.lower() not in {"a", "an", "the", "on", "of", "to", "in", "for", "and", "what", "how", "when", "is", "are", "does", "do"}), "paper")
    key = f"{first}{year}{word.lower()}"
    k, i = key, 2
    while k in used:
        k = f"{key}{i}"; i += 1
    used.add(k)
    return k

def parse_file(path, with_topics=False):
    text = join_continuations(open(path, encoding="utf-8").read())
    # drop html comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    entries = []
    section = topic = None
    for line in text.splitlines():
        h = re.match(r"^(#{2,3})\s+(.*)$", line)
        if h:
            if len(h.group(1)) == 2: section, topic = h.group(2).strip(), None
            else: topic = h.group(2).strip()
            continue
        m = ENTRY_RE.match(line)
        if not m:
            if re.match(r"^\s*1\.\s", line):
                print("UNPARSED:", line[:120], file=sys.stderr)
            continue
        title = strip_md(m.group("title")).replace("\n", " ")
        title = re.sub(r"\s+", " ", title)
        authors, has_star = parse_authors(m.group("pre"))
        venue, year, award, links = parse_post(m.group("post"))
        entries.append(dict(title=title, authors=authors, star=has_star, venue=venue, year=year,
                            award=award, links=links, section=section, topic=topic))
    return entries

pubs = parse_file(PUB_MD)
res = parse_file(RES_MD, with_topics=True)

# topic lookup from research.md -> slug keywords
def slug(t):
    t = re.sub(r"\(.*?\)", "", t).lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t
TOPIC_SLUGS = OrderedDict()
topics = {}
for e in res:
    sec = e["section"]; sub = e["topic"]
    sl = slug(sec).replace("large-language-models","llm").replace("multimodal-llm","mllm") + ("__" + slug(sub) if sub else "")
    TOPIC_SLUGS[sl] = (sec, sub)
    topics.setdefault(norm_title(e["title"]), set()).add(sl)
json.dump(list(TOPIC_SLUGS.items()), open(OUT + ".topics.json", "w"), indent=1)

merged = OrderedDict()
seen_pdf = {}
def pdfkey(e):
    u = e["links"].get("pdf", "")
    m = re.search(r"(\d{4}\.\d{4,5})", u)
    return m.group(1) if m else (u or None)
for e in pubs:
    merged[norm_title(e["title"])] = e
    if pdfkey(e): seen_pdf[pdfkey(e)] = norm_title(e["title"])
added = 0
for e in res:
    k = norm_title(e["title"])
    if k in merged: continue
    pk = pdfkey(e)
    if pk and pk in seen_pdf:
        # same paper, different title spelling: keep existing, add topics under existing key
        topics.setdefault(seen_pdf[pk], set()).update(topics.get(k, set()))
        continue
    merged[k] = e; added += 1
    if pk: seen_pdf[pk] = k
print(f"publications.md: {len(pubs)}, research.md: {len(res)}, added from research: {added}, total: {len(merged)}", file=sys.stderr)

def bibesc(s):
    return s.replace("&", "\\&").replace("%", "\\%")

used = set()
out = ["---", "---", ""]
stats = {"selected": 0}
for k, e in merged.items():
    abbr, typ, venue, note = classify(e["venue"])
    if e["section"] and e["section"].lower().startswith("misc"):
        typ = "misc"
    key = mk_key(e["authors"], e["year"], e["title"], used)
    fields = OrderedDict()
    if abbr: fields["abbr"] = abbr
    fields["title"] = "{" + e["title"] + "}"
    fields["author"] = e["authors"] if e["authors"] else "Zhou, Tianyi"
    if typ == "preprint":
        fields["journal"] = "arXiv preprint" + (f" arXiv:{venue}" if venue else "")
        if venue: fields["arxiv"] = venue
        etype = "article"
    elif typ == "journal":
        fields["journal"] = venue; etype = "article"
    elif typ == "misc":
        fields["howpublished"] = venue; etype = "misc"
    else:
        fields["booktitle"] = venue; etype = "inproceedings"
    if note:
        fields["note"] = note
    fields["year"] = e["year"] or "2026"
    for fk, url in e["links"].items():
        fields[fk] = url
    # arxiv id from pdf link
    if "arxiv" not in fields and "pdf" in fields:
        m = re.search(r"arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})", fields["pdf"])
        if m: fields["arxiv"] = m.group(1)
    if e["award"]:
        aw = re.sub(r",\s*Most cited.*$", "", e["award"]).strip()
        m = re.match(r"^(Oral|Spotlight),\s*([\d.]+%)$", aw)
        if m:
            fields["award_name"] = m.group(1); fields["award"] = f"{m.group(1)} (top {m.group(2)})"
        elif aw.startswith("Most cited"):
            pass
        else:
            fields["award_name"] = aw.split(",")[0].replace(" Award", "").strip()
            fields["award"] = aw
    for pat, (an, a) in EXTRA_AWARDS.items():
        if pat.lower() in e["title"].lower():
            fields["award_name"], fields["award"] = an, a
    for pat, ab in EXTRA_ABBR.items():
        if pat.lower() in e["venue"].lower(): fields["abbr"] = ab; fields.move_to_end("abbr", last=False)
    if e["star"]:
        fields["annotation"] = "* Equal contribution"
    tp = topics.get(k)
    if tp:
        fields["keywords"] = " ".join(f"topic:{t};" for t in sorted(tp))
    if any(re.search(p, e["title"], re.I) for p in SELECTED_PATTERNS):
        fields["selected"] = "true"; stats["selected"] += 1
    fields["bibtex_show"] = "true"
    w = max(len(f) for f in fields)
    out.append(f"@{etype}{{{key},")
    for f, v in fields.items():
        v = v if v.startswith("{") else "{" + bibesc(v) + "}"
        out.append(f"  {f.ljust(w)} = {v},")
    out[-1] = out[-1].rstrip(",")
    out.append("}")
    out.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print(json.dumps(stats), file=sys.stderr)
