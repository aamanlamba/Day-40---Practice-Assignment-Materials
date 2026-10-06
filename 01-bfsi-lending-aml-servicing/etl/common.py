import pandas as pd

def read_csv(path):
    return pd.read_csv(path, low_memory=False)

def clean_columns(df):
    # Aggressive transformation can cause collisions.
    df.columns = [c.strip().lower().replace(" ", "_").replace("-", "_") for c in df.columns]
    return df

def drop_bad_rows(df):
    # Legacy behavior: rows with any missing field are discarded.
    return df.dropna()
