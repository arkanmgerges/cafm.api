"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.HasUserPasswordSet import HasUserPasswordSetDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Users import Users
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.user_app_service_pb2 import (
    UserAppService_usersResponse,
    UserAppService_usersRequest,
    UserAppService_userByIdRequest,
    UserAppService_userByIdResponse,
    UserAppService_newIdRequest, UserAppService_hasUserPasswordSetRequest, UserAppService_hasUserPasswordSetResponse,
)
from src.resource.proto._generated.identity.user_app_service_pb2_grpc import (
    UserAppServiceStub,
)


class UserClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserClient.newId.__qualname__}] - grpc call to retrieve users from server {self._server}:{self._port}"
                )
                request = UserAppService_newIdRequest()
                response: UserAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                UserClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{UserClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def hasUserPasswordSet(self, userId) -> HasUserPasswordSetDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserClient.hasUserPasswordSet.__qualname__}] - grpc call to {self._server}:{self._port}"
                )
                request = UserAppService_hasUserPasswordSetRequest(user_id=userId)
                response: UserAppService_hasUserPasswordSetResponse = stub.has_user_password_set.with_call(
                    request,
                    metadata=(
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                UserClient.hasUserPasswordSet.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{UserClient.hasUserPasswordSet.__qualname__}] - grpc response: {response}"
                )
                return HasUserPasswordSetDescriptor(result=response[0].has_user_password_set)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def users(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Users:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserClient.users.__qualname__}] - grpc call to retrieve users from server {self._server}:{self._port}"
                )
                request = UserAppService_usersRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: UserAppService_usersResponse = stub.users.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                UserClient.users.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{UserClient.users.__qualname__}] - grpc response: {response}"
                )

                return Users(
                    users=[
                        self._descriptorByObject(obj=user) for user in response[0].users
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def userById(self, userId) -> UserDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserClient.userById.__qualname__}] - grpc call to retrieve user with userId: {userId} from server {self._server}:{self._port}"
                )
                response: UserAppService_userByIdResponse = stub.user_by_id.with_call(
                    UserAppService_userByIdRequest(id=userId),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                UserClient.users.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{UserClient.userById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].user)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> UserDescriptor:
        return UserDescriptor(id=obj.id, email=obj.email)
