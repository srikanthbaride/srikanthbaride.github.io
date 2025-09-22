#!/usr/bin/env bash
set -e
python3 -m pip install -q pyyaml
python3 tools/bib2yaml.py
hugo -d docs
