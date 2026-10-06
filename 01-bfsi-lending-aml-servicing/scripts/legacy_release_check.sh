#!/usr/bin/env sh
# Inherited local release check. Deliberately incomplete: workshop teams should assess adequacy.
set -e
python scripts/self_check.py
python -m pytest -q
echo "manual release check complete"
