#!/usr/bin/env python3
import re, os, sys, yaml

# Minimal BibTeX parser: handles @type{key, field = {value}, ...}
ENTRY_RE = re.compile(r'@(\w+)\s*\{\s*([^,]+)\s*,(.*?)\}\s*', re.S)
FIELD_RE = re.compile(r'(\w+)\s*=\s*([{\"])(.*?)(?<!\\)\2\s*,?', re.S)

def parse_bibtex(text):
    pubs = []
    for m in ENTRY_RE.finditer(text):
        entry_type, key, body = m.groups()
        fields = dict((k.lower(), v.strip()) for k,_,v in FIELD_RE.findall(body))
        pubs.append({
            "type": entry_type.lower(),
            "key": key.strip(),
            "author": fields.get("author",""),
            "title": fields.get("title",""),
            "journal": fields.get("journal",""),
            "booktitle": fields.get("booktitle",""),
            "year": fields.get("year",""),
            "pdf": fields.get("pdf",""),
        })
    return pubs

def main():
    here = os.path.dirname(__file__)
    base = os.path.abspath(os.path.join(here, ".."))
    bib = os.path.join(base, "static", "pubs.bib")
    out = os.path.join(base, "data", "pubs.yaml")
    if not os.path.exists(bib):
        print("No static/pubs.bib found", file=sys.stderr); sys.exit(1)
    with open(bib, "r", encoding="utf-8") as f:
        txt = f.read()
    pubs = parse_bibtex(txt)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        yaml.safe_dump(pubs, f, sort_keys=False, allow_unicode=True)
    print(f"Wrote {out} with {len(pubs)} entries.")
if __name__ == "__main__":
    try:
        import yaml as _y
    except Exception as e:
        print("PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    main()
