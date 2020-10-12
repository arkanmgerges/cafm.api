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

from src.port_adapter.api.rest.grpc.user_group.UserGroupClient import UserGroupClient
from src.port_adapter.api.rest.model.request.UserGroup import UserGroup
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all userGroups', response_model=List[UserGroup])
async def getAllUserGroups(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                           result_size: int = Query(10, description='Item count to be fetched'),
                           _=Depends(CustomHttpBearer())):
    """Return all userGroups
    """
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
                f'[{getAllUserGroups.__module__}.{getAllUserGroups.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{userGroup_id}/", summary='Get userGroup',
            response_model=UserGroup)
async def getUserGroup(*, userGroup_id: str = Path(...,
                                                   description='UserGroup id that is used to fetch userGroup data'),
                       _=Depends(CustomHttpBearer())):
    """Get a UserGroup by id
    """
    try:
        client = UserGroupClient()
        return client.userGroupById(userGroupId=userGroup_id)
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


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new userGroup', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the userGroup',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
