from kafka import KafkaProducer
import json

# create Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    # JSON message to send
    message = {"name": "John Doe", "age": i, "city": "New York"}

    # serialize JSON message
    serialized_message = json.dumps(message).encode('utf-8')

    # send message to Kafka topic
    # producer.send('identity_create', value=serialized_message)
    # producer.send('identity_update', value=serialized_message)
    producer.send('identity_delete', value=serialized_message)

# wait for any outstanding messages to be delivered and delivery reports received
producer.flush()

# close producer connection
producer.close()