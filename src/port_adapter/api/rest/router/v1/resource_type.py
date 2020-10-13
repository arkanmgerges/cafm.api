"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.resource_type.ResourceTypeClient import ResourceTypeClient
from src.port_adapter.api.rest.model.response.ResourceType import ResourceType
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all resource types', response_model=List[ResourceType])
async def getResourceTypes(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                           result_size: int = Query(10, description='Item count to be fetched'),
                           _=Depends(CustomHttpBearer())):
    try:
        client = ResourceTypeClient()
        return client.resourceTypes(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getResourceTypes.__module__}.{getResourceTypes.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{resource_type_id}/", summary='Get resource type',
            response_model=ResourceType)
async def getResourceType(*, resource_type_id: str = Path(...,
                                                         description='Resource type id that is used to fetch resource type data'),
                          _=Depends(CustomHttpBearer())):
    try:
        client = ResourceTypeClient()
        return client.resourceTypeById(resourceTypeId=resource_type_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getResourceType.__module__}.{getResourceType.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/create", summary='Create a new resource type', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the resource type', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_RESOURCE_TYPE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{resource_type_id}", summary='Delete a resource type', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 resource_type_id: str = Path(...,
                                             description='ResourceType id that is used in order to delete the resource type')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_RESOURCE_TYPE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': resource_type_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{resource_type_id}", summary='Update a resource type', status_code=status.HTTP_200_OK)
async def update(*, _=Depends(CustomHttpBearer()),
                 resource_type_id: str = Path(...,
                                             description='Resource type id that is used in order to delete the resource type'),
                 name: str = Body(..., description='Title of the resource type', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_RESOURCE_TYPE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': resource_type_id, 'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
