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
from src.port_adapter.api.rest.grpc.v1.project.equipment.model.EquipmentModelClient import (
    EquipmentModelClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.equipment.model.EquipmentModels import (
    EquipmentModels,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.model.EquipmentModel import (
    EquipmentModelDescriptor,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="", summary="Get all equipment model(s)", response_model=EquipmentModels
)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentModels(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = EquipmentModelClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.equipmentModels(
            resultFrom=result_from, resultSize=result_size, order=order
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getEquipmentModels.__module__}.{getEquipmentModels.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/{equipment_model_id}",
    summary="Get equipment model by id",
    response_model=EquipmentModelDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentModelById(
    *,
    equipment_model_id: str = Path(
        ..., description="equipment model id that is used to fetch equipment model data"
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a equipment model by id"""
    try:
        client = EquipmentModelClient()
        return client.equipmentModelById(id=equipment_model_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getEquipmentModelById.__module__}.{getEquipmentModelById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary="Create equipment model", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createEquipmentModel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="name of equipment model", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    client = EquipmentModelClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_EQUIPMENT_MODEL.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "equipment_model_id": client.newId(),
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.put(
    "/{equipment_model_id}",
    summary="Update equipment model",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateEquipmentModel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    equipment_model_id: str = Path(
        ...,
        description="equipment model id that is used in order to update the equipment model",
    ),
    name: str = Body(..., description="name of name", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_EQUIPMENT_MODEL.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "equipment_model_id": equipment_model_id,
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# @router.patch("/{equipment_model_id}", summary='Partial update equipment model', status_code=status.HTTP_200_OK)
# @OpenTelemetry.fastApiTraceOTel
# async def partialUpdate(*, _=Depends(CustomHttpBearer()),
#    __=Depends(CustomAuthorization()),
#                         equipment_model_id: str = Path(..., description='equipment model id that is used in order to update the equipment model'),
#                         name: str = Body(..., description='name of name', embed=True),
#                         ):
#     reqId = RequestIdGenerator.generateId()
#     producer = AppDi.instance.get(SimpleProducer)
#     from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
#     producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_MODEL.value,
#                                         metadata=json.dumps({"token": Client.token}),
#                                         data=json.dumps(
#                                             {'equipment_model_id': equipment_model_id,
#                                             'name': name,
#                                             }),
#                                         external=[]),
#                      schema=ProjectCommand.get_schema())
#     return {"request_id": reqId}


@router.delete(
    "/{equipment_model_id}",
    summary="Delete a equipment models",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteEquipmentModel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    equipment_model_id: str = Path(
        ...,
        description="equipment model id that is used in order to delete the equipment model",
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_EQUIPMENT_MODEL.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"equipment_model_id": equipment_model_id}),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
