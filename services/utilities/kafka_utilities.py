from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json

class KafkaUtilities:

    def getKafkaProducer(self, kafka_host, logger):
        try:
            connection = KafkaProducer(bootstrap_servers=kafka_host)
            return connection
        except:
            logger.critical(f"Could not connect to kafka host: {kafka_host}")

    def getKafkaConsumer(self, kafka_host, logger):
        try:
            connection = KafkaConsumer(bootstrap_servers=kafka_host,  value_deserializer=lambda m: json.loads(m.decode("utf-8")))
            return connection
        except:
            logger.critical(f"Could not connect to kafka host: {kafka_host}")

    def sendData(self, producer, topic_name, message, logger):
        try:
            serialized_message = json.dumps(message).encode('utf-8')
            producer.send(topic_name, value=serialized_message)
            producer.flush()
            return True
        except:
            logger.critical(f"Could not forward kafka message : {message.value}")
            return False