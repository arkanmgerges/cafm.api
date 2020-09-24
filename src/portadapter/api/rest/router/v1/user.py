"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List
from uuid import uuid4

from src.portadapter.messaging.Producer import Producer
from src.portadapter.messaging.model.Command import Command, COMMANDS
from src.resource.logging.logger import logger

from fastapi import APIRouter, Depends, Query, Body

import src.portadapter.api.rest.AppDi as AppDi
from src.portadapter.api.rest.model.User import User
from src.portadapter.api.rest.model.request.User import User
from src.portadapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all users', response_model=List[User])
async def getAllUsers(*, _=Depends(CustomHttpBearer())):
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
                  _=Depends(CustomHttpBearer())):
    """Get a User by id
    """
    try:
        return User()
    except:
        logger.warning(traceback.format_exc())
        return User()


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new user')
async def create(*, title: str = Body(..., description='Title of the user', embed=True),
                 _=Depends(CustomHttpBearer()),
                 ):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
    producer = AppDi.instance.get(Producer)
    producer.produce(obj=Command(id=str(uuid4()), name=COMMANDS.CREATE_USER), objMap=Command.toMap,
                     schema=str(Command.get_schema()))
