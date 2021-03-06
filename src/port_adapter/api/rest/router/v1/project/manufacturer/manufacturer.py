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
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.manufacturer.ManufacturerClient import (
    ManufacturerClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.manufacturer.Manufacturer import (
    ManufacturerDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.manufacturer.Manufacturers import (
    Manufacturers,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary="Get all manufacturer(s)", response_model=Manufacturers)
@OpenTelemetry.fastApiTraceOTel
async def getManufacturers(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ManufacturerClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.manufacturers(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getManufacturers.__module__}.{getManufacturers.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/{manufacturer_id}",
    summary="Get manufacturer by id",
    response_model=ManufacturerDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getManufacturerById(
    *,
    manufacturer_id: str = Path(
        ..., description="manufacturer id that is used to fetch manufacturer data"
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a manufacturer by id"""
    try:
        client = ManufacturerClient()
        return client.manufacturerById(id=manufacturer_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getManufacturerById.__module__}.{getManufacturerById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary="Create manufacturer", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createManufacturer(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="name of manufacturer", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    client = ManufacturerClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_MANUFACTURER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "manufacturer_id": client.newId(),
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.put(
    "/{manufacturer_id}", summary="Update manufacturer", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def updateManufacturer(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    manufacturer_id: str = Path(
        ...,
        description="manufacturer id that is used in order to update the manufacturer",
    ),
    name: str = Body(..., description="name of name", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_MANUFACTURER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "manufacturer_id": manufacturer_id,
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# @router.patch("/{manufacturer_id}", summary='Partial update manufacturer', status_code=status.HTTP_200_OK)
# @OpenTelemetry.fastApiTraceOTel
# async def partialUpdate(*, _=Depends(CustomHttpBearer()),
#    __=Depends(CustomAuthorization()),
#                         manufacturer_id: str = Path(..., description='manufacturer id that is used in order to update the manufacturer'),
#                         name: str = Body(..., description='name of name', embed=True),
#                         ):
#     reqId = RequestIdGenerator.generateId()
#     producer = AppDi.instance.get(SimpleProducer)
#     from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
#     producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_MANUFACTURER.value,
#                                         metadata=json.dumps({"token": Client.token}),
#                                         data=json.dumps(
#                                             {'manufacturer_id': manufacturer_id,
#                                             'name': name,
#                                             }),
#                                         external=[]),
#                      schema=ProjectCommand.get_schema())
#     return {"request_id": reqId}


@router.delete(
    "/{manufacturer_id}",
    summary="Delete a manufacturers",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteManufacturer(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    manufacturer_id: str = Path(
        ...,
        description="manufacturer id that is used in order to delete the manufacturer",
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_MANUFACTURER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"manufacturer_id": manufacturer_id}),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
