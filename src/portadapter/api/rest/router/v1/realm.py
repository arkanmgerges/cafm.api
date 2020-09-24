"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List
from src.resource.logging.logger import logger

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.portadapter.api.rest.AppDi as AppDi
from src.portadapter.api.rest.model.request.Realm import Realm
from src.portadapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all realms', response_model=List[Realm])
async def getAllRealms(*, _=Depends(CustomHttpBearer())):
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
                    _=Depends(CustomHttpBearer())):
    """Get a Realm by id
    """
    try:
        return Realm()
    except:
        logger.warning(traceback.format_exc())
        return Realm()


def _customFunc(args):
    pass

@router.post("/create", summary='Create a new realm', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                title: str = Body(..., description='Title of the realm',
                                                   )):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)

