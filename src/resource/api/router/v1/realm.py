"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Body
from starlette import status
from starlette.background import BackgroundTasks
from starlette.responses import Response

import src.resource.AppDi as AppDi
from src.resource.api.model.User import User
from src.resource.api.model.request.Realm import Realm
from src.resource.api.router.v1.auth import currentActiveUser

router = APIRouter()


@router.get(path="/", summary='Get all realms', response_model=List[Realm])
async def getAllRealms(*, currentUser: User = Depends(currentActiveUser)):
    """Return all realms
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{realmId}/", summary='Get realm',
            response_model=Realm)
async def getRealm(*, realmId: str = Query(...,
                                           description='Realm id that is used to fetch realm data'),
                    currentUser: User = Depends(currentActiveUser)):
    """Get a Realm by id
    """
    try:
        return Realm()
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return Realm()


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new realm', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, currentUser: User = Depends(currentActiveUser),
                title: str = Body(..., description='Title of the realm',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

