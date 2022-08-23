import json

from kafka import KafkaConsumer

MEMBER_CONFIRMED_KAFKA_TOPIC = "member_confirmed"

consumer = KafkaConsumer(
    MEMBER_CONFIRMED_KAFKA_TOPIC, 
    bootstrap_servers="localhost:29092"
)

emails_sent_so_far = set()
print("Start listening...")
while True:
    for message in consumer:
        consumed_message = json.loads(message.value.decode())
        email = consumed_message["email"]
        validation = consumed_message["validation"]
        print(f"Application Status: {validation}")
        print(f"Sending email to {email}")
        emails_sent_so_far.add(email)
        print(f"So far emails sent to {len(emails_sent_so_far)} unique emails")
