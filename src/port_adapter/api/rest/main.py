"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import random
import traceback

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.responses import JSONResponse

from src.port_adapter.api.rest.model.response.exception.Message import Message
from src.port_adapter.api.rest.router.v1 import auth, realm, ou, user, role, user_group, project, permission_context, \
    permission, request, assignment, access
from src.resource.logging.logger import logger

app = FastAPI(
    title='CAFM System Api Gateway',
    description='This system provides an entry point to the CAFM System',
    version='1.0.0',
    openapi_url='/api/v1/openapi.json'
)


def addCustomExceptionHandlers(app):
    from fastapi import Request
    # from src.domain_model.exception.ItemDoesNotExistException import ItemDoesNotExistException
    # from src.domain_model.exception.UserDoesNotExistException import UserDoesNotExistException

    # @app.exception_handler(ItemDoesNotExistException)
    # async def itemExceptionHandler(request: Request, e: ItemDoesNotExistException):
    #     logger = AppDi.instance.get(Logger)
    #     logger.warning(traceback.format_exc())
    #     return JSONResponse(content={"detail": [{"msg": str(e)}]}, status_code=status.HTTP_404_NOT_FOUND)
    #
    # @app.exception_handler(UserDoesNotExistException)
    # async def userExceptionHandler(request: Request, e: UserDoesNotExistException):
    #     logger = AppDi.instance.get(Logger)
    #     logger.warning(traceback.format_exc())
    #     return JSONResponse(content={"detail": [{"msg": str(e)}]}, status_code=status.HTTP_404_NOT_FOUND)

    @app.exception_handler(ValueError)
    async def valueExceptionHandler(request: Request, e: ValueError):
        logger.warning(traceback.format_exc())
        return JSONResponse(content={"detail": [{"msg": str(e)}]}, status_code=status.HTTP_400_BAD_REQUEST)

    @app.exception_handler(Exception)
    async def generalExceptionHandler(request: Request, e: Exception):
        logger.warning(traceback.format_exc())
        return JSONResponse(content={"detail": [{"msg": str(e)}]}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


addCustomExceptionHandlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

np.random.seed(0)
random.seed(0)

app.include_router(auth.router, prefix="/v1/auth", tags=["Auth"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(request.router, prefix="/v1/request", tags=["Request"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(realm.router, prefix="/v1/realms", tags=["Realm"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(ou.router, prefix="/v1/ous", tags=["OU"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(user.router, prefix="/v1/users", tags=["User"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(role.router, prefix="/v1/roles", tags=["Role"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(user_group.router, prefix="/v1/user_groups", tags=["User Groups"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project.router, prefix="/v1/projects", tags=["Project"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(permission.router, prefix="/v1/permissions", tags=["Permission"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(permission_context.router, prefix="/v1/permission_contexts", tags=["Permission"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(assignment.router, prefix="/v1/assignments", tags=["Assignment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(access.router, prefix="/v1/accesses", tags=["Access"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
