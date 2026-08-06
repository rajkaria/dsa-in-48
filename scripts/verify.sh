#!/usr/bin/env bash
# Repo verify gate — static page checks. Run from anywhere.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/check_pages.py
