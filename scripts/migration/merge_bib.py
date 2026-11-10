#!/usr/bin/env python3
"""Build papers.bib from the uploaded pub2026.bib + preprints2026.bib, merging extra
fields (code/website/keywords/abbr/awards) from the previously generated bib."""
import re, sys, json, unicodedata, os
from collections import OrderedDict
import bibtexparser
from bibtexparser.model import Entry, Field

PUB, PRE, OLD, OUT = sys.argv[1:5]

def norm(t):
    t = unicodedata.normalize("NFKD", t).lower().replace("\\&", "&")
    return re.sub(r"[^a-z0-9]+", "", t)

def arxiv_id(*urls):
    for u in urls:
        if not u: continue
        m = re.search(r"arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})", u)
        if m: return m.group(1)
    return None

def g(e, k):
    return e[k] if k in e else ""

old = bibtexparser.parse_file(OLD)
old_by_title, old_by_arxiv = {}, {}
for e in old.entries:
    old_by_title[norm(g(e, "title"))] = e
    a = arxiv_id(g(e, "pdf"), g(e, "arxiv") and f"arxiv.org/abs/{g(e,'arxiv')}")
    if a: old_by_arxiv[a] = e

ABBR_MAP = {"T-PAMI": "TPAMI", "ECML/PKDD": "ECML-PKDD", "NAACL Findings": "NAACL", "SIGGRAPH Asia": "SIGGRAPH Asia"}
def classify(venue):
    ms = re.findall(r"\(([A-Z][A-Za-z0-9/\- ]*?)\)", venue)
    abbr = ms[-1] if ms else None
    if abbr: abbr = ABBR_MAP.get(abbr, abbr)
    if not abbr:
        for pat, ab in [("Transactions on Machine Learning Research", "TMLR"), ("Pattern Analysis", "TPAMI"), ("Image Processing", "TIP"),
                        ("Neural Networks and Learning", "TNNLS"), ("Knowledge and Data", "TKDE"), ("Educational and Psychological", "EPM"),
                        ("World Wide Web", "WWWJ"), ("Data Mining and Knowledge", "DMKD"), ("Machine Learning", "MLJ"), ("arXiv", "arXiv"),
                        ("Under review", "Preprint"), ("Position paper", "Preprint")]:
            if pat.lower() in venue.lower(): abbr = ab; break
    if abbr and re.search(r"findings", venue, re.I) and "Findings" not in abbr:
        abbr += " Findings"
    return abbr or ""

