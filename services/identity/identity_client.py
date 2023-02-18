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
            hr_id='293',
            legal_first_name='23',
            legal_last_name=''
        ))

    print(response)

if __name__ == '__main__':
    createUpdateIdentity()
