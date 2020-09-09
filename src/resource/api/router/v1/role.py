"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.resource.AppDi as AppDi
from src.resource.api.model.request.Role import Role
from src.resource.api.router.v1.auth import currentActiveUser

router = APIRouter()


@router.get(path="/", summary='Get all roles', response_model=List[Role])
async def getAllRoles(*, currentRole: Role = Depends(currentActiveUser)):
    """Return all roles
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{roleId}/", summary='Get role',
            response_model=Role)
async def getRole(*, roleId: str = Query(...,
                                           description='Role id that is used to fetch role data'),
                    currentRole: Role = Depends(currentActiveUser)):
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
async def create(*, currentRole: Role = Depends(currentActiveUser),
                title: str = Body(..., description='Title of the role',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

