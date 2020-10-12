"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

from src.port_adapter.api.rest.grpc.user.UserClient import UserClient
from src.port_adapter.api.rest.model.request.User import User, UserDescriptor
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all users', response_model=List[UserDescriptor])
async def getAllUsers(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                      result_size: int = Query(10, description='Item count to be fetched'),
                      _=Depends(CustomHttpBearer())):
    """Return all users
    """
    try:
        client = UserClient()
        return client.users(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllUsers.__module__}.{getAllUsers.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{user_id}/", summary='Get user',
            response_model=UserDescriptor)
async def getUser(*, user_id: str = Path(...,
                                         description='User id that is used to fetch user data'),
                  _=Depends(CustomHttpBearer())):
    """Get a User by id
    """
    try:
        client = UserClient()
        return client.userById(userId=user_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUser.__module__}.{getUser.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new user', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the user',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
    # authService:AuthenticationService = AppDi.instance.get(AuthenticationService)
    # producer = AppDi.instance.get(SimpleProducer)
    # producer.produce(obj=ApiCommand(id=str(uuid4()), name=CommandConstant.CREATE_USER.value, data=json.dumps(
    #     {'username': username, 'password': authService.hashPassword(password=password)})),
    #                  schema=ApiCommand.get_schema())