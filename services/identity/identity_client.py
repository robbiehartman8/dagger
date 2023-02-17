import grpc
import identity_pb2
import identity_pb2_grpc

def readIdentity():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.readIdentity(identity_pb2.readData(
            hr_id='2388932'
            # identity_id="2839"
        ))
    
    print(response)

def createIdentity():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.createIdentity(identity_pb2.readData(
            hr_id='12345'
        ))

    print(response)

if __name__ == '__main__':
    readIdentity()
