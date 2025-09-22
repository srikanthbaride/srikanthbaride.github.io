# Profile-tailored Hugo site (BibTeX auto-render, GA, colors, CV)

## Quick start (Windows PowerShell)
```
# in repo root
./build.ps1    # converts BibTeX -> data/pubs.yaml, then hugo -d docs
git add . && git commit -m "Build" && git push
```

## Update publications
- Edit `static/pubs.bib` (add entries, optional `pdf` field).
- Run `build.ps1` (or `build.sh` on macOS/Linux).

## Google Analytics
- Put your GA4 ID in `config.toml` under `[params] google_analytics`.
