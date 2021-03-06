"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContext import (
    PermissionContextDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContexts import (
    PermissionContexts,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.permission_context_app_service_pb2 import (
    PermissionContextAppService_permissionContextsRequest,
    PermissionContextAppService_permissionContextsResponse,
    PermissionContextAppService_permissionContextByIdResponse,
    PermissionContextAppService_permissionContextByIdRequest,
    PermissionContextAppService_newIdRequest,
    PermissionContextAppService_newIdResponse, PermissionContextAppService_idByStringRequest,
    PermissionContextAppService_idByStringResponse,
)
from src.resource.proto._generated.identity.permission_context_app_service_pb2_grpc import (
    PermissionContextAppServiceStub,
)


class PermissionContextClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def idByString(self, string: str) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionContextClient.idByString.__qualname__}] - grpc call to server {self._server}:{self._port}"
                )
                request = PermissionContextAppService_idByStringRequest(string=string)
                response: PermissionContextAppService_idByStringResponse = stub.id_by_string.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                PermissionContextClient.idByString.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{PermissionContextClient.idByString.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionContextClient.newId.__qualname__}] - grpc call to retrieve permission contexts from server {self._server}:{self._port}"
                )
                request = PermissionContextAppService_newIdRequest()
                response: PermissionContextAppService_newIdResponse = (
                    stub.new_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    PermissionContextClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{PermissionContextClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissionContexts(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> PermissionContexts:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionContextClient.permissionContexts.__qualname__}] - grpc call to retrieve permission context from server {self._server}:{self._port}"
                )
                request = PermissionContextAppService_permissionContextsRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: PermissionContextAppService_permissionContextsResponse = stub.permission_contexts.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                PermissionContextClient.permissionContexts.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{PermissionContextClient.permissionContexts.__qualname__}] - grpc response: {response}"
                )

                return PermissionContexts(
                    permission_contexts=[
                        self._descriptorByObject(obj=permissionContext)
                        for permissionContext in response[0].permission_contexts
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissionContextById(self, permissionContextId) -> PermissionContextDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionContextAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionContextClient.permissionContextById.__qualname__}] - grpc call to retrieve permission context with id: {permissionContextId} from server {self._server}:{self._port}"
                )
                response: PermissionContextAppService_permissionContextByIdResponse = stub.permission_context_by_id.with_call(
                    PermissionContextAppService_permissionContextByIdRequest(
                        id=permissionContextId
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                PermissionContextClient.permissionContextById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{PermissionContextClient.permissionContextById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].permission_context)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> PermissionContextDescriptor:
        return PermissionContextDescriptor(
            id=obj.id, type=obj.type, data=json.loads(obj.data)
        )
