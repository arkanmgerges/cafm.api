"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.port_adapter.api.rest.model.response.Request import BoolRequestResponse, ResultRequestResponse
from src.port_adapter.api.rest.resource.exception.InProgressException import InProgressException
from src.port_adapter.api.rest.resource.exception.NotFoundException import NotFoundException
from src.port_adapter.api.rest.resource.exception.UnknownCacheTypeException import UnknownCacheTypeException
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/is_successful", summary='Check if the request has succeeded', response_model=BoolRequestResponse)
async def isRequestSuccessful(*,
                              request_id: str = Query(..., description='Request id to check if it is succeeded or not'),
                              _=Depends(CustomHttpBearer())):
    """Return all roles
    """
    try:
        cache = RedisCache()
        cacheClient = cache.client()
        cacheKey = f'{cache.cacheResponseKeyPrefix}:{request_id}'
        split = request_id.split(':')
        if len(split) == 1:
            result = cacheClient.get(cacheKey)
            if result is None:
                raise NotFoundException(f'Request id: {request_id} not found')
            result = json.loads(result.decode('utf-8'))
            return BoolRequestResponse(success=result["success"])
        else:
            cacheType = split[0]
            if CacheType.valueToEnum(cacheType) == CacheType.LIST:
                key = split[1]
                successRequired = split[2]
                if cacheClient.llen(cacheKey) == successRequired:
                    items = cacheClient.lrange(cacheKey, 0, -1)
                    logger.debug(items)
                    logger.debug(successRequired)
                    logger.debug(len(items) < int(successRequired))
                    if len(items) < int(successRequired):
                        raise InProgressException(f'Request id: {request_id} is still in progress')
                    for item in items:
                        result = json.loads(item.decode('utf-8'))
                        if not result['success']:
                            return BoolRequestResponse(success=False)
                    return BoolRequestResponse(success=True)
            else:
                raise UnknownCacheTypeException(f'Request id: {request_id} has unknown cache type {cacheType}')
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
