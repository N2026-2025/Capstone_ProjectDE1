import pandas as pd
from sqlalchemy import create_engine

class WarehouseManager:
    def __init__(self, connection_uri):
        self.engine = create_engine(connection_uri)

    def get_customer_history(self, customer_id):
        """Consulta rápida para que la Voice AI sepa quién llama"""
        query = f"SELECT * FROM staging_orders WHERE customer_id = '{customer_id}' ORDER BY invoice_date DESC LIMIT 5"
        return pd.read_sql(query, self.engine)

    def log_call_insight(self, customer_id, transcription, insight_json):
        """Guarda el análisis de Kaggle/Groq en el Warehouse"""
        # Lógica para insertar en la tabla call_logs
        pass
