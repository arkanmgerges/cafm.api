# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import role_app_service_pb2 as project_dot_role__app__service__pb2


class RoleAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.roleByName = channel.unary_unary(
                '/cafm.project.role.RoleAppService/roleByName',
                request_serializer=project_dot_role__app__service__pb2.RoleAppService_roleByNameRequest.SerializeToString,
                response_deserializer=project_dot_role__app__service__pb2.RoleAppService_roleByNameResponse.FromString,
                )
        self.roleById = channel.unary_unary(
                '/cafm.project.role.RoleAppService/roleById',
                request_serializer=project_dot_role__app__service__pb2.RoleAppService_roleByIdRequest.SerializeToString,
                response_deserializer=project_dot_role__app__service__pb2.RoleAppService_roleByIdResponse.FromString,
                )
        self.roles = channel.unary_unary(
                '/cafm.project.role.RoleAppService/roles',
                request_serializer=project_dot_role__app__service__pb2.RoleAppService_rolesRequest.SerializeToString,
                response_deserializer=project_dot_role__app__service__pb2.RoleAppService_rolesResponse.FromString,
                )


class RoleAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def roleByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def roleById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoleAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'roleByName': grpc.unary_unary_rpc_method_handler(
                    servicer.roleByName,
                    request_deserializer=project_dot_role__app__service__pb2.RoleAppService_roleByNameRequest.FromString,
                    response_serializer=project_dot_role__app__service__pb2.RoleAppService_roleByNameResponse.SerializeToString,
            ),
            'roleById': grpc.unary_unary_rpc_method_handler(
                    servicer.roleById,
                    request_deserializer=project_dot_role__app__service__pb2.RoleAppService_roleByIdRequest.FromString,
                    response_serializer=project_dot_role__app__service__pb2.RoleAppService_roleByIdResponse.SerializeToString,
            ),
            'roles': grpc.unary_unary_rpc_method_handler(
                    servicer.roles,
                    request_deserializer=project_dot_role__app__service__pb2.RoleAppService_rolesRequest.FromString,
                    response_serializer=project_dot_role__app__service__pb2.RoleAppService_rolesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.role.RoleAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoleAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def roleByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.role.RoleAppService/roleByName',
            project_dot_role__app__service__pb2.RoleAppService_roleByNameRequest.SerializeToString,
            project_dot_role__app__service__pb2.RoleAppService_roleByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def roleById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.role.RoleAppService/roleById',
            project_dot_role__app__service__pb2.RoleAppService_roleByIdRequest.SerializeToString,
            project_dot_role__app__service__pb2.RoleAppService_roleByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.role.RoleAppService/roles',
            project_dot_role__app__service__pb2.RoleAppService_rolesRequest.SerializeToString,
            project_dot_role__app__service__pb2.RoleAppService_rolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
