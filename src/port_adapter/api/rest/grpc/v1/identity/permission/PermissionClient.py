"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Permission import (
    PermissionDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.Permissions import Permissions
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.permission_app_service_pb2 import (
    PermissionAppService_permissionsResponse,
    PermissionAppService_permissionsRequest,
    PermissionAppService_permissionByIdRequest,
    PermissionAppService_permissionByIdResponse,
    PermissionAppService_newIdRequest,
    PermissionAppService_newIdResponse, PermissionAppService_idByStringRequest, PermissionAppService_idByStringResponse,
)
from src.resource.proto._generated.identity.permission_app_service_pb2_grpc import (
    PermissionAppServiceStub,
)


class PermissionClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def idByString(self, string: str) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionClient.idByString.__qualname__}] - grpc call to server {self._server}:{self._port}"
                )
                request = PermissionAppService_idByStringRequest(string=string)
                response: PermissionAppService_idByStringResponse = stub.id_by_string.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                PermissionClient.idByString.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{PermissionClient.idByString.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionClient.newId.__qualname__}] - grpc call to retrieve permissions from server {self._server}:{self._port}"
                )
                request = PermissionAppService_newIdRequest()
                response: PermissionAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                PermissionClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{PermissionClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissions(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Permissions:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionClient.permissions.__qualname__}] - grpc call to retrieve permissions from server {self._server}:{self._port}"
                )
                request = PermissionAppService_permissionsRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: PermissionAppService_permissionsResponse = (
                    stub.permissions.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    PermissionClient.permissions.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{PermissionClient.permissions.__qualname__}] - grpc response: {response}"
                )
                return Permissions(
                    permissions=[
                        self._descriptorByObject(obj=permission)
                        for permission in response[0].permissions
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def permissionById(self, permissionId) -> PermissionDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PermissionAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{PermissionClient.permissionById.__qualname__}] - grpc call to retrieve permission with permissionId: {permissionId} from server {self._server}:{self._port}"
                )
                response: PermissionAppService_permissionByIdResponse = (
                    stub.permission_by_id.with_call(
                        PermissionAppService_permissionByIdRequest(id=permissionId),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    PermissionClient.permissionById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{PermissionClient.permissionById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].permission)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> PermissionDescriptor:
        return PermissionDescriptor(
            id=obj.id,
            name=obj.name,
            allowed_actions=[x for x in obj.allowed_actions],
            denied_actions=[x for x in obj.denied_actions],
        )
