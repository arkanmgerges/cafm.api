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
from src.port_adapter.api.rest.grpc.realm.RealmClient import RealmClient
from src.port_adapter.api.rest.model.response.Realm import Realm
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all realms', response_model=List[Realm])
async def getRealms(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                    result_size: int = Query(10, description='Item count to be fetched'),
                    _=Depends(CustomHttpBearer())):
    """Return all realms
    """
    try:
        client = RealmClient()
        return client.realms(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getRealms.__module__}.{getRealms.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{realm_id}/", summary='Get realm',
            response_model=Realm)
async def getRealm(*, realm_id: str = Path(...,
                                           description='Realm id that is used to fetch realm data'),
                   _=Depends(CustomHttpBearer())):
    """Get a Realm by id
    """
    try:
        client = RealmClient()
        return client.realmById(realmId=realm_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getRealm.__module__}.{getRealm.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/create", summary='Create a new realm', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the realm', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_REALM.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{realm_id}", summary='Delete a realm', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 realm_id: str = Path(...,
                                     description='Realm id that is used in order to delete the realm')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_REALM.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': realm_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{realm_id}", summary='Update a realm', status_code=status.HTTP_200_OK)
async def update(*, _=Depends(CustomHttpBearer()),
                 realm_id: str = Path(...,
                                     description='Realm id that is used in order to delete the realm'),
                 name: str = Body(..., description='Title of the realm', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_REALM.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': realm_id, 'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
