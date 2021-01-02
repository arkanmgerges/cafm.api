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
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.AuthenticationService import AuthenticationService
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.user.UserClient import UserClient
from src.port_adapter.api.rest.helper.Validator import Validator
from src.port_adapter.api.rest.model.response.v1.identity.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Users import Users
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="/", summary='Get all users', response_model=Users)
@OpenTelemetry.fastApiTraceOTel
async def getUsers(*,
                   result_from: int = Query(0, description='Starting offset for fetching data'),
                   result_size: int = Query(10, description='Item count to be fetched'),
                   order: str = Query('', description='e.g. name:asc,age:desc'),
                   _=Depends(CustomHttpBearer())):
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
                f'[{getUsers.__module__}.{getUsers.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{user_id}/", summary='Get user',
            response_model=UserDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getUser(*, user_id: str = Path(...,
                                         description='User id that is used to fetch user data'),
                  _=Depends(CustomHttpBearer())):
    """Get a User by id
    """
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
                f'[{getUser.__module__}.{getUser.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/create", summary='Create a new user', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 email: str = Body(..., description='User email', embed=True),
                 first_name: str = Body(..., description='First name of the user', embed=True),
                 last_name: str = Body(..., description='Last name of the user', embed=True),
                 address_line_one: str = Body(..., description='User first line of address', embed=True),
                 address_line_two: str = Body(..., description='User second line of address', embed=True),
                 postal_code: str = Body(..., description='Postal code of the user', embed=True),
                 avatar_image: str = Body(..., description='Avatar URL of the user', embed=True),
                 ):
    reqId = f'{CacheType.LIST.value}:{str(uuid4())}:3'  # 3 for completion of identity & project
    producer = AppDi.instance.get(SimpleProducer)
    Validator.validateEmail(email=email, fields={'email': email})
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_USER.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'email': email,
                                         # 'password': authService.hashPassword(password=password),
                                         'first_name': first_name,
                                         'last_name': last_name,
                                         'address_one': address_line_one,
                                         'address_two': address_line_two,
                                         'postal_code': postal_code,
                                         'avatar_image': avatar_image})),
                     schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{user_id}", summary='Delete a user', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 user_id: str = Path(...,
                                     description='User id that is used in order to delete the user')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_USER.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': user_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{user_id}", summary='Update a user', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 user_id: str = Path(...,
                                     description='User id that is used in order to delete the user'),
                 name: str = Body(..., description='Username of the user', embed=True),
                 password: str = Body(..., description='Password of the user', embed=True),
                 first_name: str = Body(..., description='First name of the user', embed=True),
                 last_name: str = Body(..., description='Last name of the user', embed=True),
                 address_line_one: str = Body(..., description='User first line of address', embed=True),
                 address_line_two: str = Body(..., description='User second line of address', embed=True),
                 postal_code: str = Body(..., description='Postal code of the user', embed=True),
                 avatar_image: str = Body(..., description='Avatar URL of the user', embed=True),
                 ):
    reqId = f'{CacheType.LIST.value}:{str(uuid4())}:2'
    producer = AppDi.instance.get(SimpleProducer)
    authService: AuthenticationService = AppDi.instance.get(AuthenticationService)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_USER.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': user_id,
                                         'name': name,
                                         'password': authService.hashPassword(password=password),
                                         'first_name': first_name,
                                         'last_name': last_name,
                                         'address_one': address_line_one,
                                         'address_two': address_line_two,
                                         'postal_code': postal_code,
                                         'avatar_image': avatar_image})),
                     schema=ApiCommand.get_schema())
    return {"request_id": reqId}
