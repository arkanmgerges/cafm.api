"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Role import Role
from src.port_adapter.api.rest.model.response.Roles import Roles
from src.resource.logging.logger import logger
from src.resource.proto._generated.role_app_service_pb2 import RoleAppService_rolesResponse, \
    RoleAppService_rolesRequest, RoleAppService_roleByIdRequest, RoleAppService_roleByIdResponse
from src.resource.proto._generated.role_app_service_pb2_grpc import RoleAppServiceStub


class RoleClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def roles(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Roles:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}')
                request = RoleAppService_rolesRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: RoleAppService_rolesResponse = stub.roles.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{RoleClient.roles.__qualname__}] - grpc response: {response}')

                return Roles(roles=[Role(id=role.id, name=role.name) for role in response[0].roles],
                             item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def roleById(self, roleId) -> Role:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{RoleClient.roleById.__qualname__}] - grpc call to retrieve role with roleId: {roleId} from server {self._server}:{self._port}')
                response: RoleAppService_roleByIdResponse = stub.roleById.with_call(
                    RoleAppService_roleByIdRequest(id=roleId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{RoleClient.roleById.__qualname__}] - grpc response: {response}')

                return Role(id=response[0].role.id, name=response[0].role.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
