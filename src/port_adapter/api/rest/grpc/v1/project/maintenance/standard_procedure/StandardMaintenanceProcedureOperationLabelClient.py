"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureOperationLabel import StandardMaintenanceProcedureOperationLabelDescriptor
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureOperationLabels import StandardMaintenanceProcedureOperationLabels
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_label_app_service_pb2 import \
    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse, \
    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest, StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest, \
    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse, StandardMaintenanceProcedureOperationLabelAppService_newIdResponse, \
    StandardMaintenanceProcedureOperationLabelAppService_newIdRequest
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_label_app_service_pb2_grpc import StandardMaintenanceProcedureOperationLabelAppServiceStub

class StandardMaintenanceProcedureOperationLabelClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureOperationLabelAppServiceStub(channel)
            try:
                request = StandardMaintenanceProcedureOperationLabelAppService_newIdRequest()
                response: StandardMaintenanceProcedureOperationLabelAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureOperationLabelClient.newId.__qualname__))))
                logger.debug(
                    f'[{StandardMaintenanceProcedureOperationLabelClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureOperationLabels(self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None) -> StandardMaintenanceProcedureOperationLabels:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureOperationLabelAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabels.__qualname__}] - grpc call to retrieve standardMaintenanceProcedureOperationLabels from server {self._server}:{self._port}')
                request = StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsRequest(result_from=resultFrom, result_size=resultSize)
                [request.orders.add(order_by=o["orderBy"], direction=o["direction"]) for o in orders]
                response: StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse = stub.standard_maintenance_procedure_operation_labels.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabels.__qualname__)),))
                logger.debug(
                    f'[{StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabels.__qualname__}] - grpc response: {response}')

                return StandardMaintenanceProcedureOperationLabels(standard_maintenance_procedure_operation_labels=[self._descriptorByObject(obj=standardMaintenanceProcedureOperationLabel) for standardMaintenanceProcedureOperationLabel in
                                                    response[0].standard_maintenance_procedure_operation_labels],
                                     total_item_count=response[0].total_item_count)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureOperationLabelById(self, id) -> StandardMaintenanceProcedureOperationLabelDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureOperationLabelAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabelById.__qualname__}] - grpc call to retrieve standardMaintenanceProcedureOperationLabel with standardMaintenanceProcedureOperationLabelId: {id} from server {self._server}:{self._port}')
                response: StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse = stub.standard_maintenance_procedure_operation_label_by_id.with_call(
                    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabelById.__qualname__))))
                logger.debug(
                    f'[{StandardMaintenanceProcedureOperationLabelClient.standardMaintenanceProcedureOperationLabelById.__qualname__}] - grpc response: {response}')
                standardMaintenanceProcedureOperationLabel = response[0].standard_maintenance_procedure_operation_label
                return self._descriptorByObject(obj=standardMaintenanceProcedureOperationLabel)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> StandardMaintenanceProcedureOperationLabelDescriptor:
        return StandardMaintenanceProcedureOperationLabelDescriptor(id=obj.id,
                                      label=obj.label,
                                      generate_alert=obj.generate_alert,
                                      standard_maintenance_procedure_operation_id=obj.standard_maintenance_procedure_operation_id,
                                      )