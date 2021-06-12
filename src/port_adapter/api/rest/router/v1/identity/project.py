"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.identity.project.ProjectClient import (
    ProjectClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.Project import (
    ProjectDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.Projects import Projects
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_project_py__getProjects, "Get Projects", "http(s)", "Get all projects")
c4model:Rel(api__identity_project_py__getProjects, identity__grpc__ProjectAppServiceListener__projects, "Get projects", "grpc")
"""


@router.get(path="", summary="Get all projects", response_model=Projects)
async def getProjects(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.projects(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getProjects.__module__}.{getProjects.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_project_py__getProject, "Get Project", "http(s)", "Get project by id")
c4model:Rel(api__identity_project_py__getProject, identity__grpc__ProjectAppServiceListener__projectById, "Get a project by id", "grpc")
"""


@router.get(
    path="/{project_id}", summary="Get project", response_model=ProjectDescriptor
)
@OpenTelemetry.fastApiTraceOTel
async def getProject(
    *,
    project_id: str = Path(
        ..., description="Project id that is used to fetch project data"
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a Project by id"""
    try:
        client = ProjectClient()
        return client.projectById(projectId=project_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getProject.__module__}.{getProject.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_project_py__create, "Create Project", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_project_py__create__api_command_topic, "CommonCommandConstant.CREATE_PROJECT.value", "api command topic", "")
c4model:Rel(api__identity_project_py__create, api__identity_project_py__create__api_command_topic, "CommonCommandConstant.CREATE_PROJECT.value", "message")
"""


@router.post("", summary="Create a new project", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createProject(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="Title of the project", embed=True),
):
    reqId = RequestIdGenerator.generateListId(2)
    producer = AppDi.instance.get(SimpleProducer)
    client = ProjectClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_PROJECT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"project_id": client.newId(), "name": name}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}

