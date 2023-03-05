from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json

class KafkaUtilities:

    def getKafkaProducer(self, kafka_host):
        try:
            connection = KafkaProducer(bootstrap_servers=kafka_host)
            return connection
        except:
            print("Failed to connect to kakfa")

    def getKafkaConsumer(self, kafka_host):
        try:
            connection = KafkaConsumer(bootstrap_servers=kafka_host,  value_deserializer=lambda m: json.loads(m.decode("utf-8")))
            return connection
        except:
            print("Failed to connect to kakfa")

    def sendData(self, producer, topic_name, message):
        try:
            serialized_message = json.dumps(message).encode('utf-8')
            producer.send(topic_name, value=serialized_message)
            producer.flush()
            return True
        except:
            print("Failed to send message")
            return False

    # move this to its own subfolder
    # mechanism == "forward"
    #   mechanism list attributes
    #   0: topic_name
    def consumeData(self, redis_client, consumer, producer, topic_name, group_id, partition_id, mechanism, mechanism_list):
        consumer_partition_ids = set()
        partition_data_id = 0
        while True:
            offset = redis_client.get(f"kafka/{topic_name}/{partition_id}/{partition_data_id}")
            if offset is None:
                break
            partition_data_id += 1

        topic_partition = TopicPartition(topic_name, partition_id)
        consumer.assign([topic_partition])
        consumer.subscription()    
        consumer.seek(topic_partition, partition_data_id)

        for message in consumer:
            if topic_name == "provisioning":
                print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
            redis_client.set(f"kafka/{topic_name}/{partition_id}/{message.offset}", 1)

            if mechanism == "forward":
                sent = KafkaUtilities().sendData(producer, mechanism_list[0], message.value)
                if sent == False:
                    print(sent)
            elif mechanism == "service":
                pass