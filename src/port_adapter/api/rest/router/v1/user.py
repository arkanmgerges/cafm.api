"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import traceback
import hashlib
from logging import Logger
from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends, Query, Body

import src.port_adapter.api.rest.AppDi as AppDi
from src.port_adapter.api.rest.model.User import User
from src.port_adapter.api.rest.model.request.User import User
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.Command import Command
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

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

    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=Command(id=str(uuid4()), name=CommandConstant.CREATE_USER.value, data=json.dumps(
        {'username': title, 'password': hashlib.sha256('pass'.encode()).hexdigest()})),
                     schema=Command.get_schema())
