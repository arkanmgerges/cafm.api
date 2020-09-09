"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.resource.AppDi as AppDi
from src.resource.api.model.request.UserGroup import UserGroup
from src.resource.api.router.v1.auth import currentActiveUser

router = APIRouter()


@router.get(path="/", summary='Get all userGroups', response_model=List[UserGroup])
async def getAllUserGroups(*, currentUserGroup: UserGroup = Depends(currentActiveUser)):
    """Return all user groups
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{userGroupId}/", summary='Get userGroup',
            response_model=UserGroup)
async def getUserGroup(*, userGroupId: str = Query(...,
                                           description='UserGroup id that is used to fetch user group data'),
                    currentUserGroup: UserGroup = Depends(currentActiveUser)):
    """Get a UserGroup by id
    """
    try:
        return UserGroup()
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return UserGroup()


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new user group', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, currentUserGroup: UserGroup = Depends(currentActiveUser),
                title: str = Body(..., description='Title of the user group',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

