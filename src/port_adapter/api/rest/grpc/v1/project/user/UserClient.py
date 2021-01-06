"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.User import User, UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Users import Users
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.user_app_service_pb2 import UserAppService_usersResponse, \
    UserAppService_usersRequest, UserAppService_userByIdRequest, UserAppService_userByIdResponse, \
    UserAppService_userByEmailRequest, UserAppService_userByEmailResponse
from src.resource.proto._generated.project.user_app_service_pb2_grpc import UserAppServiceStub


class UserClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def users(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Users:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UserClient.users.__qualname__}] - grpc call to retrieve users from server {self._server}:{self._port}')
                request = UserAppService_usersRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: UserAppService_usersResponse = stub.users.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(UserClient.users.__qualname__)),))
                logger.debug(
                    f'[{UserClient.users.__qualname__}] - grpc response: {response}')

                return Users(users=[User(id=user.id, email=user.email,
                                         first_name=user.firstName, last_name=user.lastName,
                                         address_line_one=user.addressOne, address_line_two=user.addressTwo,
                                         postal_code=user.postalCode, avatar_image=user.avatarImage
                                         )
                                    for user in response[0].users],
                             item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def userById(self, id) -> UserDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UserClient.userById.__qualname__}] - grpc call to retrieve user with userId: {id} from server {self._server}:{self._port}')
                response: UserAppService_userByIdResponse = stub.userById.with_call(
                    UserAppService_userByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(UserClient.users.__qualname__))))
                logger.debug(
                    f'[{UserClient.userById.__qualname__}] - grpc response: {response}')
                user = response[0].user
                return User(id=user.id, email=user.email,
                            first_name=user.firstName, last_name=user.lastName,
                            address_line_one=user.addressOne, address_line_two=user.addressTwo,
                            postal_code=user.postalCode, avatar_image=user.avatarImage
                            )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

