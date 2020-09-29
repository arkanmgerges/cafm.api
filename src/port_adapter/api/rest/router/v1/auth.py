"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

# to get a string like this run:
# openssl rand -hex 32
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
        if ret is not None and ret.credentials != SECRET_TOKEN:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN,
                detail="Invalid authentication credentials",
            )
