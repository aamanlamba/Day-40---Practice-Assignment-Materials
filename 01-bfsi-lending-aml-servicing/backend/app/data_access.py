from functools import lru_cache
from pathlib import Path
import csv

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
ALLOWED_ENTITIES = ['customers', 'applications', 'transactions', 'alerts', 'repayments']

@lru_cache(maxsize=32)
def _read_cached(entity: str):
    if entity not in ALLOWED_ENTITIES:
        raise ValueError("unsupported entity")
    path = DATA_DIR / f"{entity}.csv"
    with path.open(encoding="utf-8", newline="") as f:
        return tuple(dict(row) for row in csv.DictReader(f))

def read_entity(entity: str):
    return list(_read_cached(entity))

def clear_cache():
    _read_cached.cache_clear()
