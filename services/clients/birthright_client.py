import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/birthright")
import grpc
import birthright_pb2
import birthright_pb2_grpc

from google.protobuf.json_format import MessageToDict

def readBirthrightRule(birthright_rule_id):
    request = {"birthright_rule_id": birthright_rule_id}
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = birthright_pb2_grpc.BirthrightStub(channel)
        response = stub.readBirthrightRule(birthright_pb2.readBirthrightData(**request))
    print(response)

def getAccess(identity_id):
    request = {"identity_id": identity_id}
    with grpc.insecure_channel('localhost:50056') as channel:
        stub = birthright_pb2_grpc.BirthrightStub(channel)
        response = stub.getBirthrightAccess(birthright_pb2.getAccess(**request))
    print(MessageToDict(response))

if __name__ == '__main__':
    # readBirthrightRule("1")
    getAccess("a695103c72ec15c903758592d7d7f294")
