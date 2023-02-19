from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import getUserId
from identity_pb2 import userId
import identity_pb2_grpc
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities
from snowflake.connector import DictCursor
from service_utilities import ServiceUtilities
import identity_constants as const
from identity_utilities import IdentityUtilities

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()
        self.service_util = ServiceUtilities()
        self.request_attributes = []

        self.request_attributes.append("identity_id")
        self.request_attributes.append("user_id")

        self.response_attributes = list(userId.DESCRIPTOR.fields_by_name.keys())
        self.select_attributes = QueryUtilities().getSelectQuery(self.request_attributes)

    def appearUserId(self, request, context):
            
        if request.identity_id != "":
            read_query = const.read_identity_query.format(self.select_attributes, "identity_id", request.identity_id)
            results = QueryUtilities().getSelectData(read_query, self.snowflake_connection)

            try:
                results = results[0]
                results["status_message"] = "Success: user lookup"
                response = self.service_util.getReadResponse(self.response_attributes, results)
            except:
                user_id = IdentityUtilities().getUserId(self.snowflake_connection, request.first_name, request.middle_name, request.last_name, const.read_user_id_query)
                response = {'identity_id': request.identity_id, 'user_id': user_id, 'status_message': 'Success: new user_id'}

        else:
            response = {'status_message': 'Failed: Did not pass identity_id'}

        response_data = identity_pb2.userId(**response)

        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
