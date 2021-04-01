"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameterDescriptor
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameters import MaintenanceProcedureOperationParameters
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2 import \
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse, \
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest, \
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest, \
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse, \
    MaintenanceProcedureOperationParameterAppService_newIdRequest, \
    MaintenanceProcedureOperationParameterAppService_newIdResponse
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2_grpc import MaintenanceProcedureOperationParameterAppServiceStub
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2 import MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2 import MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse

class MaintenanceProcedureOperationParameterClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                request = MaintenanceProcedureOperationParameterAppService_newIdRequest()
                response: MaintenanceProcedureOperationParameterAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(MaintenanceProcedureOperationParameterClient.newId.__qualname__))))
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParameters(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> MaintenanceProcedureOperationParameters:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__}] - grpc call to retrieve maintenanceProcedureOperationParameters from server {self._server}:{self._port}')
                request = MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse = stub.maintenanceProcedureOperationParameters.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__)),))
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__}] - grpc response: {response}')

                return MaintenanceProcedureOperationParameters(maintenance_procedure_operation_parameters=[self._descriptorByObject(obj=maintenanceProcedureOperationParameter) for maintenanceProcedureOperationParameter in
                                                    response[0].maintenanceProcedureOperationParameters],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParameterById(self, id) -> MaintenanceProcedureOperationParameterDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameterById.__qualname__}] - grpc call to retrieve maintenanceProcedureOperationParameter with maintenanceProcedureOperationParameterId: {id} from server {self._server}:{self._port}')
                response: MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse = stub.maintenanceProcedureOperationParameterById.with_call(
                    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__))))
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameterById.__qualname__}] - grpc response: {response}')
                maintenanceProcedureOperationParameter = response[0].maintenanceProcedureOperationParameter
                return self._descriptorByObject(obj=maintenanceProcedureOperationParameter)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(self, maintenanceProcedureOperationId: str = None, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> MaintenanceProcedureOperationParameters:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__}] - grpc call to retrieve maintenanceProcedureOperationParameters from server {self._server}:{self._port}')
                request = MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdRequest(maintenanceProcedureOperationId=maintenanceProcedureOperationId, resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse = stub.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParameters.__qualname__)),))
                logger.debug(
                    f'[{MaintenanceProcedureOperationParameterClient.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId.__qualname__}] - grpc response: {response}')

                return MaintenanceProcedureOperationParameters(maintenance_procedure_operation_parameters=[self._descriptorByObject(obj=maintenanceProcedureOperationParameter) for maintenanceProcedureOperationParameter in
                                                    response[0].maintenanceProcedureOperationParameters],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> MaintenanceProcedureOperationParameterDescriptor:
        return MaintenanceProcedureOperationParameterDescriptor(id=obj.id,
                                      name=obj.name,
                                      unit_id=obj.unitId,
                                      maintenance_procedure_operation_id=obj.maintenanceProcedureOperationId,
                                      min_value=float(obj.minValue),
                                      max_value=float(obj.maxValue),
                                      )
