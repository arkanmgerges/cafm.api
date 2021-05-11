"""
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
from src.port_adapter.api.rest.grpc.v1.identity.permission_context.PermissionContextClient import (
    PermissionContextClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContext import (
    PermissionContextDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.PermissionContexts import (
    PermissionContexts,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_permission_context_py__getPermissionContexts, "Get Permission Contexts", "http(s)", "Get all permission contexts")
c4model:Rel(api__identity_permission_context_py__getPermissionContexts, identity__grpc__PermissionContextAppServiceListener__permissionContexts, "Get permission contexts", "grpc")
"""


@router.get(
    path="", summary="Get all permission contexts", response_model=PermissionContexts
)
@OpenTelemetry.fastApiTraceOTel
async def getPermissionContexts(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = PermissionContextClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.permissionContexts(
            resultFrom=result_from, resultSize=result_size, order=order
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getPermissionContexts.__module__}.{getPermissionContexts.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_permission_context_py__getPermissionContext, "Get Permission Context", "http(s)", "Get permission context by id")
c4model:Rel(api__identity_permission_context_py__getPermissionContext, identity__grpc__PermissionContextAppServiceListener__permissionContextById, "Get permission context by id", "grpc")
"""


@router.get(
    path="/{permission_context_id}",
    summary="Get permission context",
    response_model=PermissionContextDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getPermissionContext(
    *,
    permission_context_id: str = Path(
        ...,
        description="Resource type id that is used to fetch permission context data",
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = PermissionContextClient()
        return client.permissionContextById(permissionContextId=permission_context_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getPermissionContext.__module__}.{getPermissionContext.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_permission_context_py__create, "Create Permission Context", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_context_py__create__api_command_topic, "CommonCommandConstant.CREATE_RESOURCE_TYPE.value", "api command topic", "")
c4model:Rel(api__identity_permission_context_py__create, api__identity_permission_context_py__create__api_command_topic, "CommonCommandConstant.CREATE_RESOURCE_TYPE.value", "message")
"""


@router.post(
    "", summary="Create a new permission context", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def createPermissionContext(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    type: str = Body(..., description="Type of the permission context", embed=True),
    data: dict = Body(..., description="Data of the permission context", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    client = PermissionContextClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_PERMISSION_CONTEXT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {"permission_context_id": client.newId(), "type": type, "data": data}
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_permission_context_py__delete, "Delete Permission Context", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_context_py__delete__api_command_topic, "CommonCommandConstant.DELETE_RESOURCE_TYPE.value", "api command topic", "")
c4model:Rel(api__identity_permission_context_py__delete, api__identity_permission_context_py__delete__api_command_topic, "CommonCommandConstant.DELETE_RESOURCE_TYPE.value", "message")
"""


@router.delete(
    "/{permission_context_id}",
    summary="Delete a permission context",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deletePermissionContext(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    permission_context_id: str = Path(
        ...,
        description="PermissionContext id that is used in order to delete the permission context",
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_RESOURCE_TYPE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"permission_context_id": permission_context_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_permission_context_py__update, "Update Permission Context", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_context_py__update__api_command_topic, "CommonCommandConstant.UPDATE_RESOURCE_TYPE.value", "api command topic", "")
c4model:Rel(api__identity_permission_context_py__update, api__identity_permission_context_py__update__api_command_topic, "CommonCommandConstant.UPDATE_RESOURCE_TYPE.value", "message")
"""


@router.put(
    "/{permission_context_id}",
    summary="Update a permission context",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updatePermissionContext(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    permission_context_id: str = Path(
        ...,
        description="Resource type id that is used in order to update the permission context",
    ),
    type: str = Body(..., description="Type of the permission context", embed=True),
    data: dict = Body(..., description="Data of the permission context", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_PERMISSION_CONTEXT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "permission_context_id": permission_context_id,
                    "type": type,
                    "data": data,
                }
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
