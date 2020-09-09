"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List, Optional, Union

from fastapi import APIRouter, Depends, Query, Body
from starlette import status
from starlette.background import BackgroundTasks
from starlette.responses import Response

import src.resource.AppDi as AppDi
from src.resource.api.model.User import User
from src.resource.api.model.request.User import User
from src.resource.api.router.v1.auth import currentActiveUser

router = APIRouter()


@router.get(path="/", summary='Get all users', response_model=List[User])
async def getAllUsers(*, currentUser: User = Depends(currentActiveUser)):
    """Return all users
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{userId}/", summary='Get user',
            response_model=User)
async def getUser(*, userId: str = Query(...,
                                           description='User id that is used to fetch user data'),
                    currentUser: User = Depends(currentActiveUser)):
    """Get a User by id
    """
    try:
        return User()
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return User()


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new user', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, currentUser: User = Depends(currentActiveUser),
                title: str = Body(..., description='Title of the user',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

