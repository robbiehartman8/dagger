# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import deleteData, deleteMessage
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
from config_utilities import service_ports, service_workers

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.snowflake_connection = SnowflakeConnetion().getConnection(self.logger)
        self.request_attributes = list(deleteData.DESCRIPTOR.fields_by_name.keys())
        self.reponse_attributes = list(deleteMessage.DESCRIPTOR.fields_by_name.keys())

        self.logger.info(f"Server started running on port: {service_ports['deleteIdentity']}")

    def deleteIdentity(self, request, context):        

        reuqest_data = MessageToDict(request, preserving_proto_field_name=True)
        request_data = ServiceUtilities().cleanCreateUpdateRequest(reuqest_data, self.request_attributes)

        if request.identity_id != "":
            mark_statement = const.mark_for_delete_query.format("identity_id", request.identity_id)
            self.logger.info("identity_id mark for delete")
        elif request.hr_id != "":
            mark_statement = const.mark_for_delete_query.format("hr_id", request.hr_id)
            self.logger.info("hr_id mark for delete")

        try:
            QueryUtilities().executeCreateUpdate(mark_statement, self.snowflake_connection, self.logger)
            response_data = {"status_message": const.mark_for_delete_success_message}    
        except:
            response_data = {"status_message": const.mark_for_delete_fail_service_message}

        response_data = identity_pb2.deleteMessage(**response_data)

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=service_workers["deleteIdentity"]))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_ports['deleteIdentity']}")
    server.start()
    server.wait_for_termination()
