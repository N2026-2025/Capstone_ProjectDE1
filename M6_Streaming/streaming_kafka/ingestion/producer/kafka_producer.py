import json
import random
import time
from datetime import datetime

# Simula la entrada de tickets con datos para CAC y ROI
def generate_ticket():
    return {
        "ticket_id": random.randint(1000, 9999),
        "customer_id": random.randint(1, 500),
        "email": f"user_{random.randint(1,100)}@gmail.com", # PII a hashear
        "category": random.choice(["Billing", "Technical", "Sales"]),
        "cac": round(random.uniform(10.0, 50.0), 2), # Costo Adquisici√≥n
        "revenue": round(random.uniform(100.0, 1000.0), 2), # Ingreso x Cliente
        "nps_score": random.randint(1, 10),
        "created_at": datetime.now().isoformat()
    }

print("Ì≥° Enviando eventos a Kafka...")
# Aqu√≠ ir√≠a la l√≥gica de kafka-python para enviar al topic 'raw_tickets'
