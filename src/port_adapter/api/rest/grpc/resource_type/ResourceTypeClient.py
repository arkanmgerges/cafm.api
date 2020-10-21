"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.ResourceType import ResourceType
from src.port_adapter.api.rest.model.response.ResourceTypes import ResourceTypes
from src.resource.logging.logger import logger
from src.resource.proto._generated.resource_type_app_service_pb2 import ResourceTypeAppService_resourceTypesResponse, \
    ResourceTypeAppService_resourceTypesRequest, ResourceTypeAppService_resourceTypeByIdRequest, \
    ResourceTypeAppService_resourceTypeByIdResponse
from src.resource.proto._generated.resource_type_app_service_pb2_grpc import ResourceTypeAppServiceStub


class ResourceTypeClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def resourceTypes(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> ResourceTypes:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ResourceTypeAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ResourceTypeClient.resourceTypes.__qualname__}] - grpc call to retrieve resourceTypes from server {self._server}:{self._port}')
                request = ResourceTypeAppService_resourceTypesRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: ResourceTypeAppService_resourceTypesResponse = stub.resourceTypes.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{ResourceTypeClient.resourceTypes.__qualname__}] - grpc response: {response}')

                return ResourceTypes(
                    resource_types=[ResourceType(id=resourceType.id, name=resourceType.name) for resourceType in
                                   response[0].resourceTypes],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def resourceTypeById(self, resourceTypeId) -> ResourceType:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ResourceTypeAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ResourceTypeClient.resourceTypeById.__qualname__}] - grpc call to retrieve resourceType with resourceTypeId: {resourceTypeId} from server {self._server}:{self._port}')
                response: ResourceTypeAppService_resourceTypeByIdResponse = stub.resourceTypeById.with_call(
                    ResourceTypeAppService_resourceTypeByIdRequest(id=resourceTypeId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{ResourceTypeClient.resourceTypeById.__qualname__}] - grpc response: {response}')

                return ResourceType(id=response[0].resourceType.id, name=response[0].resourceType.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
