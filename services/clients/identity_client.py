import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")
import grpc
import identity_pb2
import identity_pb2_grpc

def readIdentity(hr_id_number):
    request = {"hr_id": hr_id_number}
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.readIdentity(identity_pb2.readData(**request))
    print(response)

def createUpdateIdentity(hr_id):
    request = {"hr_id": hr_id, "legal_first_name": "robert", "legal_middle_name": "maurice", "legal_last_name": "hartman", 
               "preferred_first_name": "robert", "preferred_middle_name": "hartman", "preferred_last_name": "hartman"
              }
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.createUpdateIdentity(identity_pb2.hrData(**request))
        print(response)

def appearUserIdClient(identity_id):
    request = {"identity_id": identity_id, "first_name": "robert", "middle_name": "maurice", "last_name": "hartman"}
    with grpc.insecure_channel('localhost:50054') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.appearUserId(identity_pb2.getUserId(**request))
    print(response)

def deleteClient(identity_id):
    request = {"identity_id": identity_id}
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.deleteIdentity(identity_pb2.deleteData(**request))
    print(response)

if __name__ == '__main__':
    for i in range(50):
        createUpdateIdentity(str(i))