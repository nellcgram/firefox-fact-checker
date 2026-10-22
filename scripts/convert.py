import re, subprocess, sys, glob, os
from datetime import date

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
for pdf in sorted(glob.glob(os.path.join(src, "*.pdf"))):
    raw = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    raw = raw.replace("\ufb01", "fi").replace("\ufb02", "fl")
    url = re.search(r"https://support\.mozilla\.org/\S+", raw)
    lines = []
    for l in raw.splitlines():
        s = l.strip()
        if not s or "| Firefox Help" in s or re.match(r"^\d+ of \d+\s+\d+/\d+/\d+", s):
            continue
        lines.append(s)
    text = "\n".join(lines)
    start = re.search(r"\n(Firefox\s+Last updated:.*)\n", text)
    text = text[start.start()+1:] if start else text
    end = re.search(r"\nShare this article:", text)
    text = text[:end.start()] if end else text
    title = re.sub(r" \| Firefox Help.*", "", raw.splitlines()[0]).strip()
    name = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60] + ".md"
    open(os.path.join(out, name), "w").write(
        f"URL: {url.group(0) if url else 'UNKNOWN'}\nDate: {date.today()}\n\n# {title}\n\n{text}\n")
    print(name)