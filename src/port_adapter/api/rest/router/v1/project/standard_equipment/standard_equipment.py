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
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.StandardEquipmentClient import (
    StandardEquipmentClient,
)
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.StandardEquipments import (
    StandardEquipments,
)
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.StandardEquipment import (
    StandardEquipmentDescriptor,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="", summary="Get all standard equipment(s)", response_model=StandardEquipments
)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipments(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = StandardEquipmentClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.standardEquipments(
            resultFrom=result_from, resultSize=result_size, order=order
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getStandardEquipments.__module__}.{getStandardEquipments.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/{standard_equipment_id}",
    summary="Get standard equipment by id",
    response_model=StandardEquipmentDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentById(
    *,
    standard_equipment_id: str = Path(
        ...,
        description="standard equipment id that is used to fetch standard equipment data",
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a standard equipment by id"""
    try:
        client = StandardEquipmentClient()
        return client.standardEquipmentById(id=standard_equipment_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getStandardEquipmentById.__module__}.{getStandardEquipmentById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary="Create standard equipment", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createStandardEquipment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="name of standard equipment", embed=True),
    standard_equipment_category_id: str = Body(
        ...,
        description="standard equipment category id of standard equipment",
        embed=True,
    ),
    standard_equipment_category_group_id: str = Body(
        ...,
        description="standard equipment category group id of standard equipment",
        embed=True,
    ),
    manufacturer_id: str = Body(
        ..., description="manufacturer id of standard equipment", embed=True
    ),
    equipment_model_id: str = Body(
        ..., description="equipment model id of standard equipment", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    client = StandardEquipmentClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_STANDARD_EQUIPMENT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_id": client.newId(),
                    "name": name,
                    "standard_equipment_category_id": standard_equipment_category_id,
                    "standard_equipment_category_group_id": standard_equipment_category_group_id,
                    "manufacturer_id": manufacturer_id,
                    "equipment_model_id": equipment_model_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.put(
    "/{standard_equipment_id}",
    summary="Update standard equipment",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateStandardEquipment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    standard_equipment_id: str = Path(
        ...,
        description="standard equipment id that is used in order to update the standard equipment",
    ),
    name: str = Body(..., description="name of name", embed=True),
    standard_equipment_category_id: str = Body(
        ...,
        description="standard equipment category id of standard equipment category id",
        embed=True,
    ),
    standard_equipment_category_group_id: str = Body(
        ...,
        description="standard equipment category group id of standard equipment category group id",
        embed=True,
    ),
    manufacturer_id: str = Body(
        ..., description="manufacturer id of manufacturer id", embed=True
    ),
    equipment_model_id: str = Body(
        ..., description="equipment model id of equipment model id", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_STANDARD_EQUIPMENT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_id": standard_equipment_id,
                    "name": name,
                    "standard_equipment_category_id": standard_equipment_category_id,
                    "standard_equipment_category_group_id": standard_equipment_category_group_id,
                    "manufacturer_id": manufacturer_id,
                    "equipment_model_id": equipment_model_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{standard_equipment_id}",
    summary="Partial update standard equipment",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateStandardEquipment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    standard_equipment_id: str = Path(
        ...,
        description="standard equipment id that is used in order to update the standard equipment",
    ),
    name: str = Body(None, description="name of name", embed=True),
    standard_equipment_category_id: str = Body(
        None,
        description="standard equipment category id of standard equipment category id",
        embed=True,
    ),
    standard_equipment_category_group_id: str = Body(
        None,
        description="standard equipment category group id of standard equipment category group id",
        embed=True,
    ),
    manufacturer_id: str = Body(
        None, description="manufacturer id of manufacturer id", embed=True
    ),
    equipment_model_id: str = Body(
        None, description="equipment model id of equipment model id", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_STANDARD_EQUIPMENT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_id": standard_equipment_id,
                    "name": name,
                    "standard_equipment_category_id": standard_equipment_category_id,
                    "standard_equipment_category_group_id": standard_equipment_category_group_id,
                    "manufacturer_id": manufacturer_id,
                    "equipment_model_id": equipment_model_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/{standard_equipment_id}",
    summary="Delete a standard equipments",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteStandardEquipment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    standard_equipment_id: str = Path(
        ...,
        description="standard equipment id that is used in order to delete the standard equipment",
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_STANDARD_EQUIPMENT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"standard_equipment_id": standard_equipment_id}),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
