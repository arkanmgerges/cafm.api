"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi.responses import JSONResponse

from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.role.RoleClient import RoleClient
from src.port_adapter.api.rest.model.request.Role import Role
from src.port_adapter.api.rest.model.response.Request import BoolRequestResponse, ResultRequestResponse
from src.port_adapter.api.rest.resource.exception.NotFoundException import NotFoundException
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/is_successful", summary='Check if the request has succeeded', response_model=BoolRequestResponse)
async def isRequestSuccessful(*, request_id: str = Query(..., description='Request id to check if it is succeeded or not'),
                      _=Depends(CustomHttpBearer())):
    """Return all roles
    """
    try:
        cache = RedisCache()
        cacheClient = cache.client()
        result = cacheClient.get(f'{cache.cacheResponseKeyPrefix}{request_id}')

        if result is None:
            raise NotFoundException(f'Request id: {request_id} not found')
        else:
            result = json.loads(result.decode('utf-8'))
            return BoolRequestResponse(success=result["success"])
    except NotFoundException as e:
        return JSONResponse(status_code=404, content={"detail": [{"msg": e.msg}]})
    except Exception as e:
        logger.info(e)
        return BoolRequestResponse(success=False)


@router.get(path="/result", summary='Get the request id result', response_model=ResultRequestResponse)
async def getRequestIdResult(*, request_id: str = Query(..., description='Request id that is used to fetch the result'),
                      _=Depends(CustomHttpBearer())):
    try:
        cache = RedisCache()
        cacheClient = cache.client()
        result = cacheClient.get(f'{cache.cacheResponseKeyPrefix}{request_id}')

        if result is None:
            raise NotFoundException(f'Request id: {request_id} not found')
        else:
            result = json.loads(result.decode('utf-8'))
            return ResultRequestResponse(result=result["data"])
    except NotFoundException as e:
        return JSONResponse(status_code=404, content={"detail": [{"msg": e.msg}]})
    except Exception as e:
        logger.info(e)
        return JSONResponse(status_code=400, content={"detail": [{"msg": str(e)}]})