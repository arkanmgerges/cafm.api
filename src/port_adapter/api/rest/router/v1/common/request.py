"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.port_adapter.api.rest.model.response.v1.identity.Request import (
    BoolRequestResponse,
    ResultRequestResponse,
)
from src.port_adapter.api.rest.resource.exception.InProgressException import (
    InProgressException,
)
from src.port_adapter.api.rest.resource.exception.NotFoundException import (
    NotFoundException,
)
from src.port_adapter.api.rest.resource.exception.UnknownCacheTypeException import (
    UnknownCacheTypeException,
)
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="/is_successful",
    summary="Check if the request has succeeded",
    response_model=BoolRequestResponse,
)
@OpenTelemetry.fastApiTraceOTel
async def isRequestSuccessful(
    *,
    request_id: str = Query(
        ..., description="Request id to check if it is succeeded or not"
    ),
    # _=Depends(CustomHttpBearer())
):
    """Return all roles"""
    try:
        import src.port_adapter.AppDi as AppDi

        cache = AppDi.instance.get(RedisCache)
        cacheClient = cache.client()
        cacheKey = f"{cache.cacheResponseKeyPrefix()}:{request_id}"
        split = request_id.split(":")
        if len(split) == 1:
            result = cacheClient.get(cacheKey)
            if result is None:
                raise NotFoundException(f"Request id: {request_id} not found")
            result = json.loads(result.decode("utf-8"))
            return BoolRequestResponse(success=result["success"])
        elif len(split) == 2:  # Bulk
            return _isSuccessfulWhenBulk(cacheClient=cacheClient, cacheKey=cacheKey, requestId=request_id)
        else:
            cacheType = split[0]
            if CacheType.valueToEnum(cacheType) == CacheType.LIST:
                return _isSuccessfulWhenListWithSuccessCount(cacheClient=cacheClient, cacheKey=cacheKey,
                                                             split=split, requestId=request_id)
            else:
                raise UnknownCacheTypeException(
                    f"Request id: {request_id} has unknown cache type {cacheType}"
                )
    except NotFoundException as e:
        raise NotFoundException(e.message)
    except InProgressException as e:
        raise e
    except Exception as e:
        logger.info(e)
        return BoolRequestResponse(success=False)


@router.get(
    path="/result",
    summary="Get the request id result",
    response_model=ResultRequestResponse,
)
@OpenTelemetry.fastApiTraceOTel
async def getRequestIdResult(
    *,
    request_id: str = Query(
        ..., description="Request id that is used to fetch the result"
    ),
    # _=Depends(CustomHttpBearer())
):
    try:
        import src.port_adapter.AppDi as AppDi

        cache = AppDi.instance.get(RedisCache)
        cacheClient = cache.client()
        cacheKey = f"{cache.cacheResponseKeyPrefix()}:{request_id}"
        split = request_id.split(":")
        # If it's only a key
        if len(split) == 1:
            result = cacheClient.get(cacheKey)
            if result is None:
                raise NotFoundException(f"Request id: {request_id} not found")
            result = json.loads(result.decode("utf-8"))
            return ResultRequestResponse(result=result["data"])
        # If it contains 2 segments, then it's a bulk
        elif len(split) == 2:  # Bulk
            return _resultWhenBulk(cacheClient=cacheClient, cacheKey=cacheKey, requestId=request_id)
        else:
            return _resultWhenListWithSuccessCount(cacheClient=cacheClient, cacheKey=cacheKey, split=split, requestId=request_id)
    except NotFoundException as e:
        raise NotFoundException(e.message)
    except InProgressException as e:
        raise e
    except Exception as e:
        logger.info(e)
        return JSONResponse(status_code=400, content={"detail": [{"msg": str(e)}]})

def _resultWhenBulk(cacheClient, cacheKey, requestId):
    items = cacheClient.lrange(cacheKey, 0, -1)
    resultItems = _resultForBulk(items)
    if _hasAtLeastOneFailed(items) or (resultItems["item_count"] == len(resultItems["items"])):
        resultItems = _resultForBulk(items)
        return ResultRequestResponse(result=resultItems)
    raise InProgressException(
        f"Request id: {requestId} is still in progress"
    )

def _isSuccessfulWhenBulk(cacheClient, cacheKey, requestId):
    items = cacheClient.lrange(cacheKey, 0, -1)
    if _hasAtLeastOneFailed(items):
        return BoolRequestResponse(success=False)
    else:
        resultItems = _resultForBulk(items)
        if resultItems["item_count"] == len(resultItems["items"]):
            return BoolRequestResponse(success=True)
        else:
            raise InProgressException(
                f"Request id: {requestId} is still in progress"
            )

def _isSuccessfulWhenListWithSuccessCount(cacheClient, cacheKey, split, requestId):
    items = cacheClient.lrange(cacheKey, 0, -1)
    if _hasAtLeastOneFailed(items):
        return BoolRequestResponse(success=False)
    else:
        _key = split[1]
        successRequired = int(split[2])
        if cacheClient.llen(cacheKey) == successRequired:
            items = cacheClient.lrange(cacheKey, 0, -1)
            if len(items) < successRequired:
                raise InProgressException(
                    f"Request id: {requestId} is still in progress"
                )
            return BoolRequestResponse(success=True)
    raise InProgressException(
        f"Request id: {requestId} is still in progress"
    )


def _resultWhenListWithSuccessCount(cacheClient, cacheKey, split, requestId):
    cacheType = split[0]
    if CacheType.valueToEnum(cacheType) == CacheType.LIST:
        items = cacheClient.lrange(cacheKey, 0, -1)
        if _hasAtLeastOneFailed(items):
            return ResultRequestResponse(result=_resultFromItems(items))
        else:
            _key = split[1]
            successRequired = int(split[2])
            if cacheClient.llen(cacheKey) == successRequired:
                items = cacheClient.lrange(cacheKey, 0, -1)
                if len(items) < successRequired:
                    raise InProgressException(
                        f"Request id: {requestId} is still in progress"
                    )
                return ResultRequestResponse(result=_resultFromItems(items))
            else:
                raise InProgressException(
                    f"Request id: {requestId} is still in progress"
                )
    else:
        raise UnknownCacheTypeException(
            f"Request id: {requestId} has unknown cache type {cacheType}"
        )

def _hasAtLeastOneFailed(items):
    for item in items:
        resultDict = json.loads(item.decode("utf-8"))
        if resultDict["success"] is False:
            return True
    return False

def _resultForBulk(items):
    resultItems = []
    itemCount = -1
    exceptionItems = []
    for item in items:
        resultDict = json.loads(item.decode("utf-8"))
        resultData = resultDict["data"]
        dataList = resultData["data"]
        for dataItem in dataList:
            if itemCount == -1:
                itemCount = resultData["item_count"]
            resultItems.append(dataItem)
        exceptionItem = resultData["exceptions"] if "exceptions" in resultData else None
        if exceptionItem is not None:
            exceptionItems.append(exceptionItem)

    resultItemsSorted = sorted(resultItems, key=lambda x: x["_index"])
    resultItemsCurated = list(map(lambda x: x["_request_data"], resultItemsSorted))

    return {'items': resultItemsCurated, 'item_count': itemCount, 'exceptions': exceptionItems}


def _resultFromItems(items):
    result = {"items": [], "item_count": 0}
    for item in items:
        resultDict = json.loads(item.decode("utf-8"))
        result["items"].append(
            {
                **resultDict["data"],
                "creator_service_name": resultDict["creator_service_name"],
            }
        )
        result["item_count"] += 1
    return result
