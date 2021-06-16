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
from src.application.AuthenticationApplicationService import (
    AuthenticationApplicationService,
)
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.user.UserClient import UserClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.helper.Validator import Validator
from src.port_adapter.api.rest.model.response.v1.identity.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.HasUserPasswordSet import HasUserPasswordSetDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Users import Users
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_user_py__getUsers, "Get Users", "http(s)", "Get all users")
c4model:Rel(api__identity_user_py__getUsers, identity__grpc__UserAppServiceListener__users, "Get users", "grpc")
"""


@router.get(path="", summary="Get all users", response_model=Users)
@OpenTelemetry.fastApiTraceOTel
async def getUsers(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = UserClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.users(resultFrom=result_from, resultSize=result_size, orders=orders)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUsers.__module__}.{getUsers.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{user_id}/has_user_password_set", summary="Get user has password set", response_model=HasUserPasswordSetDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getHasUserPasswordSet(
    *,
    user_id: str = Path(..., description="User id that is used to fetch user data"),
    # _=Depends(CustomHttpBearer()),
    # __=Depends(CustomAuthorization()),
):
    """Get a User has one time password"""
    try:
        # trace = openTelemetry.trace()
        # with trace.get_current_span() as span:
        #     span.set_attribute("user_id", user_id)

        client = UserClient()
        return client.hasUserPasswordSet(userId=user_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getHasUserPasswordSet.__module__}.{getHasUserPasswordSet.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

"""
c4model|cb|api:Component(api__identity_user_py__getUser, "Get User", "http(s)", "Get user by id")
c4model:Rel(api__identity_user_py__getUser, identity__grpc__UserAppServiceListener__userById, "Get user by id", "grpc")
"""


@router.get(path="/{user_id}", summary="Get user", response_model=UserDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getUser(
    *,
    user_id: str = Path(..., description="User id that is used to fetch user data"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a User by id"""
    try:
        # trace = openTelemetry.trace()
        # with trace.get_current_span() as span:
        #     span.set_attribute("user_id", user_id)

        client = UserClient()
        return client.userById(userId=user_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUser.__module__}.{getUser.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

"""
c4model|cb|api:Component(api__identity_user_py__create, "Create User", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_py__create__api_command_topic, "CommonCommandConstant.CREATE_USER.value", "api command topic", "")
c4model:Rel(api__identity_user_py__create, api__identity_user_py__create__api_command_topic, "CommonCommandConstant.CREATE_USER.value", "message")
"""


@router.post("", summary="Create a new user", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createUser(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    email: str = Body(..., description="User email", embed=True),
):
    reqId = RequestIdGenerator.generateListId(
        2
    )  # 2 for completion of identity & project
    producer = AppDi.instance.get(SimpleProducer)
    Validator.validateEmail(email=email, fields={"email": email})
    client = UserClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "user_id": client.newId(),
                    "email": email,
                }
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_py__delete, "Delete User", http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_py__delete__api_command_topic, "CommonCommandConstant.DELETE_USER.value", "api command topic", "")
c4model:Rel(api__identity_user_py__delete, api__identity_user_py__delete__api_command_topic, "CommonCommandConstant.DELETE_USER.value", "message")
"""


@router.delete("/{user_id}", summary="Delete a user", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteUser(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_id: str = Path(
        ..., description="User id that is used in order to delete the user"
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_id": user_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_py__setUserPassword, "Set User Password", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_py__setUserPassword__api_command_topic, "CommonCommandConstant.SET_USER_PASSWORD.value", "api command topic", "")
c4model:Rel(api__identity_user_py__setUserPassword, api__identity_user_py__setUserPassword__api_command_topic, "CommonCommandConstant.SET_USER_PASSWORD.value", "message")
"""


@router.put(
    "/{user_id}/set_password",
    summary="Set user password",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def setUserPassword(
    *,
    _=Depends(CustomHttpBearer()),
    # __=Depends(CustomAuthorization()),
    user_id: str = Path(
        ..., description="User id that is used in order to set up the user password"
    ),
    password: str = Body(..., description="Password of the user", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    authService: AuthenticationApplicationService = AppDi.instance.get(
        AuthenticationApplicationService
    )
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.SET_USER_PASSWORD.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "user_id": user_id,
                    "password": authService.hashPassword(password=password),
                }
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_user_py__resetUserPassword, "Reset User Password", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_user_py__resetUserPassword__api_command_topic, "CommonCommandConstant.RESET_USER_PASSWORD.value", "api command topic", "")
c4model:Rel(api__identity_user_py__resetUserPassword, api__identity_user_py__resetUserPassword__api_command_topic, "CommonCommandConstant.RESET_USER_PASSWORD.value", "message")
"""


@router.put(
    "/{user_id}/reset_password",
    summary="Reset user password",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def resetUserPassword(
    *,
    # _=Depends(CustomHttpBearer()),
    # __=Depends(CustomAuthorization()),
    user_id: str = Path(
        ..., description="User id that is used in order to reset the user password"
    ),
    email: str = Body(..., description="User email", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.RESET_USER_PASSWORD.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"user_id": user_id, "email": email}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
