import threading
import json
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
import redis
from redis_utilities import RedisUtilities
from config_utilities import kafka_partitions
from kafka_utilities import KafkaUtilities
from odin_identity_utilities import OdinIdentityUtilities

if __name__ =="__main__":

    kafka_server = ["localhost:9092"]
    redUtil = RedisUtilities()
    redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")
    thread_list = []

    for create_thr in range(kafka_partitions["identity"]["identity_create"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server), KafkaUtilities().getKafkaProducer(kafka_server), "identity_create", "identity-group", create_thr, "service", []))
        thread_list.append(thread)
        thread_list[-1].start()
        print(f"Create thread {create_thr}")
    
    for update_thr in range(kafka_partitions["identity"]["identity_update"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server), KafkaUtilities().getKafkaProducer(kafka_server), "identity_update", "identity-group", update_thr, "service", []))
        thread_list.append(thread)
        thread_list[-1].start()
        print(f"Update thread {update_thr}")

    for delete_thr in range(kafka_partitions["identity"]["identity_delete"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server), KafkaUtilities().getKafkaProducer(kafka_server), "identity_delete", "identity-group", delete_thr, "forward", ["provisioning"]))
        thread_list.append(thread)
        thread_list[-1].start()
        print(f"Delete thread {delete_thr}")