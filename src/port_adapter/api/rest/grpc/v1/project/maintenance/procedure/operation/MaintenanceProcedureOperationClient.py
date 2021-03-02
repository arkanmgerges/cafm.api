"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.MaintenanceProcedureOperation import MaintenanceProcedureOperationDescriptor
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.MaintenanceProcedureOperations import MaintenanceProcedureOperations
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.maintenance_procedure_operation_app_service_pb2 import \
    MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse, \
    MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest, MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest, \
    MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse
from src.resource.proto._generated.project.maintenance_procedure_operation_app_service_pb2_grpc import MaintenanceProcedureOperationAppServiceStub
from src.resource.proto._generated.project.maintenance_procedure_operation_app_service_pb2 import MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest
from src.resource.proto._generated.project.maintenance_procedure_operation_app_service_pb2 import MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse

class MaintenanceProcedureOperationClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperations(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> MaintenanceProcedureOperations:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__}] - grpc call to retrieve maintenanceProcedureOperations from server {self._server}:{self._port}')
                request = MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse = stub.maintenanceProcedureOperations.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__)),))
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__}] - grpc response: {response}')

                return MaintenanceProcedureOperations(maintenance_procedure_operations=[self._descriptorByObject(obj=maintenanceProcedureOperation) for maintenanceProcedureOperation in
                                                    response[0].maintenanceProcedureOperations],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationById(self, id) -> MaintenanceProcedureOperationDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperationById.__qualname__}] - grpc call to retrieve maintenanceProcedureOperation with maintenanceProcedureOperationId: {id} from server {self._server}:{self._port}')
                response: MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse = stub.maintenanceProcedureOperationById.with_call(
                    MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__))))
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperationById.__qualname__}] - grpc response: {response}')
                maintenanceProcedureOperation = response[0].maintenanceProcedureOperation
                return self._descriptorByObject(obj=maintenanceProcedureOperation)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationsByMaintenanceProcedureId(self, maintenanceProcedureId: str = None, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> MaintenanceProcedureOperations:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = MaintenanceProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__}] - grpc call to retrieve maintenanceProcedureOperations from server {self._server}:{self._port}')
                request = MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest(maintenanceProcedureId=maintenanceProcedureId, resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse = stub.maintenanceProcedureOperations.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            MaintenanceProcedureOperationClient.maintenanceProcedureOperations.__qualname__)),))
                logger.debug(
                    f'[{MaintenanceProcedureOperationClient.maintenanceProcedureOperationsByMaintenanceProcedureId.__qualname__}] - grpc response: {response}')

                return MaintenanceProcedureOperations(maintenance_procedure_operations=[self._descriptorByObject(obj=maintenanceProcedureOperation) for maintenanceProcedureOperation in
                                                    response[0].maintenanceProcedureOperations],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> MaintenanceProcedureOperationDescriptor:
        return MaintenanceProcedureOperationDescriptor(id=obj.id,
                                      name=obj.name,
                                      description=obj.description,
                                      type=obj.type,
                                      maintenance_procedure_id=obj.maintenanceProcedureId,
                                      )