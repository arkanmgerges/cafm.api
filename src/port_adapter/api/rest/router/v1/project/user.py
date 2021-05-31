"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import Optional
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
from src.port_adapter.api.rest.grpc.v1.project.user.UserClient import UserClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.UserLookups import UserLookups
from src.port_adapter.api.rest.model.response.v1.project.Users import Users
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary="Get all users", response_model=Users)
@OpenTelemetry.fastApiTraceOTel
async def getUsers(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = UserClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.users(resultFrom=result_from, resultSize=result_size, order=order)
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


@router.put("/{user_id}", summary="Update a user", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateUser(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_id: str = Path(
        ..., description="User id that is used in order to update the user"
    ),
    email: str = Body(..., description="User email", embed=True),
    first_name: str = Body(..., description="First name of the user", embed=True),
    last_name: str = Body(..., description="Last name of the user", embed=True),
    address_one: str = Body(..., description="User first line of address", embed=True),
    address_two: str = Body(..., description="User second line of address", embed=True),
    postal_code: str = Body(..., description="Postal code of the user", embed=True),
    phone_number: str = Body(..., description="Phone number of the user", embed=True),
    avatar_image: str = Body(..., description="Avatar URL of the user", embed=True),
    country_id: int = Body(..., description="Country id", embed=True),
    city_id: int = Body(..., description="City id", embed=True),
    country_state_name: str = Body(..., description="State name", embed=True),
    country_state_iso_code: str = Body(
        ..., description="Country State Iso code", embed=True
    ),
    start_date: float = Body(..., description="Start date of the user", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "user_id": user_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "address_one": address_one,
                    "address_two": address_two,
                    "postal_code": postal_code,
                    "phone_number": phone_number,
                    "avatar_image": avatar_image,
                    "country_id": country_id,
                    "city_id": city_id,
                    "country_state_name": country_state_name,
                    "country_state_iso_code": country_state_iso_code,
                    "start_date": start_date,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{user_id}", summary="Partial update a user", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateUser(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    user_id: str = Path(
        ..., description="User id that is used in order to update the user"
    ),
    email: Optional[str] = Body(None, description="User email", embed=True),
    first_name: Optional[str] = Body(
        None, description="First name of the user", embed=True
    ),
    last_name: Optional[str] = Body(
        None, description="Last name of the user", embed=True
    ),
    address_one: Optional[str] = Body(
        None, description="User first line of address", embed=True
    ),
    address_two: Optional[str] = Body(
        None, description="User second line of address", embed=True
    ),
    postal_code: Optional[str] = Body(
        None, description="Postal code of the user", embed=True
    ),
    phone_number: Optional[str] = Body(
        None, description="Phone number of the user", embed=True
    ),
    avatar_image: Optional[str] = Body(
        None, description="Avatar URL of the user", embed=True
    ),
    country_id: Optional[int] = Body(None, description="Country id", embed=True),
    city_id: Optional[int] = Body(None, description="City id", embed=True),
    country_state_name: Optional[str] = Body(
        None, description="State name", embed=True
    ),
    country_state_iso_code: Optional[str] = Body(
        None, description="Counntry State Iso code", embed=True
    ),
    start_date: Optional[float] = Body(
        None, description="Start date of the user", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_USER.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "user_id": user_id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "address_one": address_one,
                    "address_two": address_two,
                    "postal_code": postal_code,
                    "phone_number": phone_number,
                    "avatar_image": avatar_image,
                    "country_id": country_id,
                    "city_id": city_id,
                    "country_state_name": country_state_name,
                    "country_state_iso_code": country_state_iso_code,
                    "start_date": start_date,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.get(path="/{user_id}", summary="Get user by id", response_model=UserDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getUserById(
    *,
    user_id: str = Path(..., description="User id that is used to fetch user data"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a User by id"""
    try:
        client = UserClient()
        return client.userById(id=user_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUserById.__module__}.{getUserById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
