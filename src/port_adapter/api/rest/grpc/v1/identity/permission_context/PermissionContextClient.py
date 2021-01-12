"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContext import PermissionContextDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContexts import PermissionContexts
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.permission_context_app_service_pb2 import \
    PermissionContextAppService_permissionContextsRequest, PermissionContextAppService_permissionContextsResponse, \
    PermissionContextAppService_permissionContextByIdResponse, PermissionContextAppService_permissionContextByIdRequest
from src.resource.proto._generated.identity.permission_context_app_service_pb2_grpc import \
    PermissionContextAppServiceStub


class PermissionContextClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def permissionContexts(self, resultFrom: int = 0, resultSize: int = 10,
                           order: List[dict] = None) -> PermissionContexts:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionContextClient.permissionContexts.__qualname__}] - grpc call to retrieve permission context from server {self._server}:{self._port}')
                request = PermissionContextAppService_permissionContextsRequest(resultFrom=resultFrom,
                                                                                resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: PermissionContextAppService_permissionContextsResponse = stub.permissionContexts.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        PermissionContextClient.permissionContexts.__qualname__))))
                logger.debug(
                    f'[{PermissionContextClient.permissionContexts.__qualname__}] - grpc response: {response}')

                return PermissionContexts(
                    permission_contexts=[
                        self._descriptorByObject(obj=permissionContext) for permissionContext in
                        response[0].permissionContexts],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissionContextById(self, permissionContextId) -> PermissionContextDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{PermissionContextClient.permissionContextById.__qualname__}] - grpc call to retrieve permission context with id: {permissionContextId} from server {self._server}:{self._port}')
                response: PermissionContextAppService_permissionContextByIdResponse = stub.permissionContextById.with_call(
                    PermissionContextAppService_permissionContextByIdRequest(id=permissionContextId),
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        PermissionContextClient.permissionContextById.__qualname__))))
                logger.debug(
                    f'[{PermissionContextClient.permissionContextById.__qualname__}] - grpc response: {response}')

                return self._descriptorByObject(obj=response[0].permissionContext)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> PermissionContextDescriptor:
        return PermissionContextDescriptor(id=obj.id, type=obj.type, data=json.loads(obj.data))
