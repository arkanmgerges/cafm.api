"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.UserGroup import UserGroup
from src.port_adapter.api.rest.model.response.UserGroups import UserGroups
from src.resource.logging.logger import logger
from src.resource.proto._generated.identity.user_group_app_service_pb2 import UserGroupAppService_userGroupsResponse, \
    UserGroupAppService_userGroupsRequest, UserGroupAppService_userGroupByIdRequest, \
    UserGroupAppService_userGroupByIdResponse
from src.resource.proto._generated.identity.user_group_app_service_pb2_grpc import UserGroupAppServiceStub


class UserGroupClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def userGroups(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> UserGroups:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UserGroupClient.userGroups.__qualname__}] - grpc call to retrieve userGroups from server {self._server}:{self._port}')
                request = UserGroupAppService_userGroupsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: UserGroupAppService_userGroupsResponse = stub.userGroups.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{UserGroupClient.userGroups.__qualname__}] - grpc response: {response}')

                return UserGroups(user_groups=[UserGroup(id=userGroup.id, name=userGroup.name) for userGroup in
                                              response[0].userGroups],
                                  item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def userGroupById(self, userGroupId) -> UserGroup:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{UserGroupClient.userGroupById.__qualname__}] - grpc call to retrieve userGroup with userGroupId: {userGroupId} from server {self._server}:{self._port}')
                response: UserGroupAppService_userGroupByIdResponse = stub.userGroupById.with_call(
                    UserGroupAppService_userGroupByIdRequest(id=userGroupId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{UserGroupClient.userGroupById.__qualname__}] - grpc response: {response}')

                return UserGroup(id=response[0].userGroup.id, name=response[0].userGroup.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
