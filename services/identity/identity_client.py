import grpc
import identity_pb2
import identity_pb2_grpc

def getUser():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.getIdentity(identity_pb2.hrData(
            hr_id='18874754'
        ))
    
    print(response)

def enterUser():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.enterIdentity(identity_pb2.hrData(
            hr_id='12345'
        ))

        print(response.user_name)

if __name__ == '__main__':
    getUser()
