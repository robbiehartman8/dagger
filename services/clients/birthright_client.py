import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/birthright")
import grpc
import birthright_pb2
import birthright_pb2_grpc

def readBirthrightRule(birthright_rule_id):
    request = {"birthright_rule_id": birthright_rule_id}
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = birthright_pb2_grpc.BirthrightStub(channel)
        response = stub.readBirthrightRule(birthright_pb2.readData(**request))
    print(response)

if __name__ == '__main__':
    readBirthrightRule("4")
