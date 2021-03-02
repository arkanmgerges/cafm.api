# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import daily_check_procedure_app_service_pb2 as project_dot_daily__check__procedure__app__service__pb2


class DailyCheckProcedureAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.dailyCheckProcedureById = channel.unary_unary(
                '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProcedureById',
                request_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest.SerializeToString,
                response_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse.FromString,
                )
        self.dailyCheckProcedures = channel.unary_unary(
                '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProcedures',
                request_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresRequest.SerializeToString,
                response_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresResponse.FromString,
                )
        self.dailyCheckProceduresByEquipmentId = channel.unary_unary(
                '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProceduresByEquipmentId',
                request_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdRequest.SerializeToString,
                response_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdResponse.FromString,
                )


class DailyCheckProcedureAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def dailyCheckProcedureById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dailyCheckProcedures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dailyCheckProceduresByEquipmentId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DailyCheckProcedureAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'dailyCheckProcedureById': grpc.unary_unary_rpc_method_handler(
                    servicer.dailyCheckProcedureById,
                    request_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest.FromString,
                    response_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse.SerializeToString,
            ),
            'dailyCheckProcedures': grpc.unary_unary_rpc_method_handler(
                    servicer.dailyCheckProcedures,
                    request_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresRequest.FromString,
                    response_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresResponse.SerializeToString,
            ),
            'dailyCheckProceduresByEquipmentId': grpc.unary_unary_rpc_method_handler(
                    servicer.dailyCheckProceduresByEquipmentId,
                    request_deserializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdRequest.FromString,
                    response_serializer=project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.daily_check_procedure.DailyCheckProcedureAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DailyCheckProcedureAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def dailyCheckProcedureById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProcedureById',
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest.SerializeToString,
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dailyCheckProcedures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProcedures',
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresRequest.SerializeToString,
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dailyCheckProceduresByEquipmentId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.daily_check_procedure.DailyCheckProcedureAppService/dailyCheckProceduresByEquipmentId',
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdRequest.SerializeToString,
            project_dot_daily__check__procedure__app__service__pb2.DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
