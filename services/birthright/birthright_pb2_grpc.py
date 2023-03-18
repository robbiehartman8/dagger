# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import birthright_pb2 as birthright__pb2


class BirthrightStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createUpdateBirthrightRule = channel.unary_unary(
                '/Birthright/createUpdateBirthrightRule',
                request_serializer=birthright__pb2.birthrightRule.SerializeToString,
                response_deserializer=birthright__pb2.birthrightRuleMessage.FromString,
                )
        self.readBirthrightRule = channel.unary_unary(
                '/Birthright/readBirthrightRule',
                request_serializer=birthright__pb2.readBirthrightData.SerializeToString,
                response_deserializer=birthright__pb2.birthrightData.FromString,
                )
        self.deleteBirthrightRule = channel.unary_unary(
                '/Birthright/deleteBirthrightRule',
                request_serializer=birthright__pb2.deleteBirthrightData.SerializeToString,
                response_deserializer=birthright__pb2.deleteBirthrightMessage.FromString,
                )
        self.getBirthrightAccess = channel.unary_unary(
                '/Birthright/getBirthrightAccess',
                request_serializer=birthright__pb2.getAccess.SerializeToString,
                response_deserializer=birthright__pb2.access.FromString,
                )


class BirthrightServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createUpdateBirthrightRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readBirthrightRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteBirthrightRule(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBirthrightAccess(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BirthrightServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createUpdateBirthrightRule': grpc.unary_unary_rpc_method_handler(
                    servicer.createUpdateBirthrightRule,
                    request_deserializer=birthright__pb2.birthrightRule.FromString,
                    response_serializer=birthright__pb2.birthrightRuleMessage.SerializeToString,
            ),
            'readBirthrightRule': grpc.unary_unary_rpc_method_handler(
                    servicer.readBirthrightRule,
                    request_deserializer=birthright__pb2.readBirthrightData.FromString,
                    response_serializer=birthright__pb2.birthrightData.SerializeToString,
            ),
            'deleteBirthrightRule': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteBirthrightRule,
                    request_deserializer=birthright__pb2.deleteBirthrightData.FromString,
                    response_serializer=birthright__pb2.deleteBirthrightMessage.SerializeToString,
            ),
            'getBirthrightAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.getBirthrightAccess,
                    request_deserializer=birthright__pb2.getAccess.FromString,
                    response_serializer=birthright__pb2.access.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Birthright', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Birthright(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createUpdateBirthrightRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Birthright/createUpdateBirthrightRule',
            birthright__pb2.birthrightRule.SerializeToString,
            birthright__pb2.birthrightRuleMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readBirthrightRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Birthright/readBirthrightRule',
            birthright__pb2.readBirthrightData.SerializeToString,
            birthright__pb2.birthrightData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteBirthrightRule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Birthright/deleteBirthrightRule',
            birthright__pb2.deleteBirthrightData.SerializeToString,
            birthright__pb2.deleteBirthrightMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBirthrightAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Birthright/getBirthrightAccess',
            birthright__pb2.getAccess.SerializeToString,
            birthright__pb2.access.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
