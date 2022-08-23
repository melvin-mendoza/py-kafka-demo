import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


MEMBER_KAFKA_TOPIC = "member_details"
MEMBER_CONFIRMED_KAFKA_TOPIC = "member_confirmed"

consumer = KafkaConsumer(
    MEMBER_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)
producer = KafkaProducer(bootstrap_servers="localhost:29092")


print("Start listening...")
while True:
    for message in consumer:
        print("Ongoing transaction..")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        member_id = consumed_message["member_id"]
        txn_type = consumed_message["txn_type"]
        data = {
            "member_id": member_id,
            "validation": "no existing membership found",
            "txn_type": txn_type,
            "email": f"{member_id}@gmail.com"
        }
        print("Successful transaction..")
        producer.send(MEMBER_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
