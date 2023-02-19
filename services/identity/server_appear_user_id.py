from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import getUserId
import identity_pb2_grpc
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities
from snowflake.connector import DictCursor
from service_utilities import ServiceUtilities
import identity_constants as const

# TODO: do all of this

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()
        self.service_util = ServiceUtilities()
        self.service_attributes = list(getUserId.DESCRIPTOR.fields_by_name.keys())
        self.select_attributes = QueryUtilities().getSelectQuery(self.service_attributes)

    def appearUserId(self, request, context):

        if request.identity_id != "":
            read_query = const.read_identity_query.format(self.select_attributes, "identity_id", request.identity_id)
        elif request.user_id != "":
            read_query = const.read_identity_query.format(self.select_attributes, "user_id", request.user_id)

        if request.identity_id != "" or request.user_id != "":
            try:
                curr = self.snowflake_connection.cursor(DictCursor)
                results = curr.execute(read_query).fetchall()
            except:
                self.snowflake_connection = SnowflakeConnetion().getConnection()
                curr = self.snowflake_connection.cursor(DictCursor)
                results = curr.execute(read_query).fetchall()

        else:
            response_data = identity_pb2.userId()

        print(results[0])

        results = {'identity_id': 'test', 'user_id': '7373', 'status_message': 'Success'}

        response_data = identity_pb2.userId(**results)

        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
