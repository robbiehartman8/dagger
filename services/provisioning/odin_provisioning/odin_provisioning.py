import threading
import json
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
import redis
from redis_utilities import RedisUtilities
from config_utilities import kafka_partitions
from kafka_utilities import KafkaUtilities

if __name__ =="__main__":

    kafka_server = ["localhost:9092"]
    redUtil = RedisUtilities()
    redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")
    thread_list = []

    for prov_thr in range(kafka_partitions["provisioning"]["provisioning"]):
        thread = threading.Thread(target=KafkaUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server), KafkaUtilities().getKafkaProducer(kafka_server), "provisioning", "provisioning-group", prov_thr, "", []))
        thread_list.append(thread)
        thread_list[-1].start()
        print(f"provisioning thread {prov_thr}")
    
    for deprov_thr in range(kafka_partitions["provisioning"]["deprovisioning"]):
        thread = threading.Thread(target=KafkaUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server), KafkaUtilities().getKafkaProducer(kafka_server), "deprovisioning", "provisioning-group", deprov_thr, "", []))
        thread_list.append(thread)
        thread_list[-1].start()
        print(f"deprovisioning thread {deprov_thr}")