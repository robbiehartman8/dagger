import threading
import json
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
import redis
from redis_utilities import RedisUtilities
from config_utilities import kafka_partitions
from kafka_utilities import KafkaUtilities
from odin_provisioining_utilities import OdinProvisioningUtilities

if __name__ =="__main__":

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    kafka_server = ["localhost:9092"]
    redUtil = RedisUtilities()
    redis_client = redUtil.getRedisClient("localhost", 6379, 0, "logger")
    thread_list = []

    for prov_thr in range(kafka_partitions["provisioning"]["provisioning"]):
        thread = threading.Thread(target=OdinProvisioningUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server, logger), KafkaUtilities().getKafkaProducer(kafka_server, logger), "provisioning", "provisioning-group", prov_thr, "", [], logger))
        thread_list.append(thread)
        thread_list[-1].start()
        logger.info(f"provisioning thread {prov_thr}")
    
    for deprov_thr in range(kafka_partitions["provisioning"]["deprovisioning"]):
        thread = threading.Thread(target=OdinProvisioningUtilities().consumeData, args=(redis_client, KafkaUtilities().getKafkaConsumer(kafka_server, logger), KafkaUtilities().getKafkaProducer(kafka_server, logger), "deprovisioning", "provisioning-group", deprov_thr, "", [], logger))
        thread_list.append(thread)
        thread_list[-1].start()
        logger.info(f"deprovisioning thread {deprov_thr}")