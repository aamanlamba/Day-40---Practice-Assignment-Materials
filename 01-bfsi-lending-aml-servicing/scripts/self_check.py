from pathlib import Path
import csv
import importlib
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

REQUIRED = ['customers', 'applications', 'transactions', 'alerts', 'repayments']
problems = []
for name in REQUIRED:
    path = ROOT / "data" / f"{name}.csv"
    if not path.exists():
        problems.append(f"missing data file: {path}")
        continue
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        count = sum(1 for _ in reader)
    if not header or count < 10:
        problems.append(f"invalid/empty data file: {path}")

importlib.import_module("backend.app.main")
if problems:
    raise SystemExit("\n".join(problems))
print("SELF_CHECK_OK")