SELECTED = OrderedDict([  # title fragment -> preview image
    ("HallusionBench", "hallusionbench.png"), ("FedProto", "fedproto.png"), ("DiSAN", "disan.png"), ("GoDec", "godec.png"),
    ("Program-of-Layers", "polar.png"), ("WestWorld", "westworld.png"), ("Schoenfeld's Anatomy", "thinkarm.png"),
    ("BLIP3-o: A Family", "blip3o.png"), ("WALL-E: World Alignment by NeuroSymbolic", "walle.png"),
    ("Fast vs. Slow Thinking", "layergrad.png"), ("Secretly an Embedding", "moee.png"), ("Superfiltering", "superfiltering.png"),
    ("InstructZero", "instructzero.png"), ("Embodied Multi-Modal Agent", "emma.png"),
])
TOPIC_FIX = {  # title fragment -> topic slug(s), for papers missing from the old research page
    "Polysona": ["agents-and-world-models"], "Quantifying and Modeling Driving Style": ["agents-and-world-models"],
    "Confidence-Controlled Exploration": ["reinforcement-learning"], "Task-Driven Domain-Agnostic": ["agents-and-world-models"],
    "AutoDavis": ["mllm__benchmarks-and-evaluation"], "TrustGen": ["llm__benchmarks-and-evaluation", "llm__safety"],
    "GPFedRec": ["distributed-and-collaborative-learning"], "Federated Recommendation Meets Cold-Start": ["distributed-and-collaborative-learning"],
    "Multi-Center Federated Learning": ["distributed-and-collaborative-learning"],
    "Subclass-balancing Contrastive": ["data-augmentation-and-synthesis"], "Omni-Scale CNNs": ["natural-language-processing"],
    "Jumpout": ["optimization"], "Bias Also Matters": ["llm__generalization"], "Constrained Stochastic Gradient": ["optimization"],
    "Labelset Anchored": ["matrix-factorization-and-feature-disentanglement"], "NESVM": ["optimization"],
    "Backward-Forward Least Angle": ["compressed-sensing-sparse-dimension-reduction"], "Manifold elastic net": ["compressed-sensing-sparse-dimension-reduction"],
    "Minimizing Nearest Neighbor": ["compressed-sensing-sparse-dimension-reduction"], "Efficient Robust Conditional Random": ["natural-language-processing"],
    "Data Subset Selection with Imperfect": ["curriculum-learning-and-data-selection"],
    "Cognitive Episodes in LLM Reasoning": ["llm__post-training-and-reasoning"], "One Model for All": ["llm__human-ai-alignment-and-reward-hacking"],
    "Item Difficulty Modeling Using Fine-tuned": ["llm__benchmarks-and-evaluation"],
    "Time-Consistency Curriculum": ["curriculum-learning-and-data-selection"], "False Correlation Reduction": ["reinforcement-learning"],
    "Extracting Local Reasoning Chains": ["llm__generalization"],
    "Library Learning of Code Actions": ["agents-and-world-models"], "Doing More with Less": ["llm__generalization"],
    "Human Modeling Meets AI Metacognition": ["llm__human-ai-alignment-and-reward-hacking", "agents-and-world-models"],
}
EXTRA = {  # title fragment -> extra fields
    "HallusionBench": {"code": "https://github.com/tianyi-lab/HallusionBench", "citations": "1363"},
    "DiSAN": {"citations": "1011"},
    "GoDec": {"citations": "954", "award_name": "Most Influential Paper", "award": "IEEE TCSC Most Influential Paper Award (2020)"},
    "Schoenfeld's Anatomy": {"award_name": "Oral · SAC Highlight", "award": "Oral; ACL 2026 SAC Highlight Award", "code": "https://github.com/MingLiiii/ThinkARM"},
    "WestWorld": {"website": "https://westworldrobot.github.io/"},
    "Item Difficulty Modeling Using Fine-tuned": {"award_name": "eAA Best Research", "award": "2026 Best Research Award, International e-Assessment Association"},
    "Divide-and-Conquer Anchoring": {"award_name": "Best Student Paper", "award": "ICDM 2013 Best Student Paper Award"},
    "BLIP3-o: A Family": {"code": "https://github.com/JiuhaiChen/BLIP3o"},
}

def parse_note(note):
    """Return (award_name, award, annotation) from the uploaded note field."""
    if not note: return None, None, None
    n = note.replace("\\%", "%")
    m = re.match(r"^(Oral|Spotlight),\s*([\d.]+%)", n)
    if m: return m.group(1), f"{m.group(1)} (top {m.group(2)})", None
    if n.strip() == "Oral": return "Oral", "Oral", None
    if n.strip().lower() == "long presentation": return "Oral", "Long presentation (oral)", None
    if "contributed equally" in n: return None, None, n.strip()
    if "Best Student Paper" in n: return "Best Student Paper", "ICDM 2013 Best Student Paper Award", None
    if "Most Influential" in n: return "Most Influential Paper", "IEEE TCSC Most Influential Paper Award (2020)", None
    return None, None, None  # "980 citations" etc. are dropped (we keep the citations field)

