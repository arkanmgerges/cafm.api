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
from src.port_adapter.api.rest.grpc.v1.identity.role.RoleClient import RoleClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.Role import RoleDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Roles import Roles
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_role_py__getRoles, "Get Roles", "http(s)", "Get all roles")
c4model:Rel(api__identity_role_py__getRoles, identity__grpc__RoleAppServiceListener__roles, "Get roles", "grpc")
"""


@router.get(path="", summary="Get all roles", response_model=Roles)
@OpenTelemetry.fastApiTraceOTel
async def getRoles(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = RoleClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.roles(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRoles.__module__}.{getRoles.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_role_py__getRole, "Get Role", "http(s)", "Get role by id")
c4model:Rel(api__identity_role_py__getRole, identity__grpc__RoleAppServiceListener__roleById, "Get role by id", "grpc")
"""


@router.get(path="/{role_id}", summary="Get role", response_model=RoleDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getRole(
    *,
    role_id: str = Path(..., description="Role id that is used to fetch role data"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = RoleClient()
        return client.roleById(roleId=role_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRole.__module__}.{getRole.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_role_py__create, "Create Role", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_role_py__create__api_command_topic, "CommonCommandConstant.CREATE_ROLE.value", "api command topic", "")
c4model:Rel(api__identity_role_py__create, api__identity_role_py__create__api_command_topic, "CommonCommandConstant.CREATE_ROLE.value", "message")
"""


@router.post("", summary="Create a new role", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createRole(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="Title of the role", embed=True),
    title: str = Body(..., description="Display title of the role", embed=True),
):
    from src.port_adapter.messaging.listener.CacheType import CacheType

    reqId = RequestIdGenerator.generateListId(2)
    producer = AppDi.instance.get(SimpleProducer)
    client = RoleClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": client.newId(), "name": name, "title": title}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_role_py__delete, "Delete Role", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_role_py__delete__api_command_topic, "CommonCommandConstant.DELETE_ROLE.value", "api command topic", "")
c4model:Rel(api__identity_role_py__delete, api__identity_role_py__delete__api_command_topic, "CommonCommandConstant.DELETE_ROLE.value", "message")
"""


@router.delete("/{role_id}", summary="Delete a role", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteRole(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Path(
        ..., description="Role id that is used in order to delete the role"
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_role_py__update, "Update Role", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_role_py__update__api_command_topic, "CommonCommandConstant.DELETE_ROLE.value", "api command topic", "")
c4model:Rel(api__identity_role_py__update, api__identity_role_py__update__api_command_topic, "CommonCommandConstant.DELETE_ROLE.value", "message")
"""


@router.put("/{role_id}", summary="Update a role", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateRole(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Path(
        ..., description="Role id that is used in order to update the role"
    ),
    name: str = Body(..., description="Title of the role", embed=True),
    title: str = Body(..., description="Display title of the role", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "name": name, "title": title}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
