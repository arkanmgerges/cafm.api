"""
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
from src.port_adapter.api.rest.grpc.v1.identity.ou.OuClient import OuClient
from src.port_adapter.api.rest.model.response.v1.identity.Ou import Ou
from src.port_adapter.api.rest.model.response.v1.identity.Ous import Ous
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="/", summary='Get all ous', response_model=Ous)
@OpenTelemetry.fastApiTraceOTel
async def getOus(*,
                 result_from: int = Query(0, description='Starting offset for fetching data'),
                 result_size: int = Query(10, description='Item count to be fetched'),
                 order: str = Query('', description='e.g. name:asc,age:desc'),
                 _=Depends(CustomHttpBearer())):
    try:
        client = OuClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.ous(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getOus.__module__}.{getOus.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{ou_id}/", summary='Get ou',
            response_model=Ou)
@OpenTelemetry.fastApiTraceOTel
async def getOu(*, ou_id: str = Path(...,
                                     description='Ou id that is used to fetch ou data'),
                _=Depends(CustomHttpBearer())):
    """Get a Ou by id
    """
    try:
        client = OuClient()
        return client.ouById(ouId=ou_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getOu.__module__}.{getOu.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/create", summary='Create a new ou', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the ou', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_OU.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{ou_id}", summary='Delete a ou', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 ou_id: str = Path(...,
                                   description='Ou id that is used in order to delete the ou')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_OU.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': ou_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{ou_id}", summary='Update a ou', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 ou_id: str = Path(...,
                                   description='Ou id that is used in order to delete the ou'),
                 name: str = Body(..., description='Title of the ou', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_OU.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': ou_id, 'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
