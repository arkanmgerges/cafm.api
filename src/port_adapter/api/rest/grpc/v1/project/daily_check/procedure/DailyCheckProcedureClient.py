"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedure import DailyCheckProcedureDescriptor
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedures import DailyCheckProcedures
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2 import \
    DailyCheckProcedureAppService_dailyCheckProceduresResponse, \
    DailyCheckProcedureAppService_dailyCheckProceduresRequest, DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest, \
    DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2_grpc import DailyCheckProcedureAppServiceStub
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2 import DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdRequest
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2 import DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdResponse

class DailyCheckProcedureClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedures(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedures:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProcedures.__qualname__}] - grpc call to retrieve dailyCheckProcedures from server {self._server}:{self._port}')
                request = DailyCheckProcedureAppService_dailyCheckProceduresRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureAppService_dailyCheckProceduresResponse = stub.dailyCheckProcedures.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureClient.dailyCheckProcedures.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProcedures.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedures(daily_check_procedures=[self._descriptorByObject(obj=dailyCheckProcedure) for dailyCheckProcedure in
                                                    response[0].dailyCheckProcedures],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureById(self, id) -> DailyCheckProcedureDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProcedureById.__qualname__}] - grpc call to retrieve dailyCheckProcedure with dailyCheckProcedureId: {id} from server {self._server}:{self._port}')
                response: DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse = stub.dailyCheckProcedureById.with_call(
                    DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureClient.dailyCheckProcedures.__qualname__))))
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProcedureById.__qualname__}] - grpc response: {response}')
                dailyCheckProcedure = response[0].dailyCheckProcedure
                return self._descriptorByObject(obj=dailyCheckProcedure)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProceduresByEquipmentId(self, equipmentId: str = None, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> DailyCheckProcedures:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProcedures.__qualname__}] - grpc call to retrieve dailyCheckProcedures from server {self._server}:{self._port}')
                request = DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdRequest(equipmentId=equipmentId, resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentIdResponse = stub.dailyCheckProcedures.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            DailyCheckProcedureClient.dailyCheckProcedures.__qualname__)),))
                logger.debug(
                    f'[{DailyCheckProcedureClient.dailyCheckProceduresByEquipmentId.__qualname__}] - grpc response: {response}')

                return DailyCheckProcedures(daily_check_procedures=[self._descriptorByObject(obj=dailyCheckProcedure) for dailyCheckProcedure in
                                                    response[0].dailyCheckProcedures],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> DailyCheckProcedureDescriptor:
        return DailyCheckProcedureDescriptor(id=obj.id,
                                      name=obj.name,
                                      description=obj.description,
                                      equipment_id=obj.equipmentId,
                                      equipment_category_group_id=obj.equipmentCategoryGroupId,
                                      )