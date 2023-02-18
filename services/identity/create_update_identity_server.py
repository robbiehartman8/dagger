from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc
from google.protobuf.json_format import MessageToDict
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection_utilities import SnowflakeConnetion
from snowflake.connector import DictCursor
from snowflake import connector
connector.paramstyle='qmark'
import identity_constants as const
from service_utilities import ServiceUtilities
from query_utilities import QueryUtilities


class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()

    def createUpdateIdentity(self, request, context):        

        reuqest_data = MessageToDict(request, preserving_proto_field_name=True)
        request_data = ServiceUtilities().cleanRequest(reuqest_data)
        merge_statment = QueryUtilities().getMergeQuery(request_data, const.create_update_identity_query)

        if "hr_id" in request_data and request_data["hr_id"] != "":
            try:
                curr = self.snowflake_connection.cursor()
                curr.execute(merge_statment)
            except:
                self.snowflake_connection = SnowflakeConnetion().getConnection()
                curr = self.snowflake_connection.cursor()
                results = curr.execute(merge_statment)

        response_data = identity_pb2.identityData(**request_data)

        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
