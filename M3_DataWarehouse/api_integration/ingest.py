# ingest.py (bronze)
import pandas as pd

df = pd.read_csv("customer_support_tickets.csv")
df.to_parquet("data/bronze/tickets.parquet", index=False)