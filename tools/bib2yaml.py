import os, yaml, bibtexparser

base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
bib_path = os.path.join(base, "static", "pubs.bib")
out_path = os.path.join(base, "data", "pubs.yaml")

with open(bib_path, encoding="utf-8") as f:
    db = bibtexparser.load(f)

pubs = []
for e in db.entries:
    pubs.append({
        "type": e.get("ENTRYTYPE",""),
        "key": e.get("ID",""),
        "author": e.get("author",""),
        "title": e.get("title",""),
        "journal": e.get("journal",""),
        "booktitle": e.get("booktitle",""),
        "year": e.get("year",""),
        "pdf": e.get("pdf",""),
    })

os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(pubs, f, sort_keys=False, allow_unicode=True)
print(f"Wrote {out_path} with {len(pubs)} entries.")
