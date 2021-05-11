"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from typing import List
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
from src.port_adapter.api.rest.grpc.v1.project.project.ProjectClient import (
    ProjectClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.Building import Building
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevel import (
    BuildingLevel,
)
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRooms import (
    BuildingLevelRooms,
)
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevels import (
    BuildingLevels,
)
from src.port_adapter.api.rest.model.response.v1.project.Buildings import Buildings
from src.port_adapter.api.rest.model.response.v1.project.Project import (
    ProjectDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.Projects import Projects
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

# region Project
"""
c4model|cb|api:Component(api__project_project_py__getProjects, "Get Projects", "http(s)", "Get all projects")
c4model:Rel(api__project_project_py__getProjects, project__grpc__ProjectAppServiceListener__projects, "Get projects", "grpc")
"""


@router.get(path="", summary="Get all projects", response_model=Projects)
@OpenTelemetry.fastApiTraceOTel
async def getProjects(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.projects(
            resultFrom=result_from, resultSize=result_size, order=order
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
c4model|cb|api:Component(api__project_project_py__getProject, "Get a Project", "http(s)", "Get all projects")
c4model:Rel(api__project_project_py__getProject, project__grpc__ProjectAppServiceListener__projectById, "Get a project", "grpc")
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
c4model|cb|api:Component(api__project_project_py__update, "Update Project", "http(s)", "")
c4model|cb|api:ComponentQueue(api__project_project_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PROJECT.value", "api command topic", "")
c4model:Rel(api__project_project_py__update, api__project_project_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PROJECT.value", "message")
"""


@router.put("/{project_id}", summary="Update a project", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateProject(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(
        ..., description="Project id that is used in order to update the project"
    ),
    name: str = Body(..., description="Title of the project", embed=True),
    city_id: str = Body(..., description="City id of this project", embed=True),
    country_id: str = Body(..., description="Country id of this project", embed=True),
    address_line: str = Body(
        ..., description="Address line of the project", embed=True
    ),
    address_line_two: str = Body(
        ..., description="Second address line of the project", embed=True
    ),
    beneficiary_id: str = Body(
        ..., description="The id of the beneficiary", embed=True
    ),
    # state: str = Body(..., description="The state of the project", embed=True),
    # Note: Change of the project's state is not allowed here; changeProjectState should be used instead
):
    reqId = RequestIdGenerator.generateListId(2)
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_PROJECT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "name": name,
                    "city_id": city_id,
                    "country_id": country_id,
                    "address_line": address_line,
                    "address_line_two": address_line_two,
                    "beneficiary_id": beneficiary_id,
                    # "state": state,
                }
            ),
            external=[],
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{project_id}", summary="Parital update a project", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateProject(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(
        ..., description="Project id that is used in order to update the project"
    ),
    name: str = Body(None, description="Title of the project", embed=True),
    city_id: str = Body(None, description="City id of this project", embed=True),
    country_id: str = Body(None, description="Country id of this project", embed=True),
    address_line: str = Body(
        None, description="Address line of the project", embed=True
    ),
    address_line_two: str = Body(
        None, description="Second address line of the project", embed=True
    ),
    beneficiary_id: str = Body(
        None, description="The id of the beneficiary", embed=True
    ),
    start_date: str = Body(
        None, description="The start date of the project", embed=True
    ),
    # state: str = Body(None, description="The state of the project", embed=True),
    # Note: Change of the project's state is not allowed here; changeProjectState should be used instead
    developer_name: str = Body(None, description="Developer company name", embed=True),
    developer_city_id: int = Body(None, description="Developer city id", embed=True),
    developer_country_id: int = Body(
        None, description="Developer country id", embed=True
    ),
    developer_address_line_one: str = Body(
        None, description="Developer address line one", embed=True
    ),
    developer_address_line_two: str = Body(
        None, description="Developer address line two", embed=True
    ),
    developer_contact: str = Body(
        None, description="Developer representative", embed=True
    ),
    developer_email: str = Body(None, description="Developer email", embed=True),
    developer_phone_number: str = Body(
        None, description="Developer phone number", embed=True
    ),
    developer_warranty: str = Body(
        None, description="Developer warranty file url", embed=True
    ),
):
    reqId = RequestIdGenerator.generateListId(2)
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_PROJECT.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "name": name,
                    "city_id": city_id,
                    "country_id": country_id,
                    "address_line": address_line,
                    "address_line_two": address_line_two,
                    "beneficiary_id": beneficiary_id,
                    "start_date": start_date,
                    # "state": state,
                    "developer_name": developer_name,
                    "developer_city_id": developer_city_id,
                    "developer_country_id": developer_country_id,
                    "developer_address_line_one": developer_address_line_one,
                    "developer_address_line_two": developer_address_line_two,
                    "developer_contact": developer_contact,
                    "developer_email": developer_email,
                    "developer_phone_number": developer_phone_number,
                    "developer_warranty": developer_warranty,
                }
            ),
            external=[],
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


# endregion

# region Building
"""
c4model|cb|api:Component(api__project_project_py__getBuildings, "Get Buildings", "http(s)", "Get all buildings")
c4model:Rel(api__project_project_py__getBuildings, project__grpc__ProjectAppServiceListener__buildings, "Get buildings", "grpc")
"""


@router.get(
    path="/{project_id}/buildings",
    summary="Get all buildings",
    response_model=Buildings,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildings(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,name:desc"),
    include: List[str] = Query(
        "", description='values: "building_level", "building_level_room"'
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.buildings(
            resultFrom=result_from,
            resultSize=result_size,
            order=order,
            include=include,
            projectId=project_id,
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
c4model|cb|api:Component(api__project_project_py__getBuildingById, "Get Building", "http(s)", "Get building")
c4model:Rel(api__project_project_py__getBuildingById, project__grpc__ProjectAppServiceListener__building, "Get building", "grpc")
"""


@router.get(
    path="/{project_id}/buildings/{building_id}",
    summary="Get building",
    response_model=Building,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildingById(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    building_id: str = Path(..., description="building id that is used to fetch data"),
    include: List[str] = Query(
        "", description='values: "building_level", "building_level_room"'
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        return client.buildingById(include=include, id=building_id)
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
c4model|cb|api:Component(api__project_project_py__createBuilding, "Create Building", "http(s)", "")
c4model:Rel(api__project_project_py__createBuilding, project__messaging_project_command_handler__CreateBuildingHandler, "CommonCommandConstant.CREATE_BUILDING.value", "message")
"""


@router.post(
    "/{project_id}/buildings", summary="Create building", status_code=status.HTTP_200_OK
)
@OpenTelemetry.fastApiTraceOTel
async def createBuilding(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    name: str = Body(..., description="Building name", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    client = ProjectClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "building_id": client.newBuildingId(),
                    "project_id": project_id,
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__deleteBuilding, "Delete Building", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuilding, project__messaging_project_command_handler__DeleteBuildingHandler, "CommonCommandConstant.DELETE_BUILDING.value", "message")
"""


@router.delete(
    "/{project_id}/buildings/{building_id}",
    summary="Delete building",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuilding(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__updateBuilding, "Update Building", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuilding, project__messaging_project_command_handler__UpdateBuildingHandler, "CommonCommandConstant.UPDATE_BUILDING.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}",
    summary="Update building",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateBuilding(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    name: str = Body(..., description="Building name", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# endregion

# region Building Level
"""
c4model|cb|api:Component(api__project_project_py__getBuildingLevels, "Get Building Levels", "http(s)", "Get building levels")
c4model:Rel(api__project_project_py__getBuildingLevels, project__grpc__ProjectAppServiceListener__buildingLevels, "Get building levels", "grpc")
"""


@router.get(
    path="/{project_id}/buildings/{building_id}/building_levels",
    summary="Get building levels",
    response_model=BuildingLevels,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildingLevels(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    building_id: str = Path(..., description="Building id that is used to fetch data"),
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,name:desc"),
    include: List[str] = Query("", description='values: "building_level_room"'),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.buildingLevels(
            resultFrom=result_from,
            resultSize=result_size,
            order=order,
            include=include,
            buildingId=building_id,
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
c4model|cb|api:Component(api__project_project_py__getBuildingLevelById, "Get Building Level by id", "http(s)", "Get building level by id")
c4model:Rel(api__project_project_py__getBuildingLevelById, project__grpc__ProjectAppServiceListener__buildingLevelById, "Get building level by id", "grpc")
"""


@router.get(
    path="/{project_id}/buildings/{building_id}/building_levels/{building_level_id}",
    summary="Get building level by id",
    response_model=BuildingLevel,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildingLevelById(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    building_id: str = Path(..., description="building id that is used to fetch data"),
    building_level_id: str = Path(
        ..., description="building level id that is used to fetch data"
    ),
    include: List[str] = Query("", description='values: "building_level_room"'),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        return client.buildingLevelById(include=include, id=building_level_id)
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
c4model|cb|api:Component(api__project_project_py__createBuildingLevel, "Create Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__createBuildingLevel, project__messaging_project_command_handler__CreateBuildingLevelHandler, "CommonCommandConstant.CREATE_BUILDING_LEVEL.value", "message")
"""


@router.post(
    "/{project_id}/buildings/{building_id}/building_levels",
    summary="Add level to building",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def createBuildingLevel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    name: str = Body(..., description="Building level name", embed=True),
    is_sublevel: bool = Body(None, description="Is it a sublevel", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    client = ProjectClient()
    is_sublevel = is_sublevel if is_sublevel is not None else False
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_BUILDING_LEVEL.value,
            metadata=json.dumps({"token": Client.token, "msg_key": building_id}),
            data=json.dumps(
                {
                    "building_level_id": client.newBuildingLevelId(),
                    "project_id": project_id,
                    "building_id": building_id,
                    "name": name,
                    "is_sublevel": is_sublevel,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__deleteBuildingLevel, "Delete Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuildingLevel, project__messaging_project_command_handler__DeleteBuildingLevelHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL.value", "message")
"""


@router.delete(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}",
    summary="Delete building level",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuildingLevel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_BUILDING_LEVEL.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__updateBuildingLevel, "Update Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuildingLevel, project__messaging_project_command_handler__UpdateBuildingLevelHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}",
    summary="Update building level",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateBuildingLevel(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
    name: str = Body(..., description="Building name", embed=True),
    is_sublevel: bool = Body(None, description="Is it a sublevel", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    is_sublevel = is_sublevel if is_sublevel is not None else False
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_BUILDING_LEVEL.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "is_sublevel": is_sublevel,
                    "name": name,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__linkBuildingLevelToBuilding, "Link Building Level to Building", "http(s)", "")
c4model:Rel(api__project_project_py__linkBuildingLevelToBuilding, project__messaging_project_command_handler__LinkBuildingLevelToBuildingHandler, "CommonCommandConstant.LINK_BUILDING_LEVEL_TO_BUILDING.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/link",
    summary="Link building level to building",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def linkBuildingLevelToBuilding(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.LINK_BUILDING_LEVEL_TO_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__unlinkBuildingLevelFromBuilding, "Unlink Building Level from Building", "http(s)", "")
c4model:Rel(api__project_project_py__unlinkBuildingLevelFromBuilding, project__messaging_project_command_handler__UnlinkBuildingLevelFromBuildingHandler, "CommonCommandConstant.UNLINK_BUILDING_LEVEL_FROM_BUILDING.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/unlink",
    summary="Unlink building level from building",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def unlinkBuildingLevelFromBuilding(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UNLINK_BUILDING_LEVEL_FROM_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# endregion

# region Building Level Room
"""
c4model|cb|api:Component(api__project_project_py__getBuildingLevelRooms, "Get Building Level rooms", "http(s)", "Get building level rooms")
c4model:Rel(api__project_project_py__getBuildingLevelRooms, project__grpc__ProjectAppServiceListener__buildingLevelRooms, "Get building level rooms", "grpc")
"""


@router.get(
    path="/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms",
    summary="Get building level rooms",
    response_model=BuildingLevelRooms,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildingLevelRooms(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    building_id: str = Path(..., description="Building id that is used to fetch data"),
    building_level_id: str = Path(
        ..., description="Building level id that is used to fetch data"
    ),
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    order: str = Query("", description="e.g. id:asc,name:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.buildingLevelRooms(
            resultFrom=result_from,
            resultSize=result_size,
            order=order,
            buildingLevelId=building_level_id,
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
c4model|cb|api:Component(api__project_project_py__getBuildingLevelRoomById, "Get Building Level room by id", "http(s)", "Get building level room by id")
c4model:Rel(api__project_project_py__getBuildingLevelRoomById, project__grpc__ProjectAppServiceListener__buildingLevelRoomById, "Get building level room by id", "grpc")
"""


@router.get(
    path="/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms/{building_level_room_id}",
    summary="Get building level room by id",
    response_model=BuildingLevelRoom,
)
@OpenTelemetry.fastApiTraceOTel
async def getBuildingLevelRoomById(
    *,
    project_id: str = Path(..., description="Project id that is used to fetch data"),
    building_id: str = Path(..., description="building id that is used to fetch data"),
    building_level_id: str = Path(
        ..., description="building level id that is used to fetch data"
    ),
    building_level_room_id: str = Path(
        ..., description="building level room id that is used to fetch data"
    ),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectClient()
        return client.buildingLevelRoomById(id=building_level_room_id)
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
c4model|cb|api:Component(api__project_project_py__createBuildingLevelRoom, "Create Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__createBuildingLevelRoom, project__messaging_project_command_handler__CreateBuildingLevelRoomHandler, "CommonCommandConstant.CREATE_BUILDING_LEVEL_ROOM.value", "message")
"""


@router.post(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms",
    summary="Add room to building level",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def createBuildingLevelRoom(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
    name: str = Body(..., description="Building level room name", embed=True),
    description: str = Body(
        ..., description="Building level room description", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    client = ProjectClient()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_BUILDING_LEVEL_ROOM.value,
            metadata=json.dumps({"token": Client.token, "msg_key": building_level_id}),
            data=json.dumps(
                {
                    "building_level_room_id": client.newBuildingLevelRoomId(),
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "name": name,
                    "description": description,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__deleteBuildingLevelRoom, "Delete Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuildingLevelRoom, project__messaging_project_command_handler__DeleteBuildingLevelRoomHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL_ROOM.value", "message")
"""


@router.delete(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms/{building_level_room_id}",
    summary="Delete building level room",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuildingLevelRoom(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
    building_level_room_id: str = Path(..., description="Building level room id"),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_BUILDING_LEVEL_ROOM.value,
            metadata=json.dumps({"token": Client.token, "msg_key": building_level_id}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "building_level_room_id": building_level_room_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__updateBuildingLevelRoom, "Update Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuildingLevelRoom, project__messaging_project_command_handler__UpdateBuildingLevelRoomHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL_ROOM.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms/{building_level_room_id}",
    summary="Update building level room",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateBuildingLevelRoom(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
    building_level_room_id: str = Path(..., description="Building level room id"),
    name: str = Body(..., description="Building level room name", embed=True),
    description: str = Body(
        ..., description="Building level room description", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_BUILDING_LEVEL_ROOM.value,
            metadata=json.dumps({"token": Client.token, "msg_key": building_level_id}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "building_level_room_id": building_level_room_id,
                    "name": name,
                    "description": description,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}

    # @router.patch("/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms/{building_level_room_id}",
    #             summary='Update building level room', status_code=status.HTTP_200_OK)
    # @OpenTelemetry.fastApiTraceOTel
    # async def updateBuildingLevelRoom(*, _=Depends(CustomHttpBearer()),
    __ = (Depends(CustomAuthorization()),)


#                                   project_id: str = Path(..., description='Project id'),
#                                   building_id: str = Path(..., description='Building id'),
#                                   building_level_id: str = Path(..., description='Building level id'),
#                                   building_level_room_id: str = Path(..., description='Building level room id'),
#                                   name: str = Body(, description='Building level room name', embed=True),
#                                   description: str = Body(..., description='Building level room description',
#                                                           embed=True),
#                                   ):
#     reqId = RequestIdGenerator.generateId()
#     producer = AppDi.instance.get(SimpleProducer)
#     producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_BUILDING_LEVEL_ROOM.value,
#                                         metadata=json.dumps({"token": Client.token, "msg_key": building_level_id}),
#                                         data=json.dumps(
#                                             {'project_id': project_id,
#                                              'building_id': building_id,
#                                              'building_level_id': building_level_id,
#                                              'building_level_room_id': building_level_room_id,
#                                              'name': name,
#                                              'description': description
#                                              }), external=[]), schema=ProjectCommand.get_schema())
#     return {"request_id": reqId}


"""  
c4model|cb|api:Component(api__project_project_py__updateBuildingLevelRoomIndex, "Update Building Level Room Index", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuildingLevelRoomIndex, project__messaging_project_command_handler__UpdateBuildingLevelRoomIndexHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL_ROOM_INDEX.value", "message")
"""


@router.put(
    "/{project_id}/buildings/{building_id}/building_levels/{building_level_id}/building_level_rooms/{building_level_room_id}/update_index",
    summary="Update building level room index",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateBuildingLevelRoomIndex(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    building_id: str = Path(..., description="Building id"),
    building_level_id: str = Path(..., description="Building level id"),
    building_level_room_id: str = Path(..., description="Building level room id"),
    index: int = Body(..., description="Building level room index", embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_BUILDING_LEVEL_ROOM_INDEX.value,
            metadata=json.dumps({"token": Client.token, "msg_key": building_level_id}),
            data=json.dumps(
                {
                    "project_id": project_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "building_level_room_id": building_level_room_id,
                    "index": index,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# endregion


"""  
c4model|cb|api:Component(api__project_project_py__changeProjectState, "Change Project State", "http(s)", "")
c4model:Rel(api__project_project_py__changeProjectState, project__messaging_project_command_handler__ChangeProjectStateHandler, "CommonCommandConstant.CHANGE_PROJECT_STATE.value", "message")
"""


@router.post(
    "/{project_id}/change_state",
    summary="Change project state",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def changeProjectState(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    project_id: str = Path(..., description="Project id"),
    state: str = Body(
        ..., description="The state can be active and archived", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    state = state.lower()
    if state not in ["active", "archived"]:
        raise ValueError("Invalid state, it should be one of these: active, archived")
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CHANGE_PROJECT_STATE.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"project_id": project_id, "state": state}),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


# endregion
