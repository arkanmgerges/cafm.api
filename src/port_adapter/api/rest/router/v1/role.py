"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List
from src.resource.logging.logger import logger

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.port_adapter.api.rest.AppDi as AppDi
from src.port_adapter.api.rest.model.request.Role import Role
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all roles', response_model=List[Role])
async def getAllRoles(*, _=Depends(CustomHttpBearer())):
    """Return all roles
    """
    try:
        return []
    except:
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{roleId}/", summary='Get role',
            response_model=Role)
async def getRole(*, roleId: str = Query(...,
                                           description='Role id that is used to fetch role data'),
                    _=Depends(CustomHttpBearer())):
    """Get a Role by id
    """
    try:
        return Role()
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return Role()


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

