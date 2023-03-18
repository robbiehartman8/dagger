import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")

import grpc
import identity_pb2
import identity_pb2_grpc

class CallService:

    def callAppearUserId(self, host, port, request_dict):
        with grpc.insecure_channel(f"{host}:{port}") as channel:
            stub = identity_pb2_grpc.IdentityStub(channel)
            response = stub.appearUserId(identity_pb2.getUserId(**request_dict))
        return response

    def callReadIdentity(self, host, port, request_dict):
        with grpc.insecure_channel(f"{host}:{port}") as channel:
            stub = identity_pb2_grpc.IdentityStub(channel)
            response = stub.readIdentity(identity_pb2.readData(**request_dict))
        return response
