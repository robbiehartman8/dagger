# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import getUserId, userId
import identity_pb2_grpc
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
# import custom libs
from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities
from snowflake.connector import DictCursor
from service_utilities import ServiceUtilities
import identity_constants as const
from identity_utilities import IdentityUtilities
from config_utilities import service_config, redis_config
from redis_utilities import RedisUtilities

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.redis_client = RedisUtilities().getRedisClient(redis_config["redis_host"], redis_config["redis_port"], redis_config["redis_database"], self.logger)
        self.request_attributes = ["identity_id", "user_id"]
        self.response_attributes = list(userId.DESCRIPTOR.fields_by_name.keys())
        self.select_attributes = QueryUtilities().createSelectStatement(self.request_attributes)

        self.logger.info(f"Server started running on port: {service_config['appearUserId']['port']}")

    def appearUserId(self, request, context):
            
        if request.identity_id != "":
            response = {
                "identity_id": request.identity_id, 
                "user_id": IdentityUtilities().getUserId(self.redis_client, request.identity_id, request.first_name, request.middle_name, request.last_name, self.logger),
                "status_message": const.appear_userid_success_message
            }
        else:
            response = {
                "status_message": "Failed: did not pass identity_id"
            }

        response_data = identity_pb2.userId(**response)

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=service_config['appearUserId']['workers']))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_config['appearUserId']['port']}")
    server.start()
    server.wait_for_termination()
