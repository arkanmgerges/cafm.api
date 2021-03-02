"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import DailyCheckProcedureOperationParameterDescriptor
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameters import DailyCheckProcedureOperationParameters
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2 import \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse, \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest, DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest, \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2_grpc import DailyCheckProcedureOperationParameterAppServiceStub
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2 import DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2 import DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse

class DailyCheckProcedureOperationParameterClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperationParameters(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedureOperationParameters:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperationParameters from server {self._server}:{self._port}')
                request = DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse = stub.dailyCheckProcedureOperationParameters.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedureOperationParameters(daily_check_procedure_operation_parameters=[self._descriptorByObject(obj=dailyCheckProcedureOperationParameter) for dailyCheckProcedureOperationParameter in
                                                    response[0].dailyCheckProcedureOperationParameters],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperationParameterById(self, id) -> DailyCheckProcedureOperationParameterDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameterById.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperationParameter with dailyCheckProcedureOperationParameterId: {id} from server {self._server}:{self._port}')
                response: DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse = stub.dailyCheckProcedureOperationParameterById.with_call(
                    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__))))
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameterById.__qualname__}] - grpc response: {response}')
                dailyCheckProcedureOperationParameter = response[0].dailyCheckProcedureOperationParameter
                return self._descriptorByObject(obj=dailyCheckProcedureOperationParameter)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(self, dailyCheckProcedureOperationId: str = None, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedureOperationParameters:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__}] - grpc call to retrieve dailyCheckProcedureOperationParameters from server {self._server}:{self._port}')
                request = DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdRequest(dailyCheckProcedureOperationId=dailyCheckProcedureOperationId, resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse = stub.dailyCheckProcedureOperationParameters.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParameters.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureOperationParameterClient.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedureOperationParameters(daily_check_procedure_operation_parameters=[self._descriptorByObject(obj=dailyCheckProcedureOperationParameter) for dailyCheckProcedureOperationParameter in
                                                    response[0].dailyCheckProcedureOperationParameters],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> DailyCheckProcedureOperationParameterDescriptor:
        return DailyCheckProcedureOperationParameterDescriptor(id=obj.id,
                                      name=obj.name,
                                      unit_id=obj.unitId,
                                      daily_check_procedure_operation_id=obj.dailyCheckProcedureOperationId,
                                      min_value=obj.minValue,
                                      max_value=obj.maxValue,
                                      )