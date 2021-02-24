"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
import random
import traceback
from datetime import datetime

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.responses import JSONResponse

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.model.response.exception.Message import Message, ValidationMessage
from src.port_adapter.api.rest.resource.exception.InProgressException import InProgressException
from src.port_adapter.api.rest.resource.exception.ValidationErrorException import ValidationErrorException
from src.port_adapter.api.rest.router.v1.common import request as common_request
from src.port_adapter.api.rest.router.v1.identity import auth as id_auth, realm as id_realm, ou as id_ou, \
    user as id_user, role as id_role, user_group as id_user_group, project as id_project, \
    permission_context as id_permission_context, \
    permission as id_permission, assignment as id_assignment, access as id_access, country as id_country, \
    city as id_city
from src.port_adapter.api.rest.router.v1.project import project as project_project, user as project_user, \
    organization as project_organization, lookup as project_lookup, subcontractor as project_subcontractor
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.port_adapter.api.rest.router.v1.project.equipment.model import equipment_model as project_equipment_model
from src.port_adapter.api.rest.router.v1.project.manufacturer import manufacturer as project_manufacturer
from src.port_adapter.api.rest.router.v1.project.equipment.project_category import equipment_project_category as project_equipment_project_category
from src.port_adapter.api.rest.router.v1.project.equipment.category import equipment_category as project_equipment_category
from src.port_adapter.api.rest.router.v1.project.equipment.category.group import equipment_category_group as project_equipment_category_group

# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI(
    title='CAFM System Api Gateway',
    description='This system provides an entry point to the CAFM System',
    version='1.0.0',
    openapi_url='/api/v1/openapi.json'
)

openTelemetry = AppDi.instance.get(OpenTelemetry)


# FastAPIInstrumentor.instrument_app(app)

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

    @app.exception_handler(ValidationErrorException)
    async def validationExceptionHandler(request: Request, e: ValidationErrorException):
        return JSONResponse(content={"detail": [json.loads(str(e))]}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @app.exception_handler(ValueError)
    async def valueExceptionHandler(request: Request, e: ValueError):
        logger.warning(traceback.format_exc())
        return JSONResponse(content={"detail": [{"message": str(e)}]}, status_code=status.HTTP_400_BAD_REQUEST)

    @app.exception_handler(InProgressException)
    async def generalExceptionHandler(request: Request, e: Exception):
        logger.warning(traceback.format_exc())
        return JSONResponse(content={"detail": [{"message": str(e)}]},
                            status_code=status.HTTP_202_ACCEPTED)

    @app.exception_handler(Exception)
    async def generalExceptionHandler(request: Request, e: Exception):
        logger.warning(traceback.format_exc())
        return JSONResponse(content={"detail": [{"message": str(e)}]},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

addCustomExceptionHandlers(app)
if os.getenv('ENABLE_CORS', True):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        # allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

np.random.seed(int(datetime.utcnow().timestamp()))
random.seed(datetime.utcnow().timestamp())

# region Global
app.include_router(common_request.router, prefix="/v1/common/request", tags=["Common"],
                   responses={202: {"model": Message}, 400: {"model": Message}, 404: {"model": Message},
                              500: {"model": Message}})
# endregion

# region Identity
app.include_router(id_auth.router, prefix="/v1/identity/auth", tags=["Identity/Auth"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 422: {"model": ValidationMessage},
                              500: {"model": Message}})
app.include_router(id_realm.router, prefix="/v1/identity/realms", tags=["Identity/Realm"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_ou.router, prefix="/v1/identity/ous", tags=["Identity/OU"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_user.router, prefix="/v1/identity/users", tags=["Identity/User"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_role.router, prefix="/v1/identity/roles", tags=["Identity/Role"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_user_group.router, prefix="/v1/identity/user_groups", tags=["Identity/User Groups"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_project.router, prefix="/v1/identity/projects", tags=["Identity/Project"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_permission.router, prefix="/v1/identity/permissions", tags=["Identity/Permission"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_permission_context.router, prefix="/v1/identity/permission_contexts", tags=["Identity/Permission"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_assignment.router, prefix="/v1/identity/assignments", tags=["Identity/Assignment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_access.router, prefix="/v1/identity/accesses", tags=["Identity/Access"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_country.router, prefix="/v1/identity/countries", tags=["Identity/Country"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(id_city.router, prefix="/v1/identity/cities", tags=["Identity/City"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
# endregion

# region Project
app.include_router(project_project.router, prefix="/v1/project/projects", tags=["Project/Project"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_user.router, prefix="/v1/project/users", tags=["Project/User"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_lookup.router, prefix="/v1/project/lookups", tags=["Project/Lookup"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_organization.router, prefix="/v1/project/organizations", tags=["Project/Organization"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_subcontractor.router, prefix="/v1/project/subcontractors", tags=["Project/SubContractor"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_equipment_model.router, prefix="/v1/project/equipment_models", tags=["Project/Equipment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_manufacturer.router, prefix="/v1/project/manufacturers", tags=["Project/Manufacturer"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_equipment_project_category.router, prefix="/v1/project/equipment_project_categories", tags=["Project/Equipment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_equipment_category.router, prefix="/v1/project/equipment_categories", tags=["Project/Equipment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
app.include_router(project_equipment_category_group.router, prefix="/v1/project/equipment_category_groups", tags=["Project/Equipment"],
                   responses={400: {"model": Message}, 404: {"model": Message}, 500: {"model": Message}})
# endregion
