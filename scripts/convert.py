"""Convert Firefox Help PDFs (printed from Firefox) to clean markdown."""
import glob, os, re, sys
from datetime import date
import pymupdf

NAV = re.compile(r"^(Customize this article|Search questions, articles|Ask a Question|Still need help|Continue$|Version \d+|Mac$|Windows$|Linux$|Firefox$|Table of Contents)")
STOP = re.compile(r"^(Share this article|These fine people|Volunteer$)")
LIGS = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl"}

def clean(s):
    for k, v in LIGS.items(): s = s.replace(k, v)
    s = re.sub(r"[ \t]{2,}", " ", s.replace("\xa0", " "))
    return re.sub(r"\s+([,.;:)])", r"\1", s)

def span_md(span, links):
    t = span["text"]
    if not t.strip(): return t
    x0, y0, x1, y1 = span["bbox"]; cx, cy = (x0+x1)/2, (y0+y1)/2
    uri = next((l["uri"] for l in links if l.get("uri") and l["uri"].rstrip("/") != "https://support.mozilla.org/en-US" and l["from"].contains(pymupdf.Point(cx, cy))), None)
    bold = "Bold" in span["font"] or "SemiBo" in span["font"]
    lead, core, trail = re.match(r"(\s*)(.*?)(\s*)$", t, re.S).groups()
    if bold: core = f"**{core}**"
    if uri: core = f"[{core}]({uri})"
    return lead + core + trail

def convert(pdf):
    doc = pymupdf.open(pdf)
    title = doc.metadata["title"].split(" | Firefox Help")[0].strip()
    footer_url = None
    items = []  # (kind, text, x0, ytop, ybot, size)
    for pn, page in enumerate(doc):
        links = page.get_links()
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                sp = [s for s in l["spans"] if s["text"].strip()]
                if not sp: continue
                if sp[0]["font"].startswith("Times"):
                    m = re.match(r"https://support\.mozilla\.org/\S+", sp[0]["text"])
                    if m and not footer_url: footer_url = clean(m.group(0))
                    continue
                plain = clean("".join(s["text"] for s in l["spans"])).strip()
                if NAV.match(plain) or plain.startswith("Last updated") or "users voted this helpful" in plain: continue
                if plain == title or plain in ("Settings",) : 
                    continue
                size = round(sp[0]["size"], 1)
                md = clean("".join(span_md(s, links) for s in l["spans"])).strip()
                items.append(dict(pn=pn, plain=plain, md=md, x=l["bbox"][0], y0=l["bbox"][1], y1=l["bbox"][3], size=size,
                                  head="Headline" in sp[0]["font"] and size >= 14))
    # stop at footer
    cut = next((i for i, it in enumerate(items) if STOP.match(it["plain"])), len(items))
    items = items[:cut]
    # drop leading category label etc: everything before first non-nav body is already filtered
    out, para, prev = [], None, None
    def flush():
        nonlocal para
        if para: out.append(para)
        para = None
    for it in items:
        if it["head"] and it["size"] >= 24:
            continue
        if it["head"]:
            flush()
            out.append(("#" * (2 if it["size"] >= 18 else 3)) + " " + re.sub(r"\*\*", "", it["md"]))
            prev = it; continue
        if re.match(r"^(\d+\.|•|◦)\s", it["plain"]):
            flush(); txt = re.sub(r"^•\s*", "- ", it["md"]); para = txt
        elif para is not None and prev and not prev["head"] and it["pn"] == prev["pn"] and it["y0"] - prev["y1"] < 10 and not re.match(r"^\*{0,2}(Note|Tip|Important|Warning|Disclaimer)\b", it["plain"]):
            para += " " + it["md"]
        elif para is not None and prev and it["pn"] != prev["pn"] and not re.search(r"[.:!?)\]]\**$", para) and it["plain"][:1].islower():
            para += " " + it["md"]
        else:
            flush(); para = it["md"]
            if re.match(r"^\*{0,2}(Note|Tip|Important|Warning|Disclaimer)\b", it["plain"]): para = "> " + para
        prev = it
    flush()
    anchor = next((re.match(r"https://support\.mozilla\.org/en-US/kb/[^#)]+", m).group(0) for o in out for m in re.finditer(r"\]\((https://[^)]*#w_[^)]*)\)", o)), None) if False else None
    for o in out:
        m = re.search(r"\((https://support\.mozilla\.org/en-US/kb/[^#)\s]+)#w_", o)
        if m: anchor = m.group(1); break
    if anchor and (not footer_url or footer_url.endswith("...")): footer_url = anchor
    out = [o for o in out if not re.match(r"^\[[^\]]+\]\(https://support\.mozilla\.org/en-US/products/firefox[^)]*\)$", o)]
    out = [o for o in out if not re.match(r"^- \[[^\]]*\]\(https://[^)]*#w_[^)]*\)$", o)]
    body = "\n\n".join(out)
    body = re.sub(r"\*\*\s*\*\*", "", body)
    return title, footer_url, body

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    seen = set()
    for pdf in sorted(glob.glob(os.path.join(src, "*.pdf"))):
        title, url, body = convert(pdf)
        name = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60].strip("-") + ".md"
        if name in seen: continue
        seen.add(name)
        flag = "" if url and not url.endswith(("-", "...", "…")) else "  <!-- URL may be truncated: check -->"
        open(os.path.join(dst, name), "w").write(f"URL: {url}{flag}\nDate: {date.today()}\n\n# {title}\n\n{body}\n")
        print(name, "|", url)
