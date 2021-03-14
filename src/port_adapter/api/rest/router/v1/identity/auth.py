"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

import grpc
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from fastapi.param_functions import Body
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer
from grpc.beta.interfaces import StatusCode
from passlib.context import CryptContext
from starlette import status
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED, HTTP_500_INTERNAL_SERVER_ERROR

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.auth.AuthClient import AuthClient
from src.port_adapter.api.rest.helper.Validator import Validator
from src.resource.logging.logger import logger

# to get a string like this run:
# openssl rand -hex 32
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

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
        import src.port_adapter.AppDi as AppDi
        authClient = AppDi.instance.get(AuthClient)
        Client.token = ret.credentials
        if ret is not None and not authClient.isAuthenticated(token=ret.credentials):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials",
            )

"""
c4model|cb|api:Component(api__auth_py__authenticate, "Authenticate a user", "json/https", "Authenticate a user")
c4model:Rel(api__auth_py__authenticate, identity__grpc__AuthAppServiceListener__authenticateUserByEmailAndPassword, "Auth user & get token", "grpc call")
"""
@router.post("/authenticate", summary='Authenticate user', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def authenticate(*,
                       email: str = Body(..., description='Email used for authentication'),
                       password: str = Body(..., description='Password used for authentication')):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
    # return f'you entered: username: {username}, password: {password}'
    try:
        client = AuthClient()
        Validator.validateEmail(email, {'email': email})
        return client.authenticateUserByEmailAndPassword(email=email, password=password)
    except grpc.RpcError as e:
        if e.code() == StatusCode.NOT_FOUND:
            return Response(status_code=HTTP_401_UNAUTHORIZED)
        else:
            logger.error(
                f'[{authenticate.__module__}.{authenticate.__qualname__}] - error response for email: {email}, e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
        raise e

"""
c4model|cb|api:Component(api__auth_py__logout, "logout", "json/https", "logout a user")
c4model:Rel(api__auth_py__logout, identity__grpc__AuthAppServiceListener__logout, "Logout user by token", "grpc call")
"""
@router.post("/logout", summary='Logout user', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def logout(*,
                 token: str = Body(..., description='Username used for authentication', embed=True), ):
    try:
        client = AuthClient()
        client.logout(token=token)
    except Exception as e:
        return Response(status_code=HTTP_500_INTERNAL_SERVER_ERROR)
