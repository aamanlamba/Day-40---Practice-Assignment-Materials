from pathlib import Path
from common import read_csv, clean_columns, drop_bad_rows

DATA = Path(__file__).resolve().parents[1] / "data"

def run():
    counts = {}
    for name in ['customers', 'applications', 'transactions', 'alerts', 'repayments']:
        df = read_csv(DATA / f"{name}.csv")
        before = len(df)
        df = clean_columns(df)
        df = drop_bad_rows(df)
        counts[name] = {"before": before, "after": len(df)}
    return counts

if __name__ == "__main__":
    print(run())
