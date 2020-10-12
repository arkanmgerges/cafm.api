"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

from src.port_adapter.api.rest.grpc.resource_type.ResourceTypeClient import ResourceTypeClient
from src.port_adapter.api.rest.model.request.ResourceType import ResourceType
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all resourceTypes', response_model=List[ResourceType])
async def getAllResourceTypes(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                              result_size: int = Query(10, description='Item count to be fetched'),
                              _=Depends(CustomHttpBearer())):
    """Return all resourceTypes
    """
    try:
        client = ResourceTypeClient()
        return client.resourceTypes(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllResourceTypes.__module__}.{getAllResourceTypes.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{resourceType_id}/", summary='Get resourceType',
            response_model=ResourceType)
async def getResourceType(*, resourceType_id: str = Path(...,
                                                         description='ResourceType id that is used to fetch resourceType data'),
                          _=Depends(CustomHttpBearer())):
    """Get a ResourceType by id
    """
    try:
        client = ResourceTypeClient()
        return client.resourceTypeById(resourceTypeId=resourceType_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getResourceType.__module__}.{getResourceType.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new resourceType', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the resourceType',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
