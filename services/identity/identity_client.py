import grpc
import identity_pb2
import identity_pb2_grpc

def readIdentity():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.readIdentity(identity_pb2.readData(
            hr_id='29300'
            # identity_id="2839"
        ))
    
    print(response)

def createUpdateIdentity():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.createUpdateIdentity(identity_pb2.hrData(
            hr_id='29393939393',
            legal_first_name='robert',
            legal_last_name='hartman'
        ))

    print(response)

def appearUserIdClient():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.appearUserId(identity_pb2.getUserId(
            identity_id='fe1fa635d557855ae678d7081ac1ab245',
            first_name="robert",
            middle_name="maurice",
            last_name="hartman"
        ))

    print(response)

if __name__ == '__main__':
    appearUserIdClient()
