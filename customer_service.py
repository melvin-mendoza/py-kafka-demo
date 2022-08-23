import json
import time

from kafka import KafkaProducer

MEMBER_KAFKA_TOPIC = "member_details"
MEMBER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Generate record every 5 seconds...")
time.sleep(10)

for i in range(MEMBER_LIMIT):
    data = {
        "txn_id": i,
        "member_id": f"MEMBER_{i}",
        "txn_type": "NEW",
    }

    producer.send(MEMBER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    print(f"Done sending to {MEMBER_KAFKA_TOPIC} ... {i}")
    #print(json.dumps(data))
    time.sleep(5)
