import threading
import json
import logging
import time
logging.basicConfig(format='%(asctime)s %(message)s')
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
import redis
from redis_utilities import RedisUtilities
from config_utilities import kafka_partitions
from kafka_utilities import KafkaUtilities
from odin_identity_utilities import OdinIdentityUtilities
from config_utilities import service_config, kafka_config, redis_config

if __name__ =="__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info(f"Waiting 30 seconds for kafka and redis to start")
    time.sleep(30)

    kafka_server = kafka_config["kafka_host"]
    redUtil = RedisUtilities()
    redis_client = redUtil.getRedisClient(redis_config["redis_host"], redis_config["redis_port"], redis_config["redis_database"], logger)
    thread_list = []

    logger.info(f"Starting threads")

    for create_thr in range(kafka_partitions["identity"]["identity_create"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server, logger), KafkaUtilities().getKafkaProducer(kafka_server, logger), "identity_create", "identity-group", create_thr, "service", [], logger))
        thread_list.append(thread)
        thread_list[-1].start()
        logger.info(f"Create thread {create_thr}")
    
    for update_thr in range(kafka_partitions["identity"]["identity_update"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server, logger), KafkaUtilities().getKafkaProducer(kafka_server, logger), "identity_update", "identity-group", update_thr, "service", [], logger))
        thread_list.append(thread)
        thread_list[-1].start()
        logger.info(f"Update thread {update_thr}")

    for delete_thr in range(kafka_partitions["identity"]["identity_delete"]):
        thread = threading.Thread(target=OdinIdentityUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server, logger), KafkaUtilities().getKafkaProducer(kafka_server, logger), "identity_delete", "identity-group", delete_thr, "forward", ["deprovisioning"], logger))
        thread_list.append(thread)
        thread_list[-1].start()
        logger.info(f"Delete thread {delete_thr}")