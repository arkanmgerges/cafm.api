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

from src.port_adapter.api.rest.grpc.ou.OuClient import OuClient
from src.port_adapter.api.rest.model.request.Ou import Ou
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all ous', response_model=List[Ou])
async def getAllOus(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                    result_size: int = Query(10, description='Item count to be fetched'),
                    _=Depends(CustomHttpBearer())):
    """Return all ous
    """
    try:
        client = OuClient()
        return client.ous(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllOus.__module__}.{getAllOus.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{ou_id}/", summary='Get ou',
            response_model=Ou)
async def getOu(*, ou_id: str = Path(...,
                                     description='Ou id that is used to fetch ou data'),
                _=Depends(CustomHttpBearer())):
    """Get a Ou by id
    """
    try:
        client = OuClient()
        return client.ouById(ouId=ou_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getOu.__module__}.{getOu.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new ou', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the ou',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
