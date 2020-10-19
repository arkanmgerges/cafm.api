"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.User import User
from src.port_adapter.api.rest.model.response.Users import Users
from src.resource.logging.logger import logger
from src.resource.proto._generated.user_app_service_pb2 import UserAppService_usersResponse, \
    UserAppService_usersRequest, UserAppService_userByIdRequest, UserAppService_userByIdResponse
from src.resource.proto._generated.user_app_service_pb2_grpc import UserAppServiceStub


class UserClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

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
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{UserClient.users.__qualname__}] - grpc response: {response}')

                return Users(users=[User(id=user.id, name=user.name) for user in response[0].users],
                             item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def userById(self, userId) -> User:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UserClient.userById.__qualname__}] - grpc call to retrieve user with userId: {userId} from server {self._server}:{self._port}')
                response: UserAppService_userByIdResponse = stub.userById.with_call(
                    UserAppService_userByIdRequest(id=userId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{UserClient.userById.__qualname__}] - grpc response: {response}')

                return User(id=response[0].user.id, name=response[0].user.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
