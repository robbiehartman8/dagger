# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import identity_pb2 as identity__pb2


class IdentityStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createUpdateIdentity = channel.unary_unary(
                '/Identity/createUpdateIdentity',
                request_serializer=identity__pb2.hrData.SerializeToString,
                response_deserializer=identity__pb2.hrDataMessage.FromString,
                )
        self.readIdentity = channel.unary_unary(
                '/Identity/readIdentity',
                request_serializer=identity__pb2.readData.SerializeToString,
                response_deserializer=identity__pb2.identityData.FromString,
                )
        self.deleteIdentity = channel.unary_unary(
                '/Identity/deleteIdentity',
                request_serializer=identity__pb2.deleteData.SerializeToString,
                response_deserializer=identity__pb2.deleteMessage.FromString,
                )
        self.appearUserId = channel.unary_unary(
                '/Identity/appearUserId',
                request_serializer=identity__pb2.getUserId.SerializeToString,
                response_deserializer=identity__pb2.userId.FromString,
                )


class IdentityServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createUpdateIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def appearUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createUpdateIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.createUpdateIdentity,
                    request_deserializer=identity__pb2.hrData.FromString,
                    response_serializer=identity__pb2.hrDataMessage.SerializeToString,
            ),
            'readIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.readIdentity,
                    request_deserializer=identity__pb2.readData.FromString,
                    response_serializer=identity__pb2.identityData.SerializeToString,
            ),
            'deleteIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteIdentity,
                    request_deserializer=identity__pb2.deleteData.FromString,
                    response_serializer=identity__pb2.deleteMessage.SerializeToString,
            ),
            'appearUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.appearUserId,
                    request_deserializer=identity__pb2.getUserId.FromString,
                    response_serializer=identity__pb2.userId.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Identity', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Identity(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createUpdateIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/createUpdateIdentity',
            identity__pb2.hrData.SerializeToString,
            identity__pb2.hrDataMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/readIdentity',
            identity__pb2.readData.SerializeToString,
            identity__pb2.identityData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/deleteIdentity',
            identity__pb2.deleteData.SerializeToString,
            identity__pb2.deleteMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def appearUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/appearUserId',
            identity__pb2.getUserId.SerializeToString,
            identity__pb2.userId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
