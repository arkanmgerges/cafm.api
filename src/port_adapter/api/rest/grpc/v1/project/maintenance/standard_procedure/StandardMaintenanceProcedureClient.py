"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedure import StandardMaintenanceProcedureDescriptor
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedures import StandardMaintenanceProcedures
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_maintenance_procedure_app_service_pb2 import \
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse, \
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest, StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest, \
    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse, StandardMaintenanceProcedureAppService_newIdResponse, \
    StandardMaintenanceProcedureAppService_newIdRequest
from src.resource.proto._generated.project.standard_maintenance_procedure_app_service_pb2_grpc import StandardMaintenanceProcedureAppServiceStub

class StandardMaintenanceProcedureClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureAppServiceStub(channel)
            try:
                request = StandardMaintenanceProcedureAppService_newIdRequest()
                response: StandardMaintenanceProcedureAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureClient.newId.__qualname__))))
                logger.debug(
                    f'[{StandardMaintenanceProcedureClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedures(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> StandardMaintenanceProcedures:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{StandardMaintenanceProcedureClient.standardMaintenanceProcedures.__qualname__}] - grpc call to retrieve standardMaintenanceProcedures from server {self._server}:{self._port}')
                request = StandardMaintenanceProcedureAppService_standardMaintenanceProceduresRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse = stub.standardMaintenanceProcedures.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureClient.standardMaintenanceProcedures.__qualname__)),))
                logger.debug(
                    f'[{StandardMaintenanceProcedureClient.standardMaintenanceProcedures.__qualname__}] - grpc response: {response}')

                return StandardMaintenanceProcedures(standard_maintenance_procedures=[self._descriptorByObject(obj=standardMaintenanceProcedure) for standardMaintenanceProcedure in
                                                    response[0].standardMaintenanceProcedures],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureById(self, id) -> StandardMaintenanceProcedureDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = StandardMaintenanceProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{StandardMaintenanceProcedureClient.standardMaintenanceProcedureById.__qualname__}] - grpc call to retrieve standardMaintenanceProcedure with standardMaintenanceProcedureId: {id} from server {self._server}:{self._port}')
                response: StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse = stub.standardMaintenanceProcedureById.with_call(
                    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            StandardMaintenanceProcedureClient.standardMaintenanceProcedureById.__qualname__))))
                logger.debug(
                    f'[{StandardMaintenanceProcedureClient.standardMaintenanceProcedureById.__qualname__}] - grpc response: {response}')
                standardMaintenanceProcedure = response[0].standardMaintenanceProcedure
                return self._descriptorByObject(obj=standardMaintenanceProcedure)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> StandardMaintenanceProcedureDescriptor:
        return StandardMaintenanceProcedureDescriptor(id=obj.id,
                                      name=obj.name,
                                      type=obj.type,
                                      subtype=obj.subtype,
                                      frequency=obj.frequency,
                                      start_date=obj.startDate,
                                      organization_id=obj.organizationId,
                                      standard_equipment_category_group_id=obj.standardEquipmentCategoryGroupId,
                                      )
