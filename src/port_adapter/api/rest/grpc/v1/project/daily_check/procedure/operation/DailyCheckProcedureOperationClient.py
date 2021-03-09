"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperation import DailyCheckProcedureOperationDescriptor
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperations import DailyCheckProcedureOperations
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.daily_check_procedure_operation_app_service_pb2 import \
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse, \
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest, \
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest, \
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse, \
    DailyCheckProcedureOperationAppService_newIdRequest, DailyCheckProcedureOperationAppService_newIdResponse
from src.resource.proto._generated.project.daily_check_procedure_operation_app_service_pb2_grpc import DailyCheckProcedureOperationAppServiceStub
from src.resource.proto._generated.project.daily_check_procedure_operation_app_service_pb2 import DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest
from src.resource.proto._generated.project.daily_check_procedure_operation_app_service_pb2 import DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse

class DailyCheckProcedureOperationClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationAppServiceStub(channel)
            try:
                request = DailyCheckProcedureOperationAppService_newIdRequest()
                response: DailyCheckProcedureOperationAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(DailyCheckProcedureOperationClient.newId.__qualname__))))
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
            
    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperations(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedureOperations:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperations from server {self._server}:{self._port}')
                request = DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse = stub.dailyCheckProcedureOperations.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedureOperations(daily_check_procedure_operations=[self._descriptorByObject(obj=dailyCheckProcedureOperation) for dailyCheckProcedureOperation in
                                                    response[0].dailyCheckProcedureOperations],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperationById(self, id) -> DailyCheckProcedureOperationDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperationById.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperation with dailyCheckProcedureOperationId: {id} from server {self._server}:{self._port}')
                response: DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse = stub.dailyCheckProcedureOperationById.with_call(
                    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__))))
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperationById.__qualname__}] - grpc response: {response}')
                dailyCheckProcedureOperation = response[0].dailyCheckProcedureOperation
                return self._descriptorByObject(obj=dailyCheckProcedureOperation)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(self, dailyCheckProcedureId: str = None, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedureOperations:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperations from server {self._server}:{self._port}')
                request = DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdRequest(dailyCheckProcedureId=dailyCheckProcedureId, resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse = stub.dailyCheckProcedureOperationsByDailyCheckProcedureId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationClient.dailyCheckProcedureOperations.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureOperationClient.dailyCheckProcedureOperationsByDailyCheckProcedureId.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedureOperations(daily_check_procedure_operations=[self._descriptorByObject(obj=dailyCheckProcedureOperation) for dailyCheckProcedureOperation in
                                                    response[0].dailyCheckProcedureOperations],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> DailyCheckProcedureOperationDescriptor:
        return DailyCheckProcedureOperationDescriptor(id=obj.id,
                                      name=obj.name,
                                      description=obj.description,
                                      type=obj.type,
                                      daily_check_procedure_id=obj.dailyCheckProcedureId,
                                      )
