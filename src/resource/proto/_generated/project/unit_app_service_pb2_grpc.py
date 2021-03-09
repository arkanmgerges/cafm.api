# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import unit_app_service_pb2 as project_dot_unit__app__service__pb2


class UnitAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.unitById = channel.unary_unary(
                '/cafm.project.unit.UnitAppService/unitById',
                request_serializer=project_dot_unit__app__service__pb2.UnitAppService_unitByIdRequest.SerializeToString,
                response_deserializer=project_dot_unit__app__service__pb2.UnitAppService_unitByIdResponse.FromString,
                )
        self.units = channel.unary_unary(
                '/cafm.project.unit.UnitAppService/units',
                request_serializer=project_dot_unit__app__service__pb2.UnitAppService_unitsRequest.SerializeToString,
                response_deserializer=project_dot_unit__app__service__pb2.UnitAppService_unitsResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.unit.UnitAppService/newId',
                request_serializer=project_dot_unit__app__service__pb2.UnitAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_unit__app__service__pb2.UnitAppService_newIdResponse.FromString,
                )


class UnitAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def unitById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def units(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UnitAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'unitById': grpc.unary_unary_rpc_method_handler(
                    servicer.unitById,
                    request_deserializer=project_dot_unit__app__service__pb2.UnitAppService_unitByIdRequest.FromString,
                    response_serializer=project_dot_unit__app__service__pb2.UnitAppService_unitByIdResponse.SerializeToString,
            ),
            'units': grpc.unary_unary_rpc_method_handler(
                    servicer.units,
                    request_deserializer=project_dot_unit__app__service__pb2.UnitAppService_unitsRequest.FromString,
                    response_serializer=project_dot_unit__app__service__pb2.UnitAppService_unitsResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=project_dot_unit__app__service__pb2.UnitAppService_newIdRequest.FromString,
                    response_serializer=project_dot_unit__app__service__pb2.UnitAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.unit.UnitAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UnitAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def unitById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.unit.UnitAppService/unitById',
            project_dot_unit__app__service__pb2.UnitAppService_unitByIdRequest.SerializeToString,
            project_dot_unit__app__service__pb2.UnitAppService_unitByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def units(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.unit.UnitAppService/units',
            project_dot_unit__app__service__pb2.UnitAppService_unitsRequest.SerializeToString,
            project_dot_unit__app__service__pb2.UnitAppService_unitsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.unit.UnitAppService/newId',
            project_dot_unit__app__service__pb2.UnitAppService_newIdRequest.SerializeToString,
            project_dot_unit__app__service__pb2.UnitAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
