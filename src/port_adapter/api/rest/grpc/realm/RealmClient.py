"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Realm import Realm
from src.port_adapter.api.rest.model.response.Realms import Realms
from src.resource.logging.logger import logger
from src.resource.proto._generated.realm_app_service_pb2 import RealmAppService_realmsResponse, \
    RealmAppService_realmsRequest, RealmAppService_realmByIdRequest, RealmAppService_realmByIdResponse
from src.resource.proto._generated.realm_app_service_pb2_grpc import RealmAppServiceStub


class RealmClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def realms(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Realms:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RealmAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RealmClient.realms.__qualname__}] - grpc call to retrieve realms from server {self._server}:{self._port}')
                request = RealmAppService_realmsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: RealmAppService_realmsResponse = stub.realms.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{RealmClient.realms.__qualname__}] - grpc response: {response}')

                return Realms(realms=[Realm(id=realm.id, name=realm.name) for realm in response[0].realms],
                              itemCount=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def realmById(self, realmId) -> Realm:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RealmAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RealmClient.realmById.__qualname__}] - grpc call to retrieve realm with realmId: {realmId} from server {self._server}:{self._port}')
                response: RealmAppService_realmByIdResponse = stub.realmById.with_call(
                    RealmAppService_realmByIdRequest(id=realmId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{RealmClient.realmById.__qualname__}] - grpc response: {response}')

                return Realm(id=response[0].realm.id, name=response[0].realm.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
