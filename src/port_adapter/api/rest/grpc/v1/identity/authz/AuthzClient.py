"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.HashedKey import HashedKey
from src.port_adapter.api.rest.model.response.v1.identity.HashedKeys import HashedKeys
from src.port_adapter.api.rest.router.v1.util.UnhashedKeys import UnhashedKeys
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.authz_app_service_pb2 import AuthzAppService_hashKeysResponse, \
    AuthzAppService_hashKeysRequest
from src.resource.proto._generated.identity.authz_app_service_pb2_grpc import AuthzAppServiceStub
from src.resource.proto._generated.identity.unhashed_key_pb2 import UnhashedKey


class AuthzClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def hashKeys(self, unhashedKeys: UnhashedKeys) -> HashedKeys:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = AuthzAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{AuthzClient.hashKeys.__qualname__}] - grpc call to hash keys')
                response: AuthzAppService_hashKeysResponse = \
                    stub.hashKeys.with_call(
                        AuthzAppService_hashKeysRequest(keys=[UnhashedKey(key=x.key) for x in unhashedKeys.keys]),
                        metadata=(('auth_token', ''), ('opentel', AppDi.instance.get(
                            OpenTelemetry).serializedContext(
                            AuthzClient.hashKeys.__qualname__))))
                logger.debug(
                    f'[{AuthzClient.hashKeys.__qualname__}] - grpc call to hash keys')

                return HashedKeys(hashed_keys=[HashedKey(key=x.key, hash_code=x.hashCode)
                                               for x in response[0].hashedKeys],
                           item_count=len(response[0].hashedKeys))
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
