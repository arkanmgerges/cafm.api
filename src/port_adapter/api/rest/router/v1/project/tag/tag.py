"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)


import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.tag.TagClient import TagClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.tag.Tags import Tags
from src.port_adapter.api.rest.model.response.v1.project.tag.Tag import TagDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all tag(s)', response_model=Tags)
@OpenTelemetry.fastApiTraceOTel
async def getTags(
    *,
    result_from: int = Query(0, description='Starting offset for fetching data'),
    result_size: int = Query(10, description='Item count to be fetched'),
    orders: str = Query('', description='e.g. id:asc,email:desc'),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        client = TagClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.tags(resultFrom=result_from, resultSize=result_size, orders=orders)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getTags.__module__}.{getTags.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/{tag_id}", summary='Get tag by id',
            response_model=TagDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getTagById(
    *,
    tag_id: str = Path(
        ...,
        description='tag id that is used to fetch tag data',
    ),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    """Get a tag by id
    """
    try:
        client = TagClient()
        return client.tagById(id=tag_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getTagById.__module__}.{getTagById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create tag', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createTag(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
        name: str = Body(..., description='name of tag', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = TagClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_TAG.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'tag_id': client.newId(),
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}



@router.post("/assign_tag_to_role", summary='Assign tag to role', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createTag(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
        name: str = Body(..., description='name of tag', embed=True),
        role_id: str = Body(..., description='role id', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.ASSIGN_TAG_TO_ROLE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'role_id': role_id,
                                             'tag_name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{tag_id}", summary='Update tag', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateTag(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    tag_id: str = Path(..., description='tag id that is used in order to update the tag'),
        name: str = Body(..., description='name of tag', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_TAG.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'tag_id': tag_id,
                                            'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{tag_id}", summary='Partial update tag', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateTag(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    tag_id: str = Path(..., description='tag id that is used in order to update the tag'),
        name: str = Body(None, description='name of tag', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_TAG.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'tag_id': tag_id,
                                            'name': name,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{tag_id}", summary='Delete a tags', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteTag(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    tag_id: str = Path(
        ..., description='tag id that is used in order to delete the tag'
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_TAG.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'tag_id': tag_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}