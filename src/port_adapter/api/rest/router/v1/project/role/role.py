"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json
from src.port_adapter.api.rest.grpc.v1.identity import role
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
from src.port_adapter.api.rest.grpc.v1.project.role.RoleClient import RoleClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.role.Roles import Roles
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="/by_organization_type/{organization_type}",
    summary="Get all role(s) by organization type",
    response_model=Roles,
)
@OpenTelemetry.fastApiTraceOTel
async def getRolesByOrganizationType(
    *,
    organization_type: str = Path(
        ..., description="organization type that is used to fetch role data"
    ),
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
):
    try:
        client = RoleClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.rolesByOrganizationType(
            organizationType=organization_type,
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRolesByOrganizationType.__module__}.{getRolesByOrganizationType.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="", summary="Get all role(s)", response_model=Roles)
@OpenTelemetry.fastApiTraceOTel
async def getRoles(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
):
    try:
        client = RoleClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.roles(resultFrom=result_from, resultSize=result_size, orders=orders)
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


@router.get(path="/{role_id}", summary="Get role by id", response_model=RoleDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getRoleById(
    *,
    role_id: str = Path(
        ...,
        description="role id that is used to fetch role data",
    ),
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
):
    """Get a role by id"""
    try:
        client = RoleClient()
        return client.roleById(id=role_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRoleById.__module__}.{getRoleById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/by_name/{role_name}", summary="Get role by name", response_model=RoleDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getRoleByName(
    *,
    role_name: str = Path(
        ...,
        description="role name that is used to fetch role data",
    ),
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
):
    """Get a role by name"""
    try:
        client = RoleClient()
        return client.roleByName(role_name=role_name)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRoleById.__module__}.{getRoleById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.post("", summary="Create role", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createRole(
    *,
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
    name: str = Body(..., description="name of role", embed=True),
    title: str = Body(..., description="title of role", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    client = RoleClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "role_id": client.newId(),
                    "name": name,
                    "title": title,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.put("/{role_id}", summary="Update role", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateRole(
    *,
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
    role_id: str = Path(
        ..., description="role id that is used in order to update the role"
    ),
    name: str = Body(..., description="name of role", embed=True),
    title: str = Body(..., description="title of role", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "role_id": role_id,
                    "name": name,
                    "title": title,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{role_id}", summary="Partial update role", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateRole(
    *,
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
    role_id: str = Path(
        ..., description="role id that is used in order to update the role"
    ),
    name: str = Body(None, description="name of role", embed=True),
    title: str = Body(None, description="title of role", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "role_id": role_id,
                    "name": name,
                    "title": title,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete("/{role_id}", summary="Delete a roles", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteRole(
    *,
    _=Depends(CustomHttpBearer()),
    #    _1=Depends(CustomAuthorization()),
    role_id: str = Path(
        ..., description="role id that is used in order to delete the role"
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_ROLE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id}),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
