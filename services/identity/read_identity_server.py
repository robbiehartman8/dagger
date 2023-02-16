from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection import SnowflakeConnetion
from snowflake.connector import DictCursor
import identity_constants as const

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()

    def readIdentity(self, request, context):
        
        try:
            curr = self.snowflake_connection.cursor(DictCursor)
            results = curr.execute(const.read_identity_query.format(request.hr_id)).fetchall()
        except:
            self.snowflake_connection = SnowflakeConnetion().getConnection()
            curr = self.snowflake_connection.cursor(DictCursor)
            results = curr.execute(const.read_identity_query.format(request.hr_id)).fetchall()

        try:
            results = results[0]
            response_data = identity_pb2.iamData(
                hr_id = results["HR_ID"], 
                user_name = results["USER_ID"]
            )
        except:
            response_data = const.response_data_null

        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
