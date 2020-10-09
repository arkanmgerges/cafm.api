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
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from src.port_adapter.api.rest.grpc.realm.RealmClient import RealmClient
from src.port_adapter.api.rest.model.request.Realm import Realm
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all realms', response_model=List[Realm])
async def getAllRealms(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                       result_size: int = Query(10, description='Item count to be fetched'),
                       _=Depends(CustomHttpBearer())):
    """Return all realms
    """
    try:
        client = RealmClient()
        return client.realms(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllRealms.__module__}.{getAllRealms.__qualname__}] - error response e: {e}')
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
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getRealm.__module__}.{getRealm.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new realm', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the realm',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
