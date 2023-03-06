from kafka import TopicPartition
import json
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from kafka_utilities import KafkaUtilities


class OdinProvisioningUtilities:

    # move this to its own subfolder
    # mechanism == "forward"
    #   mechanism list attributes
    #   0: topic_name
    def consumeData(self, redis_client, consumer, producer, topic_name, group_id, partition_id, mechanism, mechanism_list, logger):
        consumer_partition_ids = set()
        partition_data_id = 0
        while True:
            offset = redis_client.get(f"kafka/{topic_name}/{partition_id}/{partition_data_id}")
            if offset is None:
                break
            partition_data_id += 1

        logger.info(f"Starting kafka cumsume data at partition_data_id: {partition_data_id}")

        topic_partition = TopicPartition(topic_name, partition_id)
        consumer.assign([topic_partition])
        consumer.subscription()
        consumer.seek(topic_partition, partition_data_id)

        for message in consumer:
            redis_client.set(f"kafka/{topic_name}/{partition_id}/{message.offset}", 1)
            print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

            if mechanism == "forward":
                sent = KafkaUtilities().sendData(producer, mechanism_list[0], message.value, logger)
            elif mechanism == "service":
                pass
            # TODO: call birthright service