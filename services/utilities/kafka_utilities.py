from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json

class KafkaUtilities:

    def getKafkaConnection(self, kafka_host, connection_type):
        try:
            if connection_type == "producer":
                connection = KafkaProducer(bootstrap_servers=kafka_host)
                return connection
            elif connection_type == "consumer":
                connection = KafkaConsumer(bootstrap_servers=kafka_host,  value_deserializer=lambda m: json.loads(m.decode("utf-8")))
                return connection
        except:
            print("Failed to connect to kakfa")

    def sendData(self, kafka_connection, topic_name, message):
        try:
            serialized_message = json.dumps(message).encode('utf-8')
            kafka_connection.send(topic_name, value=serialized_message)
            kafka_connection.flush()
            return True
        except:
            print("Failed to send message")
            return False

    # mechanism == "forward"
    #   mechanism list attributes
    #   0: topic_name
    def consumeData(self, redis_client, kafka_connection, topic_name, group_id, partition_id, mechanism, mechanism_list):
        consumer_partition_ids = set()
        partition_data_id = 0
        while True:
            offset = redis_client.get(f"kafka/{topic_name}/{partition_id}/{partition_data_id}")
            if offset is None:
                break
            partition_data_id += 1

        topic_partition = TopicPartition(topic_name, partition_id)
        kafka_connection.assign([topic_partition])
        kafka_connection.subscription()    
        kafka_connection.seek(topic_partition, partition_data_id)

        for message in consumer_partition:
            if topic_name == "provisioning":
                print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
            redis_client.set(f"kafka/{topic_name}/{partition_id}/{message.offset}", 1)

            if mechanism == "forward":
                sent = KafkaUtilities().sendData(kafka_host, mechanism_list[0], message.value)
                if sent == False:
                    print(sent)
            elif mechanism == "service":
                pass