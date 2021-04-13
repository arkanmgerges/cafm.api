"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json

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
from src.port_adapter.api.rest.grpc.v1.project.equipment.project_category.EquipmentProjectCategoryClient import \
    EquipmentProjectCategoryClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroups import \
    EquipmentCategoryGroups
from src.port_adapter.api.rest.model.response.v1.project.equipment.project_category.EquipmentProjectCategories import \
    EquipmentProjectCategories
from src.port_adapter.api.rest.model.response.v1.project.equipment.project_category.EquipmentProjectCategory import \
    EquipmentProjectCategoryDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all equipment project category(s)', response_model=EquipmentProjectCategories)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentProjectCategories(*,
                                        result_from: int = Query(0, description='Starting offset for fetching data'),
                                        result_size: int = Query(10, description='Item count to be fetched'),
                                        order: str = Query('', description='e.g. id:asc,email:desc'),
                                        _=Depends(CustomHttpBearer())):
    try:
        client = EquipmentProjectCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.equipmentProjectCategories(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentProjectCategories.__module__}.{getEquipmentProjectCategories.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{equipment_project_category_id}", summary='Get equipment project category by id',
            response_model=EquipmentProjectCategoryDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentProjectCategoryById(*, equipment_project_category_id: str = Path(...,
                                                                                       description='equipment project category id that is used to fetch equipment project category data'),
                                          _=Depends(CustomHttpBearer())):
    """Get a equipment project category by id
    """
    try:
        client = EquipmentProjectCategoryClient()
        return client.equipmentProjectCategoryById(id=equipment_project_category_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentProjectCategoryById.__module__}.{getEquipmentProjectCategoryById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create equipment project category', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createEquipmentProjectCategory(*, _=Depends(CustomHttpBearer()),
                                         name: str = Body(..., description='name of equipment project category',
                                                          embed=True),
                                         ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = EquipmentProjectCategoryClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_EQUIPMENT_PROJECT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                                'equipment_project_category_id': client.newId(),
                                                'name': name,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{equipment_project_category_id}", summary='Update equipment project category',
            status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateEquipmentProjectCategory(*, _=Depends(CustomHttpBearer()),
                                         equipment_project_category_id: str = Path(...,
                                                                                   description='equipment project category id that is used in order to update the equipment project category'),
                                         name: str = Body(..., description='name of name', embed=True),
                                         ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_PROJECT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_project_category_id': equipment_project_category_id,
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


# @router.patch("/{equipment_project_category_id}", summary='Partial update equipment project category', status_code=status.HTTP_200_OK)
# @OpenTelemetry.fastApiTraceOTel
# async def partialUpdate(*, _=Depends(CustomHttpBearer()),
#                         equipment_project_category_id: str = Path(..., description='equipment project category id that is used in order to update the equipment project category'),
#                         name: str = Body(..., description='name of name', embed=True),
#                         ):
#     reqId = RequestIdGenerator.generateId()
#     producer = AppDi.instance.get(SimpleProducer)
#     from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
#     producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_PROJECT_CATEGORY.value,
#                                         metadata=json.dumps({"token": Client.token}),
#                                         data=json.dumps(
#                                             {'equipment_project_category_id': equipment_project_category_id,
#                                             'name': name,
#                                             }),
#                                         external=[]),
#                      schema=ProjectCommand.get_schema())
#     return {"request_id": reqId}


@router.delete("/{equipment_project_category_id}", summary='Delete a equipment project categories',
               status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteEquipmentProjectCategory(*, _=Depends(CustomHttpBearer()),
                                         equipment_project_category_id: str = Path(...,
                                                                                   description='equipment project category id that is used in order to delete the equipment project category'), ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_EQUIPMENT_PROJECT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_project_category_id': equipment_project_category_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.post("/{equipment_project_category_id}/relate_to_category_group/{category_group_id}/link",
             summary='Link equipment project category and category group', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def linkEquipmentProjectCategoryToCategoryGroup(*, _=Depends(CustomHttpBearer()),
               equipment_project_category_id: str = Path(..., description='id of equipment project category'),
               category_group_id: str = Path(..., description='id of equipment category group'), ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.LINK_EQUIPMENT_PROJECT_CATEGORY_GROUP.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps({'equipment_project_category_id': equipment_project_category_id,
                                                         'category_group_id': category_group_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{equipment_project_category_id}/relate_to_category_group/{category_group_id}/unlink",
               summary='Unlink equipment project category and category group', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def unlinkEquipmentProjectCategoryFromCategoryGroup(*, _=Depends(CustomHttpBearer()),
                 equipment_project_category_id: str = Path(..., description='id of equipment project category'),
                 category_group_id: str = Path(..., description='id of equipment category group'), ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UNLINK_EQUIPMENT_PROJECT_CATEGORY_GROUP.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps({'equipment_project_category_id': equipment_project_category_id,
                                                         'category_group_id': category_group_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.get(path="/{equipment_project_category_id}/equipment_category_groups",
            summary='Get all equipment category Groups', response_model=EquipmentCategoryGroups)
@OpenTelemetry.fastApiTraceOTel
async def getCategoryGroupsByProjectCategoryId(*,
                                               equipment_project_category_id: str = Path(...,
                                                                                         description='id of equipment project category'),
                                               result_from: int = Query(0,
                                                                        description='Starting offset for fetching data'),
                                               result_size: int = Query(10, description='Item count to be fetched'),
                                               order: str = Query('', description='e.g. id:asc,email:desc'),
                                               _=Depends(CustomHttpBearer())):
    try:
        client = EquipmentProjectCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.categoryGroupsByProjectCategoryId(id=equipment_project_category_id, resultFrom=result_from,
                                                        resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getCategoryGroupsByProjectCategoryId.__module__}.{getCategoryGroupsByProjectCategoryId.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
