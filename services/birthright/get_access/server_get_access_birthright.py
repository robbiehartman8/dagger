# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/birthright")
# import python libs
from concurrent import futures
import grpc
import birthright_pb2
from birthright_pb2 import getAccess, birthrightItemsArray
import birthright_pb2_grpc
from google.protobuf.json_format import MessageToDict
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
# import custom libs
from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities
from snowflake.connector import DictCursor
from service_utilities import ServiceUtilities
from call_service_utilities import CallService
import birthright_constants as const
from birthright_utilities import BirthrightUtilities
from config_utilities import service_config, kafka_config
from kafka_utilities import KafkaUtilities

class Birthright(birthright_pb2_grpc.BirthrightServicer):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.snowflake_connection = SnowflakeConnetion().getConnection(self.logger)
        self.service_util = ServiceUtilities()
        self.request_attributes = list(getAccess.DESCRIPTOR.fields_by_name.keys())
        self.response_attributes = list(birthrightItemsArray.DESCRIPTOR.fields_by_name.keys())

        self.logger.info(f"Server started running on port: {service_config['getAccessBirthright']['port']}") 

    def getBirthrightAccess(self, request, context):

        if request.identity_id != "":
            get_user_id_request = {"identity_id": request.identity_id}
            identity_response = MessageToDict(CallService().callReadIdentity(service_config['readIdentity']['host'], service_config['readIdentity']['port'], get_user_id_request), preserving_proto_field_name=True)
            select_statement = BirthrightUtilities().getBirthrightSelect(identity_response)
            results = QueryUtilities().executeSelect(select_statement, self.snowflake_connection, self.logger)

            self.logger.info("Executed select statement")
            try:
                response = self.service_util.getMVReadResponse(self.response_attributes, results)
                response_data = birthright_pb2.birthrightItemsArray(**response)
                response["identity"] = identity_response
                KafkaUtilities().sendData(KafkaUtilities().getKafkaProducer(kafka_config["kafka_host"], self.logger), "provisioning", response, self.logger)

                self.logger.info("Entry existed")
            except:
                response_data = birthright_pb2.birthrightItemsArray()
                self.logger.info("Entry did not exist")
        else:
            response_data = birthright_pb2.birthrightItemsArray()
            self.logger.info("Did not pass birthright_rule_id")   
        
        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=service_config['getAccessBirthright']['workers']))
    birthright_pb2_grpc.add_BirthrightServicer_to_server(Birthright(), server)
    server.add_insecure_port(f"[::]:{service_config['getAccessBirthright']['port']}")
    server.start()
    server.wait_for_termination()
