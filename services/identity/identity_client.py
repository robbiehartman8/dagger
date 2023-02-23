import grpc
import identity_pb2
import identity_pb2_grpc

import threading
import time

def readIdentity(hr_id_number):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        response = stub.readIdentity(identity_pb2.readData(
            hr_id=hr_id_number
            # identity_id="2839"
        ))
    
    print(response)

def createUpdateIdentity(star, stop):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = identity_pb2_grpc.IdentityStub(channel)
        for i in range(star, stop):
            response = stub.createUpdateIdentity(identity_pb2.hrData(
                hr_id=str(i),
                legal_first_name='robert',
                legal_middle_name='maurice',
                legal_last_name='hartman',
                preferred_first_name='robert',
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
            identity_id='3ac4cd09d0d7b58138018bf0d009f7f1',
            first_name="robert",
            middle_name="maurice",
            last_name="hartman"
        ))

    print(response)

if __name__ == '__main__':
    # for i in range(1):
    # hr_id = str("hello")
    # createUpdateIdentity(0, 1)
    #     readIdentity(hr_id)
    appearUserIdClient()

    # # creating threads
    # t1 = threading.Thread(target=createUpdateIdentity, args=(0, 10,))
    # t2 = threading.Thread(target=createUpdateIdentity, args=(11, 20,))
    # t3 = threading.Thread(target=createUpdateIdentity, args=(21, 30,))
    # t4 = threading.Thread(target=createUpdateIdentity, args=(31, 40,))
    # t5 = threading.Thread(target=createUpdateIdentity, args=(41, 50,))
    # t6 = threading.Thread(target=createUpdateIdentity, args=(51, 60,))

    # # starting threads
    # t1.start()
    # time.sleep(0.5)
    # t2.start()
    # time.sleep(0.5)
    # t3.start()
    # time.sleep(0.5)
    # t4.start()
    # time.sleep(0.5)
    # t5.start()
    # time.sleep(0.5)
    # t6.start()
 
    # # wait until all threads finish
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
