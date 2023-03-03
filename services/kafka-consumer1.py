from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")

import redis
from redis_utilities import RedisUtilities

topic_name="provisioning"
group_id = "provisioning-group"

redUtil = RedisUtilities()
redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")

consumer_partition_1_ids = set()

partition_data_id = 0
while True:
    offset = redis_client.get(f"kafka/provisioning/1/{partition_data_id}")
    if offset is None:
        break
    partition_data_id += 1

consumer_partition_1 = KafkaConsumer(bootstrap_servers=['localhost:9092'],  value_deserializer=lambda m: json.loads(m.decode('utf-8')))
print("Available Kafka topics are ..",consumer_partition_1.topics())

topic_partition = TopicPartition(topic_name, 1)
consumer_partition_1.assign([topic_partition])
consumer_partition_1.subscription()    
consumer_partition_1.seek(topic_partition, partition_data_id)

for message in consumer_partition_1:    
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
    redis_client.set(f"kafka/provisioning/1/{message.offset}", 1)
