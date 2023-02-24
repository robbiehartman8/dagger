from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer('provisioning', bootstrap_servers=['localhost:9092'])

# Continuously poll for new messages
for message in consumer:
    # Print the message key and value
    print(f"Received message: key={message.key}, value={message.value}")
