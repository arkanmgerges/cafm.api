"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List

from grpc.beta.interfaces import StatusCode
from fastapi import Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

import grpc
from src.port_adapter.api.rest.grpc.role.RoleClient import RoleClient
from src.resource.logging.logger import logger

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.model.request.Role import Role
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all roles', response_model=List[Role])
async def getAllRoles(*, _=Depends(CustomHttpBearer())):
    """Return all roles
    """
    try:
        client = RoleClient()
        return client.roles()
    except grpc.RpcError as e:
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllRoles.__module__}.{getAllRoles.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{roleId}/", summary='Get role',
            response_model=Role)
async def getRole(*, roleId: str = Query(...,
                                           description='Role id that is used to fetch role data'),
                    _=Depends(CustomHttpBearer())):
    """Get a Role by id
    """
    pass


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new role', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                title: str = Body(..., description='Title of the role',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

