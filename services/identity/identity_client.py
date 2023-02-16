import grpc
import identity_pb2
import identity_pb2_grpc

def getUser():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.getIdentity(identity_pb2.hrData(hr_id='12345'))
    
    print(response)

def enterUser(hrID):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.enterIdentity(identity_pb2.hrData(
            hr_id = str(hrID), 
            first_name = "dan", 
            middle_name = "b", 
            last_name = "hartman", 
            job_title = "eng", 
            location_number = 9999, 
            location_name = "New York", 
            manager_hr_id = "00001"
        ))

        print(response)

for i in range(1000000):
    enterUser(i)
