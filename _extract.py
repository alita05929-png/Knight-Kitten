import re
html = open(r"therobincoin.xyz/index.html", encoding="utf-8").read()
out = []
texts = re.findall(r">([^<]{2,240})<", html)
for t in texts:
    t = t.replace("&amp;", "&").replace("&#x27;", "'").replace("&quot;", '"').strip()
    if t:
        out.append(t)
out.append("\n==== IMAGES ====")
imgs = re.findall(r'(?:src|href)="(/images/[^"]+)"', html)
for i in imgs:
    out.append(i)
open("_extract.txt", "w", encoding="utf-8").write("\n".join(out))
