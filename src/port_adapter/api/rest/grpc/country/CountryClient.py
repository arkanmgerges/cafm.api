"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Country import Country
from src.port_adapter.api.rest.model.response.Countries import Countries
from src.resource.logging.logger import logger
from src.resource.proto._generated.user_app_service_pb2 import UserAppService_usersResponse, \
    UserAppService_usersRequest, UserAppService_userByIdRequest, UserAppService_userByIdResponse
from src.resource.proto._generated.user_app_service_pb2_grpc import UserAppServiceStub


class CountryClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def Countries(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Countries:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = UserAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CountryClient.Countries.__qualname__}] - grpc call to retrieve countries from server {self._server}:{self._port}')
                request = UserAppService_usersRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: UserAppService_usersResponse = stub.users.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{UserClient.users.__qualname__}] - grpc response: {response}')

                return Countries(users=[Country(id=user.id, name=user.name, first_name=user.firstName, last_name=user.lastName, 
                                         address_line_one=user.addressOne, address_line_two=user.addressTwo, 
                                         postal_code=user.postalCode, avatar_image=user.avatarImage) for user in response[0].users],
                             item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
