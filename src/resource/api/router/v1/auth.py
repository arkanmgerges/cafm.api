"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from passlib.context import CryptContext

from src.resource.api.model.Token import Token
from src.resource.api.model.TokenData import TokenData
from src.resource.api.model.User import User
from src.resource.api.model.UserInDb import UserInDb

# to get a string like this run:
# openssl rand -hex 32
router = APIRouter()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 14400

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


def verifyPassword(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)


def userByUsername(db, username: str):
    if username in db:
        userDict = db[username]
        return UserInDb(**userDict)


def authenticateUser(fakeDb, username: str, password: str):
    user = userByUsername(fakeDb, username)
    if not user:
        return False
    if not verifyPassword(password, user.hashedPassword):
        return False
    return user


def createAccessToken(*, data: dict, expiresDelta: timedelta = None):
    toEncode = data.copy()
    if expiresDelta:
        expire = datetime.utcnow() + expiresDelta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    toEncode.update({"exp": expire})
    encodedJwt = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodedJwt


async def verifyAuthToken(token: str = Depends(oauth2Scheme)):
    credentialException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentialException
        tokenData = TokenData(username=username)
    except PyJWTError:
        raise credentialException
    user = userByUsername(fakeUserDb, username=tokenData.username)
    if user is None:
        raise credentialException
    return user


async def currentActiveUser(user: User = Depends(verifyAuthToken)):
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


@router.post("/token", response_model=Token, summary='Login for auth token')
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    user = authenticateUser(fakeUserDb, formData.username, formData.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    accessTokenExpirationTimeDelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    accessToken = createAccessToken(
        data={"sub": user.username}, expiresDelta=accessTokenExpirationTimeDelta
    )
    # Use snake case in order to be compatible with oath2 specification
    return {"access_token": accessToken, "token_type": "bearer"}
