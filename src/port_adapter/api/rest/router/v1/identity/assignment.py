"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Body
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
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.role.RoleClient import RoleClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.Role import RoleDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionData import (
    RoleAccessPermissionDataDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.RoleAccessPermissionDatas import (
    RoleAccessPermissionDatas,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="/roles_trees",
    summary="Get all tree details for all roles",
    response_model=RoleAccessPermissionDatas,
)
@OpenTelemetry.fastApiTraceOTel
async def getRolesTrees(*, _=Depends(CustomHttpBearer())):
    try:
        client = RoleClient()
        return client.rolesTrees()
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRolesTrees.__module__}.{getRolesTrees.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/roles/{role_id}/role_tree",
    summary="Get all tree details for a role",
    response_model=RoleAccessPermissionDataDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getRoleTree(
    *,
    role_id: str = Path(..., description="Role id that is used to fetch role data"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = RoleClient()
        return client.roleTree(role_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRoleTree.__module__}.{getRoleTree.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/{role_id}", summary="Get role assignments", response_model=RoleDescriptor
)
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


@router.post(
    "/role_to_user", summary="Assign role to user", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def AssignRoleToUser(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(..., description="Role id to be assigned to user", embed=True),
    user_id: str = Body(..., description="User id to have the role", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_ROLE_TO_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "user_id": user_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/role_to_user",
    summary="Remove a role assignment to user",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeRoleToUserAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(
        ..., description="Role id to be disconnected from the user", embed=True
    ),
    user_id: str = Body(
        ..., description="User id that will be disconnected from the role", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "user_id": user_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
    "/role_to_user_group",
    summary="Assign role to user group",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignRoleToUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(
        ..., description="Role id to be assigned to user group", embed=True
    ),
    user_group_id: str = Body(
        ..., description="User group id to have the role", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_ROLE_TO_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "user_group_id": user_group_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/role_to_user_group",
    summary="Remove a role assignment to user group",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeRoleToUserGroupAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(
        ..., description="Role id to be disconnected from the user group", embed=True
    ),
    user_group_id: str = Body(
        ...,
        description="User group id that will be disconnected from the role",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "user_group_id": user_group_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
    "/user_to_user_group",
    summary="Assign user to user group",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignUserToUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_id: str = Body(..., description="User id to have the user group", embed=True),
    user_group_id: str = Body(
        ..., description="User group id to be assigned to user", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_USER_TO_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": user_group_id, "user_id": user_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/user_to_user_group",
    summary="Remove assignment a user to user group",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeUserToUserGroupAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_id: str = Body(
        ...,
        description="User id that will be disconnected from the user group",
        embed=True,
    ),
    user_group_id: str = Body(
        ...,
        description="User group id to be disconnected from the user group",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_USER_TO_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": user_group_id, "user_id": user_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
    "/role_to_permission",
    summary="Assign role to permission",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignRoleToPermission(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(
        ..., description="Role id that will have a permission", embed=True
    ),
    permission_id: str = Body(
        ..., description="Permission id to be assigned to a role", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_ROLE_TO_PERMISSION.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "permission_id": permission_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/role_to_permission",
    summary="Remove the assignment of a role to permission",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeRoleToPermissionAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    role_id: str = Body(
        ...,
        description="Role id that will remove the assignment for a permission for resource type",
        embed=True,
    ),
    permission_id: str = Body(
        ...,
        description="Permission id to be have assignment removed to a role for a resource type",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_PERMISSION.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"role_id": role_id, "permission_id": permission_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
    "/permission_to_permission_context",
    summary="Assign permission to permission context",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignPermissionToPermissionContext(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    permission_id: str = Body(
        ..., description="Permission id to be assigned to a resource type", embed=True
    ),
    permission_context_id: str = Body(
        ...,
        description="Permission context id to be associated with the permission",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_PERMISSION_TO_PERMISSION_CONTEXT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "permission_id": permission_id,
                    "permission_context_id": permission_context_id,
                }
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/permission_to_permission_context",
    summary="Revoke the assignment of a permission from permission context",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removePermissionToPermissionContextAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    permission_id: str = Body(
        ...,
        description="Permission id to be have assignment removed from the permission context",
        embed=True,
    ),
    permission_context_id: str = Body(
        ...,
        description="Permission context id to be dissociated from the permission",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_PERMISSION_TO_PERMISSION_CONTEXT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "permission_id": permission_id,
                    "permission_context_id": permission_context_id,
                }
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
    "/resource_to_resource",
    summary="Assign a resource to another resouce",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignResourceToAnotherResource(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    src_resource_id: str = Body(..., description="Source resource id", embed=True),
    dst_resource_id: str = Body(..., description="Destination resource id", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.ASSIGN_RESOURCE_TO_RESOURCE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {"src_resource_id": src_resource_id, "dst_resource_id": dst_resource_id}
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/resource_to_resource",
    summary="Remove assignment of resource to another resource",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeResourceToAnotherResourceAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    src_resource_id: str = Body(
        ...,
        description="Source resource to unlink it from the destination resource",
        embed=True,
    ),
    dst_resource_id: str = Body(
        ...,
        description="Destination resource to unlink it from the source resource",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_RESOURCE_TO_RESOURCE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {"src_resource_id": src_resource_id, "dst_resource_id": dst_resource_id}
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.post(
"/assign_child_realm_to_parent_realm",
summary="Assign a resource to another resouce",
status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def assignResourceToAnotherResource(
        *,
        _=Depends(CustomHttpBearer()),
        __=Depends(CustomAuthorization()),
        child_realm_id: str = Body(..., description="Child realm id", embed=True),
        parent_realm_id: str = Body(..., description="Parent realm id", embed=True),
    ):
        reqId = RequestIdGenerator.generateId()
        producer = AppDi.instance.get(SimpleProducer)
        producer.produce(
            obj=ApiCommand(
                id=reqId,
                name=CommandConstant.ASSIGN_RESOURCE_TO_RESOURCE.value,
                metadata=json.dumps({"token": Client.token}),
                data=json.dumps(
                    {"src_resource_id": parent_realm_id, "dst_resource_id": child_realm_id}
                ),
            ),
            schema=ApiCommand.get_schema(),
        )
        return {"request_id": reqId}

@router.delete(
    "/assign_child_realm_to_parent_realm",
    summary="Remove assignment of resource to another resource",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def removeResourceToAnotherResourceAssignment(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    child_realm_id: str = Body(..., description="Child realm id to unlink", embed=True),
    parent_realm_id: str = Body(..., description="Parent realm id to unlink", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.REVOKE_ASSIGNMENT_RESOURCE_TO_RESOURCE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {"src_resource_id": parent_realm_id, "dst_resource_id": child_realm_id}
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}