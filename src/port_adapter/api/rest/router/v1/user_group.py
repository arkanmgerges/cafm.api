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
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.user_group.UserGroupClient import UserGroupClient
from src.port_adapter.api.rest.model.response.UserGroup import UserGroup
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all user groups', response_model=List[UserGroup])
async def getUserGroups(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                        result_size: int = Query(10, description='Item count to be fetched'),
                        _=Depends(CustomHttpBearer())):
    try:
        client = UserGroupClient()
        return client.userGroups(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUserGroups.__module__}.{getUserGroups.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{user_group_id}/", summary='Get user group',
            response_model=UserGroup)
async def getUserGroup(*, user_group_id: str = Path(...,
                                                   description='User group id that is used to fetch user group data'),
                       _=Depends(CustomHttpBearer())):
    """Get a UserGroup by id
    """
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
                f'[{getUserGroup.__module__}.{getUserGroup.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/create", summary='Create a new user group', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the user group', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{user_group_id}", summary='Delete a user group', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 user_group_id: str = Path(...,
                                     description='User group id that is used in order to delete the user group')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': user_group_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{user_group_id}", summary='Update a user group', status_code=status.HTTP_200_OK)
async def update(*, _=Depends(CustomHttpBearer()),
                 user_group_id: str = Path(...,
                                     description='User group id that is used in order to delete the user group'),
                 name: str = Body(..., description='Title of the user group', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_USER_GROUP.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': user_group_id, 'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
