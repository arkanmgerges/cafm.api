"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from src.resource.logging.logger import logger
from typing import List

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

from src.port_adapter.api.rest.model.request.UserGroup import UserGroup
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all userGroups', response_model=List[UserGroup])
async def getAllUserGroups(*, _=Depends(CustomHttpBearer())):
    """Return all user groups
    """
    try:
        return []
    except:
        logger
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{userGroupId}/", summary='Get userGroup',
            response_model=UserGroup)
async def getUserGroup(*, userGroupId: str = Query(...,
                                           description='UserGroup id that is used to fetch user group data'),
                    _=Depends(CustomHttpBearer())):
    """Get a UserGroup by id
    """
    try:
        return UserGroup()
    except:
        logger.warning(traceback.format_exc())
        return UserGroup()


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new user group', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                title: str = Body(..., description='Title of the user group',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

