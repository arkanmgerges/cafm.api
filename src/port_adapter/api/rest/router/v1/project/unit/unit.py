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
from src.port_adapter.api.rest.grpc.v1.project.unit.UnitClient import UnitClient
from src.port_adapter.api.rest.model.response.v1.project.unit.Units import Units
from src.port_adapter.api.rest.model.response.v1.project.unit.Unit import UnitDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all unit(s)', response_model=Units)
@OpenTelemetry.fastApiTraceOTel
async def getUnits(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = UnitClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.units(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUnits.__module__}.{getUnits.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{unit_id}", summary='Get unit by id',
            response_model=UnitDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getUnitById(*, unit_id: str = Path(...,
                                                                description='unit id that is used to fetch unit data'),
                               _=Depends(CustomHttpBearer())):
    """Get a unit by id
    """
    try:
        client = UnitClient()
        return client.unitById(id=unit_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUnitById.__module__}.{getUnitById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create unit', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of unit', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = UnitClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_UNIT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'id': client.newId(),
                                             'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{unit_id}", summary='Update unit', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 unit_id: str = Path(..., description='unit id that is used in order to update the unit'),
                 name: str = Body(..., description='name of name', embed=True),                 
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_UNIT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'unit_id': unit_id,
                                            'name': name,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{unit_id}", summary='Partial update unit', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdate(*, _=Depends(CustomHttpBearer()),
                        unit_id: str = Path(..., description='unit id that is used in order to update the unit'),
                        name: str = Body(..., description='name of name', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_UNIT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'unit_id': unit_id,
                                            'name': name,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{unit_id}", summary='Delete a units', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 unit_id: str = Path(..., description='unit id that is used in order to delete the unit'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_UNIT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'unit_id': unit_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
