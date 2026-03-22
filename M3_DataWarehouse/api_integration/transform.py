# transform.py (silver)
import pandas as pd

df = pd.read_parquet("data/bronze/tickets.parquet")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
df["resolved_at"] = pd.to_datetime(df["resolved_at"], errors="coerce")

df = df.drop_duplicates()

df.to_parquet("data/silver/tickets_clean.parquet", index=False)