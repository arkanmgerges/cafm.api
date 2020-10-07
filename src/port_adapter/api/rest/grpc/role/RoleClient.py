"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.domain_model.AuthenticationService import AuthenticationService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.request.Role import Role
from src.resource.logging.logger import logger
from src.resource.proto._generated.auth_app_service_pb2 import AuthAppService_authenticateUserByNameAndPasswordRequest, \
    AuthAppService_authenticateUserByNameAndPasswordResponse, AuthAppService_isAuthenticatedResponse, \
    AuthAppService_isAuthenticatedRequest
from src.resource.proto._generated.auth_app_service_pb2_grpc import AuthAppServiceStub
from src.resource.proto._generated.role_app_service_pb2 import RoleAppService_rolesResponse, RoleAppService_rolesRequest
from src.resource.proto._generated.role_app_service_pb2_grpc import RoleAppServiceStub


class RoleClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')


    def roles(self) -> List[Role]:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}')
                response: RoleAppService_rolesResponse = stub.roles.with_call(RoleAppService_rolesRequest(resultFrom=0, resultSize=20),
                                                                              metadata=(('token', self.token),))
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc response: {response}')

                return [Role(id=role['id'], name=role['name']) for role in json.loads(response[0].response)]
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
