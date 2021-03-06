# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project.lookup.project import project_lookup_app_service_pb2 as project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2


class ProjectLookupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.lookup = channel.unary_unary(
                '/cafm.project.lookup.project.ProjectLookupAppService/lookup',
                request_serializer=project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsRequest.SerializeToString,
                response_deserializer=project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsResponse.FromString,
                )


class ProjectLookupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def lookup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectLookupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.lookup,
                    request_deserializer=project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsRequest.FromString,
                    response_serializer=project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.lookup.project.ProjectLookupAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectLookupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.lookup.project.ProjectLookupAppService/lookup',
            project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsRequest.SerializeToString,
            project_dot_lookup_dot_project_dot_project__lookup__app__service__pb2.ProjectLookupAppService_projectLookupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
