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
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.standard_category.StandardEquipmentCategoryClient import \
    StandardEquipmentCategoryClient
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.StandardEquipmentCategories import \
    StandardEquipmentCategories
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.StandardEquipmentCategory import \
    StandardEquipmentCategoryDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

router = APIRouter()


@router.get(path="", summary='Get all standard equipment category(s)', response_model=StandardEquipmentCategories)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentCategories(*,
                                         result_from: int = Query(0, description='Starting offset for fetching data'),
                                         result_size: int = Query(10, description='Item count to be fetched'),
                                         order: str = Query('', description='e.g. id:asc,email:desc'),
                                         _=Depends(CustomHttpBearer())):
    try:
        client = StandardEquipmentCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.standardEquipmentCategories(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getStandardEquipmentCategories.__module__}.{getStandardEquipmentCategories.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{standard_equipment_category_id}", summary='Get standard equipment category by id',
            response_model=StandardEquipmentCategoryDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentCategoryById(*, standard_equipment_category_id: str = Path(...,
                                                                                         description='standard equipment category id that is used to fetch standard equipment category data'),
                                           _=Depends(CustomHttpBearer())):
    """Get a standard equipment category by id
    """
    try:
        client = StandardEquipmentCategoryClient()
        return client.standardEquipmentCategoryById(id=standard_equipment_category_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getStandardEquipmentCategoryById.__module__}.{getStandardEquipmentCategoryById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create standard equipment category', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createStandardEquipmentCategory(*, _=Depends(CustomHttpBearer()),
                                          name: str = Body(..., description='name of standard equipment category',
                                                           embed=True),
                                          ):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    client = StandardEquipmentCategoryClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_STANDARD_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                                'standard_equipment_category_id': client.newId(),
                                                'name': name,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{standard_equipment_category_id}", summary='Update standard equipment category',
            status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateStandardEquipmentCategory(*, _=Depends(CustomHttpBearer()),
                                          standard_equipment_category_id: str = Path(...,
                                                                                     description='standard equipment category id that is used in order to update the standard equipment category'),
                                          name: str = Body(..., description='name of name', embed=True),
                                          ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_STANDARD_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_equipment_category_id': standard_equipment_category_id,
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{standard_equipment_category_id}", summary='Partial update standard equipment category',
              status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateStandardEquipmentCategory(*, _=Depends(CustomHttpBearer()),
                                                 standard_equipment_category_id: str = Path(...,
                                                                                            description='standard equipment category id that is used in order to update the standard equipment category'),
                                                 name: str = Body(None, description='name of name', embed=True),
                                                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_STANDARD_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_equipment_category_id': standard_equipment_category_id,
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{standard_equipment_category_id}", summary='Delete a standard equipment categories',
               status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteStandardEquipmentCategory(*, _=Depends(CustomHttpBearer()),
                                          standard_equipment_category_id: str = Path(...,
                                                                                     description='standard equipment category id that is used in order to delete the standard equipment category'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_STANDARD_EQUIPMENT_CATEGORY.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_equipment_category_id': standard_equipment_category_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
