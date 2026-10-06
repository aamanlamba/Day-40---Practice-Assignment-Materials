import sqlite3, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
db = ROOT / "brownfield.db"
if db.exists():
    db.unlink()
con = sqlite3.connect(db)
for name in ['customers', 'applications', 'transactions', 'alerts', 'repayments']:
    path = ROOT / "data" / f"{name}.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        continue
    cols = list(rows[0].keys())
    con.execute(f'DROP TABLE IF EXISTS "{name}"')
    con.execute('CREATE TABLE "' + name + '" (' + ','.join([f'"{c}" TEXT' for c in cols]) + ')')
    q = 'INSERT INTO "' + name + '" VALUES (' + ','.join(['?']*len(cols)) + ')'
    con.executemany(q, [[r.get(c) for c in cols] for r in rows])
con.commit()
con.close()
print(f"Created {db}")
