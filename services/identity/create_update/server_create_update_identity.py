# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import hrData, hrDataMessage
import identity_pb2_grpc
from google.protobuf.json_format import MessageToDict
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
# import custom libs
from snowflake_connection_utilities import SnowflakeConnetion
import identity_constants as const
from service_utilities import ServiceUtilities
from query_utilities import QueryUtilities
from identity_utilities import IdentityUtilities
from call_service_utilities import CallService
from config_utilities import service_config, kafka_config
from kafka_utilities import KafkaUtilities

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.snowflake_connection = SnowflakeConnetion().getConnection(self.logger)
        self.request_attributes = list(hrData.DESCRIPTOR.fields_by_name.keys())
        self.reponse_attributes = list(hrDataMessage.DESCRIPTOR.fields_by_name.keys())

        self.logger.info(f"Server started running on port: {service_config['createUpdateIdentity']['port']}")

    def createUpdateIdentity(self, request, context):        

        reuqest_data = MessageToDict(request, preserving_proto_field_name=True)
        request_data = ServiceUtilities().cleanCreateUpdateRequest(reuqest_data, self.request_attributes)

        try:
            if request_data["hr_id"] != "":

                request_data["identity_id"] = ServiceUtilities().getTablePK("identity", request_data["hr_id"])

                legal_name_list, preferred_name_list = IdentityUtilities().cleanName([request.legal_first_name, request.legal_middle_name, request.legal_last_name, request.preferred_first_name, request.preferred_middle_name, request.preferred_last_name])
                name_status, name_list = IdentityUtilities().checkNameStatus(legal_name_list, preferred_name_list)
                request_data["use_preferred_name"] = name_status

                get_user_id_request = {"identity_id": request_data["identity_id"], "first_name": name_list[0], "middle_name": name_list[1], "last_name": name_list[2]}
                request_data["user_id"] = MessageToDict(CallService().callAppearUserId(service_config['appearUserId']['host'], service_config['appearUserId']['port'], get_user_id_request), preserving_proto_field_name=True)["user_id"]

                create_update_statement = QueryUtilities().createCreateUpdate(request_data, const.create_update_identity_query)
                query_type = QueryUtilities().executeCreateUpdate(create_update_statement, "create_update", self.snowflake_connection, self.logger)

                if query_type == "insert":
                    KafkaUtilities().sendData(KafkaUtilities().getKafkaProducer(kafka_config["kafka_host"], self.logger), "identity_create", {"identity_id": request_data["identity_id"]}, self.logger)
                elif query_type == "update":
                    KafkaUtilities().sendData(KafkaUtilities().getKafkaProducer(kafka_config["kafka_host"], self.logger), "identity_update", {"identity_id": request_data["identity_id"]}, self.logger)

                response_data = ServiceUtilities().getCreateUpdateResponse(const.create_update_success_message, self.reponse_attributes, request_data)       
        except:
            response_data = ServiceUtilities().getCreateUpdateResponse(const.create_update_fail_message, ["status_message"], request_data)

        response_data = identity_pb2.hrDataMessage(**response_data)

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=service_config['createUpdateIdentity']['workers']))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_config['createUpdateIdentity']['port']}")
    server.start()
    server.wait_for_termination()
