import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def stream_call_event(customer_id, text):
    event = {
        "customer_id": customer_id,
        "transcription": text,
        "event_timestamp": time.time()
    }
    producer.send('voice_events', event)
    print(f"í³¡ Evento de llamada enviado a Kafka: {customer_id}")

if __name__ == "__main__":
    stream_call_event("12345", "Hola, quiero saber el estado de mi pedido")
