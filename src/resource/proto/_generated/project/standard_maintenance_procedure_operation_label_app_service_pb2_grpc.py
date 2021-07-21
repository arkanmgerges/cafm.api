# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import standard_maintenance_procedure_operation_label_app_service_pb2 as project_dot_standard__maintenance__procedure__operation__label__app__service__pb2


class StandardMaintenanceProcedureOperationLabelAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.standard_maintenance_procedure_operation_label_by_id = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/standard_maintenance_procedure_operation_label_by_id',
                request_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest.SerializeToString,
                response_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse.FromString,
                )
        self.standard_maintenance_procedure_operation_labels = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/standard_maintenance_procedure_operation_labels',
                request_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.SerializeToString,
                response_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/new_id',
                request_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse.FromString,
                )


class StandardMaintenanceProcedureOperationLabelAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def standard_maintenance_procedure_operation_label_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def standard_maintenance_procedure_operation_labels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StandardMaintenanceProcedureOperationLabelAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'standard_maintenance_procedure_operation_label_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_maintenance_procedure_operation_label_by_id,
                    request_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest.FromString,
                    response_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse.SerializeToString,
            ),
            'standard_maintenance_procedure_operation_labels': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_maintenance_procedure_operation_labels,
                    request_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.FromString,
                    response_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest.FromString,
                    response_serializer=project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StandardMaintenanceProcedureOperationLabelAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def standard_maintenance_procedure_operation_label_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/standard_maintenance_procedure_operation_label_by_id',
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest.SerializeToString,
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def standard_maintenance_procedure_operation_labels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/standard_maintenance_procedure_operation_labels',
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest.SerializeToString,
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def new_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_label.StandardMaintenanceProcedureOperationLabelAppService/new_id',
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdRequest.SerializeToString,
            project_dot_standard__maintenance__procedure__operation__label__app__service__pb2.StandardMaintenanceProcedureOperationLabelAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
