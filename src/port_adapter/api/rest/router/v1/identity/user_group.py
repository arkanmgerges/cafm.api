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
from src.port_adapter.api.rest.grpc.v1.identity.user_group.UserGroupClient import (
    UserGroupClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.UserGroup import (
    UserGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.UserGroups import UserGroups
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_user_group_py__getUserGroups, "Get User Groups", "http(s)", "get all user groups")
c4model:Rel(api__identity_user_group_py__getUserGroups, identity__grpc__UserGroupAppServiceListener__userGroups, "Get user groups", "grpc")
"""


@router.get(path="", summary="Get all user groups", response_model=UserGroups)
@OpenTelemetry.fastApiTraceOTel
async def getUserGroups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = UserGroupClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.userGroups(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUserGroups.__module__}.{getUserGroups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_user_group_py__getUserGroup, "Get User Group", "http(s)", "get user group by id")
c4model:Rel(api__identity_user_group_py__getUserGroup, identity__grpc__UserGroupAppServiceListener__userGroupById, "Get user group by id", "grpc")
"""


@router.get(
    path="/{user_group_id}",
    summary="Get user group",
    response_model=UserGroupDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getUserGroup(
    *,
    user_group_id: str = Path(
        ..., description="User group id that is used to fetch user group data"
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a UserGroup by id"""
    try:
        client = UserGroupClient()
        return client.userGroupById(userGroupId=user_group_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUserGroup.__module__}.{getUserGroup.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_user_group_py__create, "Create User Group", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_group_py__create__api_command_topic, "CommonCommandConstant.CREATE_USER_GROUP.value", "api command topic", "")
c4model:Rel(api__identity_user_group_py__create, api__identity_user_group_py__create__api_command_topic, "CommonCommandConstant.CREATE_USER_GROUP.value", "message")
"""


@router.post("", summary="Create a new user group", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="Title of the user group", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    client = UserGroupClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": client.newId(), "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_group_py__delete, "Delete User Group", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_group_py__delete__api_command_topic, "CommonCommandConstant.DELETE_USER_GROUP.value", "api command topic", "")
c4model:Rel(api__identity_user_group_py__delete, api__identity_user_group_py__delete__api_command_topic, "CommonCommandConstant.DELETE_USER_GROUP.value", "message")
"""


@router.delete(
    "/{user_group_id}", summary="Delete a user group", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def deleteUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_group_id: str = Path(
        ..., description="User group id that is used in order to delete the user group"
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": user_group_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_group_py__update, "Update User Group", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_group_py__update__api_command_topic, "CommonCommandConstant.UPDATE_USER_GROUP.value", "api command topic", "")
c4model:Rel(api__identity_user_group_py__update, api__identity_user_group_py__update__api_command_topic, "CommonCommandConstant.UPDATE_USER_GROUP.value", "message")
"""


@router.put(
    "/{user_group_id}", summary="Update a user group", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def updateUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_group_id: str = Path(
        ..., description="User group id that is used in order to update the user group"
    ),
    name: str = Body(..., description="Title of the user group", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": user_group_id, "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_group_py__partial_update, "Update User Group", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_group_py__update__api_command_topic, "CommonCommandConstant.UPDATE_USER_GROUP.value", "api command topic", "")
c4model:Rel(api__identity_user_group_py__partial_update, api__identity_user_group_py__update__api_command_topic, "CommonCommandConstant.UPDATE_USER_GROUP.value", "message")
"""


@router.patch(
    "/{user_group_id}", summary="Update a user group", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateUserGroup(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_group_id: str = Path(
        ..., description="User group id that is used in order to update the user group"
    ),
    name: str = Body(None, description="Title of the user group", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.UPDATE_USER_GROUP.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_group_id": user_group_id, "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
