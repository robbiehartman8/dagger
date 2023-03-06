# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")
# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import identityData, readData
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
from config_utilities import service_config

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.snowflake_connection = SnowflakeConnetion().getConnection(self.logger)
        self.service_util = ServiceUtilities()
        self.request_attributes = list(readData.DESCRIPTOR.fields_by_name.keys())
        self.response_attributes = list(identityData.DESCRIPTOR.fields_by_name.keys())
        self.select_attributes = QueryUtilities().createSelectStatement(self.response_attributes)

        self.logger.info(f"Server started running on port: {service_config['readIdentity']['port']}") 

    def readIdentity(self, request, context):

        if request.hr_id != "":
            select_statement = const.read_identity_query.format(self.select_attributes, "hr_id", request.hr_id)
            self.logger.info("hr_id select statement")
        elif request.identity_id != "":
            select_statement = const.read_identity_query.format(self.select_attributes, "identity_id", request.identity_id)
            self.logger.info("identity_id select statement")

        if request.hr_id != "" or request.identity_id != "":
            results = QueryUtilities().executeSelect(select_statement, self.snowflake_connection, self.logger)
            self.logger.info("Executed select statement")
            try:
                results = results[0]
                response = self.service_util.getReadResponse(self.response_attributes, results)
                response_data = identity_pb2.identityData(**response)
                self.logger.info("Entry existed")
            except:
                response_data = identity_pb2.identityData()
                self.logger.info("Entry did not exist")
        else:
            response_data = identity_pb2.identityData()
            self.logger.info("Did not pass hr_id or identity_id")

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=service_config['readIdentity']['workers']))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_config['readIdentity']['port']}")
    server.start()
    server.wait_for_termination()
