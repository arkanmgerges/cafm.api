"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

import grpc

import src.port_adapter.AppDi as AppDi
from src.domain_model.AuthenticationService import AuthenticationService
from src.port_adapter.api.rest.grpc.Client import Client
from src.resource.logging.logger import logger
from src.resource.proto._generated.auth_app_service_pb2 import AuthAppService_authenticateUserByNameAndPasswordRequest, \
    AuthAppService_authenticateUserByNameAndPasswordResponse, AuthAppService_isAuthenticatedResponse, \
    AuthAppService_isAuthenticatedRequest
from src.resource.proto._generated.auth_app_service_pb2_grpc import AuthAppServiceStub


class AuthClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def authenticateUserByNameAndPassword(self, name: str, password: str):
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = AuthAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{AuthClient.authenticateUserByNameAndPassword.__qualname__}] - grpc call to authenticate user name: {name} from server {self._server}:{self._port}')
                authService: AuthenticationService = AppDi.instance.get(AuthenticationService)
                response: AuthAppService_authenticateUserByNameAndPasswordResponse = stub.authenticateUserByNameAndPassword.with_call(
                    AuthAppService_authenticateUserByNameAndPasswordRequest(name=name,
                                                                            password=authService.hashPassword(
                                                                                password)),
                    metadata=(('auth_token', 'res-token-yumyum'),))
                logger.debug(
                    f'[{AuthClient.authenticateUserByNameAndPassword.__qualname__}] - grpc call to authenticate user name: {name} response: {response}')

                return response[0].token
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def isAuthenticated(self, token: str) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = AuthAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{AuthClient.isAuthenticated.__qualname__}] - grpc call to check if the token is valid and considered as authenticated token: {token} from server {self._server}:{self._port}')
                response: AuthAppService_isAuthenticatedResponse = stub.isAuthenticated.with_call(
                    AuthAppService_isAuthenticatedRequest(token=token))
                logger.debug(
                    f'[{AuthClient.isAuthenticated.__qualname__}] - grpc response: {response}')

                return response[0].response is True
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
