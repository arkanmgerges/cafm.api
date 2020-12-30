"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Permission import Permission
from src.port_adapter.api.rest.model.response.Permissions import Permissions
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.permission_app_service_pb2 import PermissionAppService_permissionsResponse, \
    PermissionAppService_permissionsRequest, PermissionAppService_permissionByIdRequest, \
    PermissionAppService_permissionByIdResponse
from src.resource.proto._generated.identity.permission_app_service_pb2_grpc import PermissionAppServiceStub


class PermissionClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def permissions(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Permissions:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionClient.permissions.__qualname__}] - grpc call to retrieve permissions from server {self._server}:{self._port}')
                request = PermissionAppService_permissionsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: PermissionAppService_permissionsResponse = stub.permissions.with_call(
                    request,
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(PermissionClient.permissions.__qualname__))))
                logger.debug(
                    f'[{PermissionClient.permissions.__qualname__}] - grpc response: {response}')
                return Permissions(permissions=[
                    Permission(id=permission.id, name=permission.name,
                               allowed_actions=[x for x in permission.allowedActions], denied_actions=[x for x in permission.deniedActions]) for
                    permission in
                    response[0].permissions],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissionById(self, permissionId) -> Permission:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionClient.permissionById.__qualname__}] - grpc call to retrieve permission with permissionId: {permissionId} from server {self._server}:{self._port}')
                response: PermissionAppService_permissionByIdResponse = stub.permissionById.with_call(
                    PermissionAppService_permissionByIdRequest(id=permissionId),
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(PermissionClient.permissionById.__qualname__))))
                logger.debug(
                    f'[{PermissionClient.permissionById.__qualname__}] - grpc response: {response}')

                return Permission(id=response[0].permission.id, name=response[0].permission.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
