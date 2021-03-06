"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.UserGroup import (
    UserGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.UserGroups import UserGroups
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.user_group_app_service_pb2 import (
    UserGroupAppService_userGroupsResponse,
    UserGroupAppService_userGroupsRequest,
    UserGroupAppService_userGroupByIdRequest,
    UserGroupAppService_userGroupByIdResponse,
    UserGroupAppService_newIdRequest,
    UserGroupAppService_newIdResponse,
)
from src.resource.proto._generated.identity.user_group_app_service_pb2_grpc import (
    UserGroupAppServiceStub,
)


class UserGroupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserGroupClient.newId.__qualname__}] - grpc call to retrieve user group from server {self._server}:{self._port}"
                )
                request = UserGroupAppService_newIdRequest()
                response: UserGroupAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                UserGroupClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{UserGroupClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def userGroups(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> UserGroups:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserGroupClient.userGroups.__qualname__}] - grpc call to retrieve userGroups from server {self._server}:{self._port}"
                )
                request = UserGroupAppService_userGroupsRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: UserGroupAppService_userGroupsResponse = (
                    stub.user_groups.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    UserGroupClient.userGroups.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{UserGroupClient.userGroups.__qualname__}] - grpc response: {response}"
                )

                return UserGroups(
                    user_groups=[
                        self._descriptorByObject(obj=userGroup)
                        for userGroup in response[0].user_groups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def userGroupById(self, userGroupId) -> UserGroupDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserGroupClient.userGroupById.__qualname__}] - grpc call to retrieve userGroup with userGroupId: {userGroupId} from server {self._server}:{self._port}"
                )
                response: UserGroupAppService_userGroupByIdResponse = (
                    stub.user_group_by_id.with_call(
                        UserGroupAppService_userGroupByIdRequest(id=userGroupId),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    UserGroupClient.userGroupById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{UserGroupClient.userGroupById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].user_group)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> UserGroupDescriptor:
        return UserGroupDescriptor(id=obj.id, name=obj.name)
