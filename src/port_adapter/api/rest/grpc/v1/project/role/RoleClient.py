"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor
from src.port_adapter.api.rest.model.response.v1.project.role.Roles import Roles
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.role_app_service_pb2 import (
    RoleAppService_rolesByTagNameRequest,
    RoleAppService_rolesByTagNameResponse,
    RoleAppService_rolesResponse,
    RoleAppService_rolesRequest,
    RoleAppService_roleByIdRequest,
    RoleAppService_roleByIdResponse,
    RoleAppService_roleByNameRequest,
    RoleAppService_roleByNameResponse,
    RoleAppService_newIdResponse,
    RoleAppService_rolesByOrganizationTypeRequest,
    RoleAppService_rolesByOrganizationTypeResponse,
    RoleAppService_newIdRequest,
)
from src.resource.proto._generated.project.role_app_service_pb2_grpc import (
    RoleAppServiceStub,
)


class RoleClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                request = RoleAppService_newIdRequest()
                response: RoleAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roles(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Roles:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roles.__qualname__}] - grpc call to retrieve roles from server {self._server}:{self._port}"
                )
                request = RoleAppService_rolesRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: RoleAppService_rolesResponse = stub.roles.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roles.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.roles.__qualname__}] - grpc response: {response}"
                )

                return Roles(
                    roles=[
                        self._descriptorByObject(obj=role) for role in response[0].roles
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def rolesByOrganizationType(
        self,
        organizationType: str = None,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> Roles:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.rolesByOrganizationType.__qualname__}] - grpc call to retrieve roles by organization type from server {self._server}:{self._port}"
                )
                request = RoleAppService_rolesByOrganizationTypeRequest(
                    organization_type=organizationType,
                    result_from=resultFrom,
                    result_size=resultSize,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: RoleAppService_rolesByOrganizationTypeResponse = (
                    stub.roles_by_organization_type.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    RoleClient.rolesByOrganizationType.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{RoleClient.rolesByOrganizationType.__qualname__}] - grpc response: {response}"
                )

                return Roles(
                    roles=[
                        self._descriptorByObject(obj=role) for role in response[0].roles
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def rolesByTagName(
        self,
        tagName: str = None,
    ) -> Roles:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.rolesByTagName.__qualname__}] - grpc call to retrieve roles by organization type from server {self._server}:{self._port}"
                )
                request = RoleAppService_rolesByTagNameRequest(
                    tag_name=tagName,
                )

                response: RoleAppService_rolesByTagNameResponse = (
                    stub.roles_by_tag_name.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    RoleClient.rolesByTagName.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{RoleClient.rolesByTagName.__qualname__}] - grpc response: {response}"
                )

                return Roles(
                    roles=[
                        self._descriptorByObject(obj=role) for role in response[0].roles
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleById(self, id) -> RoleDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roleById.__qualname__}] - grpc call to retrieve role with roleId: {id} from server {self._server}:{self._port}"
                )
                response: RoleAppService_roleByIdResponse = stub.role_by_id.with_call(
                    RoleAppService_roleByIdRequest(id=id),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roleById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.roleById.__qualname__}] - grpc response: {response}"
                )
                role = response[0].role
                return self._descriptorByObject(obj=role)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def roleByName(self, role_name) -> RoleDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RoleClient.roleByName.__qualname__}] - grpc call to retrieve role with roleId: {role_name} from server {self._server}:{self._port}"
                )
                response: RoleAppService_roleByNameResponse = stub.role_by_name.with_call(
                    RoleAppService_roleByNameRequest(name=role_name),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RoleClient.roleByName.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RoleClient.roleByName.__qualname__}] - grpc response: {response}"
                )
                role = response[0].role
                return self._descriptorByObject(obj=role)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> RoleDescriptor:
        return RoleDescriptor(
            id=obj.id,
            name=obj.name,
            title=obj.title,
        )
