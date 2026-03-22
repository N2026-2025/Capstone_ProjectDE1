# warehouse.py(gold)
import pandas as pd

df = pd.read_parquet("data/silver/tickets_clean.parquet")

# Dimensión cliente
dim_customers = df[["customer_id"]].drop_duplicates()

# Dimensión agente
dim_agents = df[["agent"]].drop_duplicates()

# Fact table
fact_tickets = df[[
    "ticket_id",
    "customer_id",
    "agent",
    "created_at",
    "resolved_at",
    "priority",
    "status"
]]

dim_customers.to_parquet("data/gold/dim_customers.parquet", index=False)
dim_agents.to_parquet("data/gold/dim_agents.parquet", index=False)
fact_tickets.to_parquet("data/gold/fact_tickets.parquet", index=False)