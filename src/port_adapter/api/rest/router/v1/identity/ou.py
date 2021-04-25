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
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.ou.OuClient import OuClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.Ou import OuDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Ous import Ous
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.common.model.IdentityCommand import IdentityCommand
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_ou_py__getOus, "Get Ous", "http(s)", "")
c4model:Rel(api__identity_ou_py__getOus, identity__grpc__OuAppServiceListener__ous, "Get ous", "grpc")
"""


@router.get(path="", summary="Get all ous", response_model=Ous)
@OpenTelemetry.fastApiTraceOTel
async def getOus(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
):
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
                f"[{getOus.__module__}.{getOus.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_ou_py__getOu, "Get Ou", "http(s)", "Get ou by id")
c4model:Rel(api__identity_ou_py__getOu, identity__grpc__OuAppServiceListener__ouById, "Get ou by id", "grpc")
"""


@router.get(path="/{ou_id}", summary="Get ou", response_model=OuDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getOu(
    *,
    ou_id: str = Path(..., description="Ou id that is used to fetch ou data"),
    _=Depends(CustomHttpBearer()),
):
    """Get a Ou by id"""
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
                f"[{getOu.__module__}.{getOu.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_ou_py__create, "Create Ou", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_ou_py__create__api_command_topic, "CommonCommandConstant.CREATE_OU.value", "api command topic", "")
c4model:Rel(api__identity_ou_py__create, api__identity_ou_py__create__api_command_topic, "CommonCommandConstant.CREATE_OU.value", "message")
"""


@router.post("", summary="Create a new ou", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createOu(
    *,
    _=Depends(CustomHttpBearer()),
    name: str = Body(..., description="Title of the ou", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    client = OuClient()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=IdentityCommand(
            id=reqId,
            name=CommandConstant.CREATE_OU.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"ou_id": client.newId(), "name": name}),
            external=[],
        ),
        schema=IdentityCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_ou_py__delete, "Delete Ou", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_ou_py__delete__api_command_topic, "CommonCommandConstant.DELETE_OU.value", "api command topic", "")
c4model:Rel(api__identity_ou_py__delete, api__identity_ou_py__delete__api_command_topic, "CommonCommandConstant.DELETE_OU.value", "message")
"""


@router.delete("/{ou_id}", summary="Delete a ou", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteOu(
    *,
    _=Depends(CustomHttpBearer()),
    ou_id: str = Path(..., description="Ou id that is used in order to delete the ou"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_OU.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"ou_id": ou_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_ou_py__update, "Update Ou", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_ou_py__update__api_command_topic, "CommonCommandConstant.UPDATE_OU.value", "api command topic", "")
c4model:Rel(api__identity_ou_py__update, api__identity_ou_py__update__api_command_topic, "CommonCommandConstant.UPDATE_OU.value", "message")
"""


@router.put("/{ou_id}", summary="Update a ou", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateOu(
    *,
    _=Depends(CustomHttpBearer()),
    ou_id: str = Path(..., description="Ou id that is used in order to update the ou"),
    name: str = Body(..., description="Title of the ou", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_OU.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"ou_id": ou_id, "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_ou_py__partial_update, "Update Ou", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_ou_py__update__api_command_topic, "CommonCommandConstant.UPDATE_OU.value", "api command topic", "")
c4model:Rel(api__identity_ou_py__partial_update, api__identity_ou_py__update__api_command_topic, "CommonCommandConstant.UPDATE_OU.value", "message")
"""


@router.patch("/{ou_id}", summary="Partial update a ou", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateOu(
    *,
    _=Depends(CustomHttpBearer()),
    ou_id: str = Path(..., description="Ou id that is used in order to update the ou"),
    name: str = Body(None, description="Title of the ou", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_OU.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"ou_id": ou_id, "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