def build(src_path, status):
    db = bibtexparser.parse_file(src_path)
    out = []
    for e in db.entries:
        f = OrderedDict()
        title = g(e, "title").strip()
        if title.startswith("{") and title.endswith("}"): title = title[1:-1]
        title = title.replace("\\&", "&").replace("FaSTA\\:", "FaSTA*:")
        venue = g(e, "booktitle") or g(e, "journal") or ""
        abbr = classify(venue) if status == "published" else ("Preprint" if "arXiv" not in venue else "arXiv")
        f["abbr"] = abbr
        f["title"] = title
        f["author"] = g(e, "author")
        if "booktitle" in e: f["booktitle"] = venue
        else: f["journal"] = venue
        for k in ("volume", "number", "pages", "publisher"):
            if k in e: f[k] = g(e, k)
        f["year"] = g(e, "year")
        url = g(e, "url")
        a = arxiv_id(url)
        if url:
            if a: f["arxiv"] = a
            f["pdf"] = url
        an, aw, annot = parse_note(g(e, "note"))
        if an: f["award_name"], f["award"] = an, aw
        if annot: f["annotation"] = annot
        if "citations" in e: f["citations"] = g(e, "citations")
        # merge from old bib
        o = old_by_arxiv.get(a) if a else None
        if o is None: o = old_by_title.get(norm(title))
        kws = set()
        if o is not None:
            for k in ("code", "website", "supp", "slides", "poster", "video"):
                if k in o and k not in f: f[k] = g(o, k)
            if "pdf" not in f and "pdf" in o: f["pdf"] = g(o, "pdf")
            if "award_name" not in f and "award_name" in o:
                f["award_name"], f["award"] = g(o, "award_name"), g(o, "award")
            kws.update(re.findall(r"topic:[a-z0-9_\-]+;", g(o, "keywords")))
        for frag, extra in EXTRA.items():
            if frag.lower() in title.lower():
                for k, v in extra.items(): f[k] = v
        # auto thumbnail from the paper's GitHub repo (assets/img/publication_preview/repo-<owner>__<repo>.png)
        if "code" in f and "github.com/" in f["code"]:
            m = re.search(r"github\.com/([^/]+)/([^/#?]+)", f["code"])
            if m:
                cand = f"repo-{m.group(1)}_{m.group(2).replace('.git','')}.png".lower()
                if os.path.exists(os.path.join(os.path.dirname(OUT), "..", "assets", "img", "publication_preview", cand)):
                    f["preview"] = cand
        for i, (frag, prev) in enumerate(SELECTED.items()):
            if frag.lower() in title.lower():
                f["selected"] = "true"; f["preview"] = prev
                kws.add("pick:highly-cited;" if i < 4 else "pick:recent;")
        for frag, sl in TOPIC_FIX.items():
            if frag.lower() in title.lower(): kws.update(f"topic:{x};" for x in sl)
        kws.add(f"status:{status};")
        kws.update(k.replace("topic:", f"{status}:") for k in list(kws) if k.startswith("topic:"))
        f["keywords"] = " ".join(sorted(kws))
        f["bibtex_show"] = "true"
        etype = e.entry_type
        out.append((e.key, etype, f))
    return out

entries = build(PUB, "published") + build(PRE, "preprint")
# de-duplicate keys
seen = {}
for i, (k, t, f) in enumerate(entries):
    kk = re.sub(r"[^A-Za-z0-9_\-]", "", k)
    while kk in seen: kk += "x"
    seen[kk] = 1; entries[i] = (kk, t, f)

def esc(v):
    return v.replace("&", "\\&") if "\\&" not in v else v

lines = ["---", "---", ""]
for k, t, f in entries:
    w = max(len(x) for x in f)
    lines.append(f"@{t}{{{k},")
    for fk, v in f.items():
        vv = "{" + title_wrap(v) + "}" if False else None
        if fk == "title": body = "{" + esc(v) + "}"   # double braces keep capitalisation
        elif fk in ("booktitle", "journal", "award", "annotation", "publisher"): body = esc(v)
        else: body = v
        lines.append(f"  {fk.ljust(w)} = {{{body}}},")
    lines[-1] = lines[-1].rstrip(",")
    lines.append("}"); lines.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(lines))
sel = [f["title"][:50] for _, _, f in entries if "selected" in f]
print(f"{len(entries)} entries; selected {len(sel)}:", *sel, sep="\n  ", file=sys.stderr)
print("published:", sum(1 for *_, f in entries if "status:published" in f["keywords"]),
      "preprint:", sum(1 for *_, f in entries if "status:preprint" in f["keywords"]),
      "with topics:", sum(1 for *_, f in entries if "topic:" in f["keywords"]), file=sys.stderr)
