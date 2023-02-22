import grpc
import identity_pb2
import identity_pb2_grpc

import threading

def readIdentity(hr_id_number):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.readIdentity(identity_pb2.readData(
            hr_id=hr_id_number
            # identity_id="2839"
        ))
    
    print(response)

def createUpdateIdentity1():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        for i in range(100):
            response = stub.createUpdateIdentity(identity_pb2.hrData(
                hr_id=str(i),
                legal_first_name='robert',
                legal_middle_name='maurice',
                legal_last_name='hartman',
                preferred_first_name='rob',
                preferred_middle_name='',
                preferred_last_name='hartman',
                job_title_code='ceng',
                job_title_description='chief engineer',
                job_title_level='100',
                location_code='1001',
                location_name='new york',
                location_address='new york',
                phone_number_work='555-555-5555',
                phone_number_work_mobile='555-555-5555',
                phone_number_home='555-555-5555',
                phone_number_home_mobile='555-555-5555',
                email_work_primary='robhartman@hartmancorp.com',
                email_home_primary='robhartman@hartmancorp.com',
                status='A',
                hire_start_date='2023-02-01',
                termination_date='',
                leave_of_absense_start_date='',
                leave_of_absense_end_date='',
                employee_type='full_time',
                cost_center='100000001',
                manager_hr_id=str(i)
            ))

            print(response)

def createUpdateIdentity2():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        for i in range(101, 200):
            response = stub.createUpdateIdentity(identity_pb2.hrData(
                hr_id=str(i),
                legal_first_name='robert',
                legal_middle_name='maurice',
                legal_last_name='hartman',
                preferred_first_name='rob',
                preferred_middle_name='',
                preferred_last_name='hartman',
                job_title_code='ceng',
                job_title_description='chief engineer',
                job_title_level='100',
                location_code='1001',
                location_name='new york',
                location_address='new york',
                phone_number_work='555-555-5555',
                phone_number_work_mobile='555-555-5555',
                phone_number_home='555-555-5555',
                phone_number_home_mobile='555-555-5555',
                email_work_primary='robhartman@hartmancorp.com',
                email_home_primary='robhartman@hartmancorp.com',
                status='A',
                hire_start_date='2023-02-01',
                termination_date='',
                leave_of_absense_start_date='',
                leave_of_absense_end_date='',
                employee_type='full_time',
                cost_center='100000001',
                manager_hr_id=str(i)
            ))

            print(response)

def appearUserIdClient():
    with grpc.insecure_channel('localhost:50054') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.appearUserId(identity_pb2.getUserId(
            identity_id='skd',
            first_name="robert",
            middle_name="maurice",
            last_name="hartman"
        ))

    print(response)

if __name__ == '__main__':
    # for i in range(500):
    #     hr_id = str(i)
    #     createUpdateIdentity(hr_id)
    # readIdentity(hr_id)
    # appearUserIdClient()

    # creating threads
    t1 = threading.Thread(target=createUpdateIdentity1)
    t2 = threading.Thread(target=createUpdateIdentity2) 

    # starting threads
    t1.start()
    t2.start()
 
    # wait until all threads finish
    t1.join()
    t2.join()