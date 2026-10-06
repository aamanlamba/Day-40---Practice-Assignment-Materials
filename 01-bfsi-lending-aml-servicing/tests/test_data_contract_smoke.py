import csv
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"data"
EXPECTED=['customers', 'applications', 'transactions', 'alerts', 'repayments']

def test_required_data_files_exist_and_have_rows():
    for name in EXPECTED:
        p=DATA/f"{name}.csv"
        assert p.exists(), name
        with p.open(encoding="utf-8", newline="") as f:
            rows=list(csv.reader(f))
        assert len(rows) > 10
        assert len(rows[0]) >= 4
