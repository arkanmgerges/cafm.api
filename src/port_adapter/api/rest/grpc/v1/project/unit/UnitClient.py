"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.unit.Unit import UnitDescriptor
from src.port_adapter.api.rest.model.response.v1.project.unit.Units import Units
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.unit_app_service_pb2 import \
    UnitAppService_unitsResponse, \
    UnitAppService_unitsRequest, UnitAppService_unitByIdRequest, \
    UnitAppService_unitByIdResponse, UnitAppService_newIdRequest, UnitAppService_newIdResponse
from src.resource.proto._generated.project.unit_app_service_pb2_grpc import UnitAppServiceStub


class UnitClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UnitAppServiceStub(channel)
            try:
                request = UnitAppService_newIdRequest()
                response: UnitAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(UnitClient.newId.__qualname__))))
                logger.debug(
                    f'[{UnitClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
            
    @OpenTelemetry.grpcTraceOTel
    def units(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Units:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UnitAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UnitClient.units.__qualname__}] - grpc call to retrieve units from server {self._server}:{self._port}')
                request = UnitAppService_unitsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: UnitAppService_unitsResponse = stub.units.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            UnitClient.units.__qualname__)),))
                logger.debug(
                    f'[{UnitClient.units.__qualname__}] - grpc response: {response}')

                return Units(units=[self._descriptorByObject(obj=unit) for unit in
                                                    response[0].units],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def unitById(self, id) -> UnitDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UnitAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UnitClient.unitById.__qualname__}] - grpc call to retrieve unit with unitId: {id} from server {self._server}:{self._port}')
                response: UnitAppService_unitByIdResponse = stub.unitById.with_call(
                    UnitAppService_unitByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            UnitClient.units.__qualname__))))
                logger.debug(
                    f'[{UnitClient.unitById.__qualname__}] - grpc response: {response}')
                unit = response[0].unit
                return self._descriptorByObject(obj=unit)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> UnitDescriptor:
        return UnitDescriptor(id=obj.id,
                                      name=obj.name,
                                      )
