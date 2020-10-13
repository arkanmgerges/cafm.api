"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.ResourceTypeApplicationService import ResourceTypeApplicationService
from src.domain_model.TokenService import TokenService
from src.domain_model.resource.exception.ResourceTypeDoesNotExistException import ResourceTypeDoesNotExistException
from src.domain_model.resource_type.ResourceType import ResourceType
from src.resource.logging.logger import logger
from src.resource.proto._generated.resource_type_app_service_pb2 import \
    ResourceTypeAppService_resourceTypeByNameResponse, ResourceTypeAppService_resourceTypesResponse, \
    ResourceTypeAppService_resourceTypeByIdResponse
from src.resource.proto._generated.resource_type_app_service_pb2_grpc import ResourceTypeAppServiceServicer


class ResourceTypeAppServiceListener(ResourceTypeAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()


    def __str__(self):
        return self.__class__.__name__

    def resourceTypeByName(self, request, context):
        try:
            resourceTypeAppService: ResourceTypeApplicationService = AppDi.instance.get(ResourceTypeApplicationService)
            resourceType: ResourceType = resourceTypeAppService.resourceTypeByName(name=request.name)
            response = ResourceTypeAppService_resourceTypeByNameResponse()
            response.resourceType.id = resourceType.id()
            response.resourceType.name = resourceType.name()
            return response
        except ResourceTypeDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('ResourceType does not exist')
            return ResourceTypeAppService_resourceTypeByNameResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.ResourceTypeResponse()

    def resourceTypes(self, request, context):
        try:
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize > 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            ownedResourceTypes = claims['resourceType'] if 'resourceType' in claims else []
            logger.debug(f'[{ResourceTypeAppServiceListener.resourceTypes.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t ownedResourceTypes {ownedResourceTypes}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}')
            resourceTypeAppService: ResourceTypeApplicationService = AppDi.instance.get(ResourceTypeApplicationService)

            resourceTypes: List[ResourceType] = resourceTypeAppService.resourceTypes(ownedResourceTypes=ownedResourceTypes, resultFrom=request.resultFrom,
                                                     resultSize=resultSize)
            response = ResourceTypeAppService_resourceTypesResponse()
            for resourceType in resourceTypes:
                response.resourceTypes.add(id=resourceType.id(), name=resourceType.name())
            logger.debug(f'[{ResourceTypeAppServiceListener.resourceTypes.__qualname__}] - response: {response}')
            return ResourceTypeAppService_resourceTypesResponse(resourceTypes=response.resourceTypes)
        except ResourceTypeDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No resourceTypes found')
            return ResourceTypeAppService_resourceTypeByNameResponse()

    def resourceTypeById(self, request, context):
        try:
            resourceTypeAppService: ResourceTypeApplicationService = AppDi.instance.get(ResourceTypeApplicationService)
            resourceType: ResourceType = resourceTypeAppService.resourceTypeById(id=request.id)
            logger.debug(f'[{ResourceTypeAppServiceListener.resourceTypeById.__qualname__}] - response: {resourceType}')
            response = ResourceTypeAppService_resourceTypeByIdResponse()
            response.resourceType.id = resourceType.id()
            response.resourceType.name = resourceType.name()
            return response
        except ResourceTypeDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('ResourceType does not exist')
            return ResourceTypeAppService_resourceTypeByIdResponse()