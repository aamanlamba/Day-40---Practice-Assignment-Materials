#!/usr/bin/env sh
set -eu
python scripts/self_check.py
python -m pytest
