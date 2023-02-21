# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import getUserId, userId
import identity_pb2_grpc
# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
# import custom libs
from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities
from snowflake.connector import DictCursor
from service_utilities import ServiceUtilities
import identity_constants as const
from identity_utilities import IdentityUtilities
from config_utilities import service_ports

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()
        self.request_attributes = ["identity_id", "user_id"]
        self.response_attributes = list(userId.DESCRIPTOR.fields_by_name.keys())
        self.select_attributes = QueryUtilities().createSelectStatement(self.request_attributes)

    def appearUserId(self, request, context):
            
        if request.identity_id != "":
            select_statement = const.read_identity_query.format(self.select_attributes, "identity_id", request.identity_id)
            results = QueryUtilities().executeSelect(select_statement, self.snowflake_connection)
            try:
                results = results[0]
                results["status_message"] = const.appear_userid_lookup_success_message
                response = ServiceUtilities().getReadResponse(self.response_attributes, results)
            except:
                response = {
                    "identity_id": request.identity_id, 
                    "user_id": IdentityUtilities().generateUserId(self.snowflake_connection, request.first_name, request.middle_name, request.last_name, const.read_user_id_query), 
                    "status_message": const.appear_userid_generate_success_message
                }
        else:
            response = {
                "status_message": "Failed: did not pass identity_id"
            }

        response_data = identity_pb2.userId(**response)

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_ports['appearUserId']}")
    server.start()
    server.wait_for_termination()
