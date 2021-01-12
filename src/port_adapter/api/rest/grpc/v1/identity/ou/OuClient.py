"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Ou import OuDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Ous import Ous
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.ou_app_service_pb2 import OuAppService_ousResponse, \
    OuAppService_ousRequest, OuAppService_ouByIdRequest, OuAppService_ouByIdResponse
from src.resource.proto._generated.identity.ou_app_service_pb2_grpc import OuAppServiceStub


class OuClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def ous(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Ous:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OuAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{OuClient.ous.__qualname__}] - grpc call to retrieve ous from server {self._server}:{self._port}')
                request = OuAppService_ousRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: OuAppService_ousResponse = stub.ous.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(OuClient.ous.__qualname__))))
                logger.debug(
                    f'[{OuClient.ous.__qualname__}] - grpc response: {response}')
                return Ous(ous=[self._descriptorByObject(obj=ou) for ou in response[0].ous],
                           item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def ouById(self, ouId) -> OuDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OuAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{OuClient.ouById.__qualname__}] - grpc call to retrieve ou with ouId: {ouId} from server {self._server}:{self._port}')
                response: OuAppService_ouByIdResponse = stub.ouById.with_call(
                    OuAppService_ouByIdRequest(id=ouId),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(OuClient.ouById.__qualname__))))
                logger.debug(
                    f'[{OuClient.ouById.__qualname__}] - grpc response: {response}')

                return self._descriptorByObject(obj=response[0].ou)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> OuDescriptor:
        return OuDescriptor(id=obj.id, name=obj.name)
