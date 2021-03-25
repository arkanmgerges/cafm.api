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
from src.port_adapter.api.rest.grpc.v1.identity.permission.PermissionClient import PermissionClient
from src.port_adapter.api.rest.model.response.v1.identity.Permission import PermissionDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Permissions import Permissions
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


# openTelemetry = AppDi.instance.get(OpenTelemetry)

"""
c4model|cb|api:Component(api__identity_permission_py__getPermissions, "Get Permissions", "http(s)", "Get all permissions")
c4model:Rel(api__identity_permission_py__getPermissions, identity__grpc__PermissionAppServiceListener__permissions, "Get permissions", "grpc")
"""
@router.get(path="", summary='Get all permissions', response_model=Permissions)
@OpenTelemetry.fastApiTraceOTel
async def getPermissions(*,
                         result_from: int = Query(0, description='Starting offset for fetching data'),
                         result_size: int = Query(10, description='Item count to be fetched'),
                         order: str = Query('', description='e.g. name:asc,age:desc'),
                         _=Depends(CustomHttpBearer())):
    try:
        # trace = openTelemetry.trace()
        # with trace.get_current_span() as span:
        #     span.set_attribute("result_from", result_from)
        #     span.set_attribute("result_size", result_size)
        #     span.set_attribute("order", order)

        client = PermissionClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.permissions(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getPermissions.__module__}.{getPermissions.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

"""
c4model|cb|api:Component(api__identity_permission_py__getPermission, "Get Permission", "http(s)", "Get permission by id")
c4model:Rel(api__identity_permission_py__getPermission, identity__grpc__PermissionAppServiceListener__permissionById, "Get permission by id", "grpc")
"""
@router.get(path="/{permission_id}", summary='Get permission',
            response_model=PermissionDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getPermission(*, permission_id: str = Path(...,
                                                     description='Permission id that is used to fetch permission data'),
                        _=Depends(CustomHttpBearer())):
    """Get a Permission by id
    """
    try:
        client = PermissionClient()
        return client.permissionById(permissionId=permission_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getPermission.__module__}.{getPermission.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass

"""
c4model|cb|api:Component(api__identity_permission_py__create, "Create Permission", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_py__create__api_command_topic, "CommonCommandConstant.CREATE_PERMISSION.value", "api command topic", "")
c4model:Rel(api__identity_permission_py__create, api__identity_permission_py__create__api_command_topic, "CommonCommandConstant.CREATE_PERMISSION.value", "message")
"""
@router.post("", summary='Create a new permission', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createPermission(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the permission', embed=True),
                 allowed_actions: List[str] = Body(..., description='The actions that are allowed by the permission',
                                                   embed=True),
                 denied_actions: List[str] = Body(...,
                                                  description='The actions that are denied by the permission and it has higher priority over the allowed actions',
                                                  embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    client = PermissionClient()
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_PERMISSION.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'permission_id': client.newId(), 'name': name, 'allowed_actions': allowed_actions,
                                         'denied_actions': denied_actions})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}

"""
c4model|cb|api:Component(api__identity_permission_py__delete, "Delete Permission", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_py__delete__api_command_topic, "CommonCommandConstant.DELETE_PERMISSION.value", "api command topic", "")
c4model:Rel(api__identity_permission_py__delete, api__identity_permission_py__delete__api_command_topic, "CommonCommandConstant.DELETE_PERMISSION.value", "message")
"""
@router.delete("/{permission_id}", summary='Delete a permission', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deletePermission(*, _=Depends(CustomHttpBearer()),
                 permission_id: str = Path(...,
                                           description='Permission id that is used in order to delete the permission')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_PERMISSION.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'permission_id': permission_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}

"""
c4model|cb|api:Component(api__identity_permission_py__update, "Update Permission", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_permission_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PERMISSION.value", "api command topic", "")
c4model:Rel(api__identity_permission_py__update, api__identity_permission_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PERMISSION.value", "message")
"""
@router.put("/{permission_id}", summary='Update a permission', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updatePermission(*, _=Depends(CustomHttpBearer()),
                 permission_id: str = Path(...,
                                           description='Permission id that is used in order to update the permission'),
                 name: str = Body(..., description='Title of the permission', embed=True),
                 allowed_actions: List[str] = Body(..., description='The actions that is allowed by the permission',
                                                   embed=True),
                 denied_actions: List[str] = Body(...,
                                                  description='The actions that are denied by the permission and it has higher priority over the allowed actions',
                                                  embed=True)
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_PERMISSION.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'permission_id': permission_id, 'name': name, 'allowed_actions': allowed_actions,
                                         'denied_actions': denied_actions})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
