from concurrent import futures
import grpc
import identity_pb2
import identity_pb2_grpc
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
from snowflake_connection import SnowflakeConnetion
from query_utilities import QueryUtil
from snowflake.connector import DictCursor
import identity_constants as const

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        self.snowflake_connection = SnowflakeConnetion().getConnection()

    def readIdentity(self, request, context):

        select_attributes = QueryUtil().getSelectQuery(const.identity_attribute_list)

        if request.hr_id != "":
            read_query = const.read_identity_query.format(select_attributes, "hr_id", request.hr_id)
        elif request.identity_id != "":
            read_query = const.read_identity_query.format(select_attributes, "identity_id", request.identity_id)

        if request.hr_id != "" or request.identity_id != "":
            try:
                curr = self.snowflake_connection.cursor(DictCursor)
                results = curr.execute(read_query).fetchall()
            except:
                self.snowflake_connection = SnowflakeConnetion().getConnection()
                curr = self.snowflake_connection.cursor(DictCursor)
                results = curr.execute(read_query).fetchall()

            try:
                results = results[0]
                response_data = identity_pb2.identityData(
                    hr_id = results["HR_ID"], 
                    user_id = results["USER_ID"]
                )
            except:
                response_data = dentity_pb2.identityData()
        else:
            response_data = dentity_pb2.identityData()

        return response_data

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
