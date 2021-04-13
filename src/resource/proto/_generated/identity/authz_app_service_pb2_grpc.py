# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from identity import authz_app_service_pb2 as identity_dot_authz__app__service__pb2


class AuthzAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.isAllowed = channel.unary_unary(
                '/cafm.identity.authz.AuthzAppService/isAllowed',
                request_serializer=identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedRequest.SerializeToString,
                response_deserializer=identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedResponse.FromString,
                )
        self.hashKeys = channel.unary_unary(
                '/cafm.identity.authz.AuthzAppService/hashKeys',
                request_serializer=identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysRequest.SerializeToString,
                response_deserializer=identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysResponse.FromString,
                )


class AuthzAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def isAllowed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def hashKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthzAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'isAllowed': grpc.unary_unary_rpc_method_handler(
                    servicer.isAllowed,
                    request_deserializer=identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedRequest.FromString,
                    response_serializer=identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedResponse.SerializeToString,
            ),
            'hashKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.hashKeys,
                    request_deserializer=identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysRequest.FromString,
                    response_serializer=identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.identity.authz.AuthzAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthzAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def isAllowed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.authz.AuthzAppService/isAllowed',
            identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedRequest.SerializeToString,
            identity_dot_authz__app__service__pb2.AuthzAppService_isAllowedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def hashKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.authz.AuthzAppService/hashKeys',
            identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysRequest.SerializeToString,
            identity_dot_authz__app__service__pb2.AuthzAppService_hashKeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
