from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection import SnowflakeConnetion

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()

    def getIdentity(self, request, context):
        
        curr = self.snowflake_connection.cursor()
        results = curr.execute(f"select hr_id, user_id from identity.identity where hr_id = '{request.hr_id}'").fetchall()

        response_data = identity_pb2.iamData(
            hr_id = results[0][0], 
            user_name = results[0][1]
        )
        return response_data

    def enterIdentity(self, request, context):
        response_data = identity_pb2.iamData(
            hr_id = request.hr_id, 
            user_name = 'rxh82f6'
        )
        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
