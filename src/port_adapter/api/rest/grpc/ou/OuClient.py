"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Ou import Ou
from src.port_adapter.api.rest.model.response.Ous import Ous
from src.resource.logging.logger import logger
from src.resource.proto._generated.ou_app_service_pb2 import OuAppService_ousResponse, \
    OuAppService_ousRequest, OuAppService_ouByIdRequest, OuAppService_ouByIdResponse
from src.resource.proto._generated.ou_app_service_pb2_grpc import OuAppServiceStub


class OuClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

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
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{OuClient.ous.__qualname__}] - grpc response: {response}')

                return Ous(ous=[Ou(id=ou.id, name=ou.name) for ou in response[0].ous],
                           itemCount=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def ouById(self, ouId) -> Ou:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OuAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{OuClient.ouById.__qualname__}] - grpc call to retrieve ou with ouId: {ouId} from server {self._server}:{self._port}')
                response: OuAppService_ouByIdResponse = stub.ouById.with_call(
                    OuAppService_ouByIdRequest(id=ouId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{OuClient.ouById.__qualname__}] - grpc response: {response}')

                return Ou(id=response[0].ou.id, name=response[0].ou.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
