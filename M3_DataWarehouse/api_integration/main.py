from fastapi import FastAPI, HTTPException
from utils.warehouse_queries import WarehouseManager
import os

app = FastAPI(title="Retail Voice AI Warehouse API")
db_uri = os.getenv("DATABASE_URL", "postgresql://root:root@localhost:5432/retail_db")
wm = WarehouseManager(db_uri)

@app.get("/health")
def health():
    return {"status": "Warehouse connected", "engine": "Postgres 18"}

@app.get("/customer-context/{customer_id}")
def get_context(customer_id: str):
    try:
        history = wm.get_customer_history(customer_id)
        if history.empty:
            return {"context": "Nuevo cliente", "last_orders": []}
        return {
            "context": "Cliente frecuente",
            "last_orders": history.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
