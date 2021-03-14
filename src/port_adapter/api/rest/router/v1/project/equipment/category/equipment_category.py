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
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.equipment.category.EquipmentCategoryClient import EquipmentCategoryClient
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.EquipmentCategories import EquipmentCategories
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.EquipmentCategory import EquipmentCategoryDescriptor
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroups import EquipmentCategoryGroups
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all equipment category(s)', response_model=EquipmentCategories)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentCategories(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = EquipmentCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.equipmentCategories(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentCategories.__module__}.{getEquipmentCategories.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{equipment_category_id}", summary='Get equipment category by id',
            response_model=EquipmentCategoryDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentCategoryById(*, equipment_category_id: str = Path(...,
                                                                description='equipment category id that is used to fetch equipment category data'),
                               _=Depends(CustomHttpBearer())):
    """Get a equipment category by id
    """
    try:
        client = EquipmentCategoryClient()
        return client.equipmentCategoryById(id=equipment_category_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentCategoryById.__module__}.{getEquipmentCategoryById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create equipment category', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of equipment category', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = EquipmentCategoryClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'id': client.newId(),
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{equipment_category_id}", summary='Update equipment category', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 equipment_category_id: str = Path(..., description='equipment category id that is used in order to update the equipment category'),
                 name: str = Body(..., description='name of name', embed=True),                 
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_category_id': equipment_category_id,
                                            'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


# @router.patch("/{equipment_category_id}", summary='Partial update equipment category', status_code=status.HTTP_200_OK)
# @OpenTelemetry.fastApiTraceOTel
# async def partialUpdate(*, _=Depends(CustomHttpBearer()),
#                         equipment_category_id: str = Path(..., description='equipment category id that is used in order to update the equipment category'),
#                         name: str = Body(..., description='name of name', embed=True),
#                         ):
#     reqId = str(uuid4())
#     producer = AppDi.instance.get(SimpleProducer)
#     from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
#     producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_CATEGORY.value,
#                                         metadata=json.dumps({"token": Client.token}),
#                                         data=json.dumps(
#                                             {'equipment_category_id': equipment_category_id,
#                                             'name': name,
#                                             }),
#                                         external=[]),
#                      schema=ProjectCommand.get_schema())
#     return {"request_id": reqId}


@router.delete("/{equipment_category_id}", summary='Delete a equipment categories', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 equipment_category_id: str = Path(..., description='equipment category id that is used in order to delete the equipment category'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_category_id': equipment_category_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.get(path="/{equipment_category_id}/equipment_category_groups",
            summary='Get equipment category groups by equipment category id',
            response_model=EquipmentCategoryGroups)
@OpenTelemetry.fastApiTraceOTel
async def getCategoryGroupsByCategoryId(*, equipment_category_id: str = Path(...,
                                                                             description='equipment category id that is used to fetch equipment category groups'),
                                        result_from: int = Query(0,
                                                                 description='Starting offset for fetching data'),
                                        result_size: int = Query(10, description='Item count to be fetched'),
                                        order: str = Query('', description='e.g. id:asc,email:desc'),
                                        _=Depends(CustomHttpBearer())):
    """Get a equipment category groups by equipment category id
    """
    try:
        client = EquipmentCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.categoryGroupsByCategoryId(id=equipment_category_id, resultFrom=result_from,
                                                 resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getCategoryGroupsByCategoryId.__module__}.{getCategoryGroupsByCategoryId.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
