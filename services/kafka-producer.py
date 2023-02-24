from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer

# Define the Avro schema for the message value
schema_str = """
{
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}
"""

# Load the Avro schema
schema = avro.loads(schema_str)

# Configure the Kafka producer
producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://localhost:8081',
    'client.id': 'python-kafka-producer'
}

# Define a message to send
message_value = {"name": "Alice", "age": 25}

# Create an AvroProducer instance
producer = AvroProducer(producer_conf, default_value_schema=schema)

# Produce the message to the Kafka topic 'my-topic'
producer.produce(topic='my-topic', value=message_value)

# Wait for any outstanding messages to be delivered and delivery reports
# to be received.
producer.flush()
