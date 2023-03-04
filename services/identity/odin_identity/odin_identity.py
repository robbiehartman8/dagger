from kafka import KafkaConsumer
from kafka import TopicPartition
import threading
import json
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
import redis
from redis_utilities import RedisUtilities

def consumeData(redis_client, kafka_host, topic_name, group_id, partition_id):
    consumer_partition_ids = set()
    partition_data_id = 0
    while True:
        offset = redis_client.get(f"kafka/{topic_name}/{partition_id}/{partition_data_id}")
        if offset is None:
            break
        partition_data_id += 1

    consumer_partition = KafkaConsumer(bootstrap_servers=kafka_host,  value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    topic_partition = TopicPartition(topic_name, partition_id)
    consumer_partition.assign([topic_partition])
    consumer_partition.subscription()    
    consumer_partition.seek(topic_partition, partition_data_id)

    for message in consumer_partition:    
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
        redis_client.set(f"kafka/{topic_name}/{partition_id}/{message.offset}", 1)
    
topic_name="provisioning"
group_id = "provisioning-group"
kafka_server = ['localhost:9092']

redUtil = RedisUtilities()
redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")

if __name__ =="__main__":
    n_threads= 4
    thread_list = []

    for thr in range(n_threads):
        thread = threading.Thread(target=consumeData, args=(redis_client, kafka_server, topic_name, group_id, thr))
        thread_list.append(thread)
        thread_list[-1].start()
        print(thr)