#consumer → parquet (lake)
from kafka import KafkaConsumer
import json
import pandas as pd

consumer = KafkaConsumer(
    'tickets_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

data = []

for msg in consumer:
    data.append(msg.value)

    if len(data) >= 1000:
        df = pd.DataFrame(data)
        df.to_parquet("data/bronze/stream_tickets.parquet", append=True)
        data = []