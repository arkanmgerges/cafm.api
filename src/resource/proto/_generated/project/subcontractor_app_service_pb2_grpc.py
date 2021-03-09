# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import subcontractor_app_service_pb2 as project_dot_subcontractor__app__service__pb2


class SubcontractorAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.subcontractorById = channel.unary_unary(
                '/cafm.project.subcontractor.SubcontractorAppService/subcontractorById',
                request_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdResponse.FromString,
                )
        self.subcontractors = channel.unary_unary(
                '/cafm.project.subcontractor.SubcontractorAppService/subcontractors',
                request_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.subcontractor.SubcontractorAppService/newId',
                request_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdResponse.FromString,
                )


class SubcontractorAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def subcontractorById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def subcontractors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubcontractorAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'subcontractorById': grpc.unary_unary_rpc_method_handler(
                    servicer.subcontractorById,
                    request_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdRequest.FromString,
                    response_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdResponse.SerializeToString,
            ),
            'subcontractors': grpc.unary_unary_rpc_method_handler(
                    servicer.subcontractors,
                    request_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsRequest.FromString,
                    response_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdRequest.FromString,
                    response_serializer=project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.subcontractor.SubcontractorAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubcontractorAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def subcontractorById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor.SubcontractorAppService/subcontractorById',
            project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdRequest.SerializeToString,
            project_dot_subcontractor__app__service__pb2.SubcontractorppService_subcontractorByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def subcontractors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor.SubcontractorAppService/subcontractors',
            project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsRequest.SerializeToString,
            project_dot_subcontractor__app__service__pb2.SubcontractorAppService_subcontractorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor.SubcontractorAppService/newId',
            project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdRequest.SerializeToString,
            project_dot_subcontractor__app__service__pb2.SubcontractorAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
