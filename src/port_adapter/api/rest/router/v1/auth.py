"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os

import grpc
from fastapi import Response
from grpc.beta.interfaces import StatusCode

from src.domain_model.AuthenticationService import AuthenticationService
import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.auth.AuthClient import AuthClient
from src.resource.logging.logger import logger


from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.param_functions import Body
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_200_OK, \
    HTTP_500_INTERNAL_SERVER_ERROR

# to get a string like this run:
# openssl rand -hex 32
from src.resource.proto._generated.auth_app_service_pb2 import AuthAppService_authenticateUserByNameAndPasswordRequest, \
    AuthAppService_authenticateUserByNameAndPasswordResponse
from src.resource.proto._generated.auth_app_service_pb2_grpc import AuthAppServiceStub

router = APIRouter()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14400
SECRET_TOKEN = os.getenv('SECRET_TOKEN', None)

fakeUserDb = {
    "arkan": {
        "username": "arkan",
        "fullName": "Arkan M. Gerges",
        "email": "arkan.m.gerges@gmail.com",
        "hashedPassword": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")


class CustomHttpBearer(HTTPBearer):
    def __init__(self):
        super().__init__()

    async def __call__(self, request: Request):
        ret = await super().__call__(request)
        authClient = AuthClient()
        Client.token = ret.credentials
        if ret is not None and not authClient.isAuthenticated(token=ret.credentials):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials",
            )



@router.post("/authenticate", summary='Authenticate user', status_code=status.HTTP_200_OK)
async def authenticate(*,
                username: str = Body(..., description='Username used for authentication'),
                password: str = Body(..., description='Password used for authentication')):
                                                   # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    #backgroundTasks.add_task(_customFunc, args)
    # return f'you entered: username: {username}, password: {password}'
    try:
        client = AuthClient()
        return client.authenticateUserByNameAndPassword(name=username, password=password)
    except grpc.RpcError as e:
        if e.code() == StatusCode.NOT_FOUND:
            return Response(status_code=HTTP_401_UNAUTHORIZED)
        else:
            logger.error(
                f'[{authenticate.__module__}.{authenticate.__qualname__}] - error response for username: {username}, e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

