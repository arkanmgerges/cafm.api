"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List
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
from src.port_adapter.api.rest.grpc.role.RoleClient import RoleClient
from src.port_adapter.api.rest.model.response.Role import Role
from src.port_adapter.api.rest.model.response.Roles import Roles
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/roles", summary='Get all assignments for all roles', response_model=Roles)
async def getRoles(*,
                   result_from: int = Query(0, description='Starting offset for fetching data'),
                   result_size: int = Query(10, description='Item count to be fetched'),
                   order: str = Query('', description='e.g. name:asc,age:desc'),
                   _=Depends(CustomHttpBearer())):
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
                f'[{getRoles.__module__}.{getRoles.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{role_id}", summary='Get role assignments',
            response_model=Role)
async def getRole(*, role_id: str = Path(...,
                                         description='Role id that is used to fetch role data'),
                  _=Depends(CustomHttpBearer())):
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
                f'[{getRole.__module__}.{getRole.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/role_to_user", summary='Assign role to user', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to be assigned to user', embed=True),
                 user_id: str = Body(..., description='User id to have the role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.ASSIGN_ROLE_TO_USER.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'user_id': user_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/role_to_user", summary='Remove a role assignment to user', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to be disconnected from the user', embed=True),
                 user_id: str = Body(..., description='User id that will be disconnected from the role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_USER.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'user_id': user_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}

@router.post("/role_to_user_group", summary='Assign role to user group', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to be assigned to user group', embed=True),
                 user_group_id: str = Body(..., description='User group id to have the role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.ASSIGN_ROLE_TO_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'user_group_id': user_group_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/role_to_user_group", summary='Remove a role assignment to user group', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to be disconnected from the user group', embed=True),
                 user_group_id: str = Body(..., description='User group id that will be disconnected from the role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'user_group_id': user_group_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}

@router.post("/user_to_user_group", summary='Assign user to user group', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 user_id: str = Body(..., description='User id to have the user group', embed=True),
                 user_group_id: str = Body(..., description='User group id to be assigned to user', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.ASSIGN_USER_TO_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'user_group_id': user_group_id, 'user_id': user_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/user_to_user_group", summary='Remove assignment a user to user group', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 user_id: str = Body(..., description='User id that will be disconnected from the user group', embed=True),
                 user_group_id: str = Body(..., description='User group id to be disconnected from the user group', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.REVOKE_ASSIGNMENT_USER_TO_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'user_group_id': user_group_id, 'user_id': user_id})), schema=ApiCommand.get_schema(),
                     )
    return {"request_id": reqId}


@router.post("/role_permission_resource_type", summary='Assign role to permission for resource type', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id that will have a permission for resource type', embed=True),
                 permission_id: str = Body(..., description='Permission id to be assigned to a role for a resource type', embed=True),
                 resource_type_id: str = Body(..., description='Resource type id to be associated for a permission to a role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.ASSIGN_ROLE_TO_PERMISSION_FOR_RESOURCE_TYPE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'permission_id': permission_id, 'resource_type_id': resource_type_id})), schema=ApiCommand.get_schema(),
                     )
    return {"request_id": reqId}

@router.delete("/role_permission_resource_type", summary='Remove the assignment of a role to permission for resource type', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id that will remove the assignment for a permission for resource type', embed=True),
                 permission_id: str = Body(..., description='Permission id to be have assignment removed to a role for a resource type', embed=True),
                 resource_type_id: str = Body(..., description='Resource type id to be disassociated for a permission to a role', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.REVOKE_ASSIGNMENT_ROLE_TO_PERMISSION_FOR_RESOURCE_TYPE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'permission_id': permission_id, 'resource_type_id': resource_type_id})), schema=ApiCommand.get_schema(),
                     )
    return {"request_id": reqId}

@router.post("/access/role_resource", summary='Link access for a role to a resource', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to link access to a resource', embed=True),
                 resource_id: str = Body(..., description='Resource is for a role to have access to', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_ROLE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'resource_id': resource_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}

@router.delete("/access/role_resource", summary='Remove a link access for a role to a resource', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to remove link access to a resource', embed=True),
                 resource_id: str = Body(..., description='Resource is for a role to remove the access to', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_ROLE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'resource_id': resource_id})), schema=ApiCommand.get_schema())
