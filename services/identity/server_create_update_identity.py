# import python libs
from concurrent import futures
import grpc
import identity_pb2
from identity_pb2 import hrData, hrDataMessage
import identity_pb2_grpc
from google.protobuf.json_format import MessageToDict
# take out with docker
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")
# import custom libs
from snowflake_connection_utilities import SnowflakeConnetion
import identity_constants as const
from service_utilities import ServiceUtilities
from query_utilities import QueryUtilities
from identity_utilities import IdentityUtilities
from call_service_utilities import CallService
from config_utilities import service_ports

class Identity(identity_pb2_grpc.IdentityServicer):

    def __init__(self):
        # self.snowflake_connection = SnowflakeConnetion().getConnection()
        self.request_attributes = list(hrData.DESCRIPTOR.fields_by_name.keys())
        self.reponse_attributes = list(hrDataMessage.DESCRIPTOR.fields_by_name.keys())

    def createUpdateIdentity(self, request, context):        

        reuqest_data = MessageToDict(request, preserving_proto_field_name=True)
        request_data = ServiceUtilities().cleanCreateUpdateRequest(reuqest_data, self.request_attributes)

        try:
            if request_data["hr_id"] != "":

                request_data["identity_id"] = ServiceUtilities().getID("identity", request_data["hr_id"])

                legal_name_list, preferred_name_list = IdentityUtilities().cleanName([request.legal_first_name, request.legal_middle_name, request.legal_last_name, request.preferred_first_name, request.preferred_middle_name, request.preferred_last_name])
                name_status, name_list = IdentityUtilities().checkNameStatus(legal_name_list, preferred_name_list)
                request_data["use_preferred_name"] = name_status

                # get_user_id_request = {"identity_id": request_data["identity_id"], "first_name": name_list[0], "middle_name": name_list[1], "last_name": name_list[2]}
                # request_data["user_id"] = MessageToDict(CallService().callAppearUserId("localhost", service_ports["appearUserId"], get_user_id_request), preserving_proto_field_name=True)["user_id"]

                request_data["user_id"] = 'rxh82f6'

                merge_statement = QueryUtilities().createMergeStatement(request_data, const.create_update_identity_query)
                # QueryUtilities().executeMerge(merge_statement, self.snowflake_connection)
                        
                response_data = ServiceUtilities().getCreateUpdateResponse(const.create_update_success_message, self.reponse_attributes, request_data)       
        except:
            response_data = ServiceUtilities().getCreateUpdateResponse(const.create_update_fail_message, ["status_message"], request_data)

        response_data = identity_pb2.hrDataMessage(**response_data)

        return response_data

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    identity_pb2_grpc.add_IdentityServicer_to_server(Identity(), server)
    server.add_insecure_port(f"[::]:{service_ports['createUpdateIdentity']}")
    server.start()
    server.wait_for_termination()
