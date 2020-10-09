"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.request.Permission import Permission
from src.resource.logging.logger import logger
from src.resource.proto._generated.permission_app_service_pb2 import PermissionAppService_permissionsResponse, \
    PermissionAppService_permissionsRequest, PermissionAppService_permissionByIdRequest, PermissionAppService_permissionByIdResponse
from src.resource.proto._generated.permission_app_service_pb2_grpc import PermissionAppServiceStub


class PermissionClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def permissions(self, resultFrom: int = 0, resultSize: int = 10) -> List[Permission]:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionClient.permissions.__qualname__}] - grpc call to retrieve permissions from server {self._server}:{self._port}')
                response: PermissionAppService_permissionsResponse = stub.permissions.with_call(
                    PermissionAppService_permissionsRequest(resultFrom=resultFrom, resultSize=resultSize),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{PermissionClient.permissions.__qualname__}] - grpc response: {response}')

                return [Permission(id=permission.id, name=permission.name) for permission in response[0].permissions]
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def permissionById(self, permissionId) -> Permission:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionClient.permissionById.__qualname__}] - grpc call to retrieve permission with permissionId: {permissionId} from server {self._server}:{self._port}')
                response: PermissionAppService_permissionByIdResponse = stub.permissionById.with_call(
                    PermissionAppService_permissionByIdRequest(id=permissionId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{PermissionClient.permissionById.__qualname__}] - grpc response: {response}')

                return Permission(id=response[0].permission.id, name=response[0].permission.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
