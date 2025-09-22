# Converts BibTeX to YAML, then builds site to /docs
python -m pip install --quiet pyyaml
python tools/bib2yaml.py
hugo -d docs
