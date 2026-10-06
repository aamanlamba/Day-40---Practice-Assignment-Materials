import pandas as pd
from pathlib import Path
DATA=Path(__file__).resolve().parents[1]/"data"
apps=pd.read_csv(DATA/"applications.csv")
reps=pd.read_csv(DATA/"repayments.csv")
# weak join assumption can produce mismatched customer relationships
merged=reps.merge(apps[["application_id","customer_id","amount"]], on="application_id", how="left", suffixes=("_rep","_app"))
print("mismatched customers", (merged.customer_id_rep != merged.customer_id_app).sum())
