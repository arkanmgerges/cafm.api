"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.AuthenticationApplicationService import AuthenticationApplicationService
from src.port_adapter.api.rest.grpc.Client import Client
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.auth_app_service_pb2 import \
    AuthAppService_authenticateUserByEmailAndPasswordRequest, \
    AuthAppService_authenticateUserByEmailAndPasswordResponse, AuthAppService_logoutRequest
from src.resource.proto._generated.identity.auth_app_service_pb2_grpc import AuthAppServiceStub


class AuthClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def authenticateUserByEmailAndPassword(self, email: str, password: str):
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = AuthAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{AuthClient.authenticateUserByEmailAndPassword.__qualname__}] - grpc call to authenticate user \
                    email: {email} from server {self._server}:{self._port}')
                authService: AuthenticationApplicationService = AppDi.instance.get(AuthenticationApplicationService)
                response: AuthAppService_authenticateUserByEmailAndPasswordResponse = \
                    stub.authenticateUserByEmailAndPassword.with_call(
                        AuthAppService_authenticateUserByEmailAndPasswordRequest(email=email,
                                                                                 password=authService.hashPassword(
                                                                                     password)),
                        metadata=(('auth_token', 'res-token-yumyum'), ('opentel', AppDi.instance.get(
                            OpenTelemetry).serializedContext(
                            AuthClient.authenticateUserByEmailAndPassword.__qualname__))))
                logger.debug(
                    f'[{AuthClient.authenticateUserByEmailAndPassword.__qualname__}] - grpc call to authenticate user email: {email} response: {response}')

                return response[0].token
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def isAuthenticated(self, token: str) -> bool:
        authService: AuthenticationApplicationService = AppDi.instance.get(AuthenticationApplicationService)
        return authService.isAuthenticated(token=token)

    @OpenTelemetry.grpcTraceOTel
    def logout(self, token: str) -> None:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = AuthAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{AuthClient.logout.__qualname__}] - grpc call to logout user with token: {token} from server {self._server}:{self._port}')
                stub.logout.with_call(AuthAppService_logoutRequest(token=token),
                                      metadata=(('token', token), ('opentel',
                                                                   AppDi.instance.get(OpenTelemetry).serializedContext(
                                                                       AuthClient.logout.__qualname__))))
                logger.debug(
                    f'[{AuthClient.logout.__qualname__}] - grpc call')
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
