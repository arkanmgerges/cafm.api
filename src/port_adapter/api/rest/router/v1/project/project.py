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
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.project.ProjectClient import ProjectClient
from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Projects import Projects
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all projects', response_model=Projects)
@OpenTelemetry.fastApiTraceOTel
async def getProjects(*,
                      result_from: int = Query(0, description='Starting offset for fetching data'),
                      result_size: int = Query(10, description='Item count to be fetched'),
                      order: str = Query('', description='e.g. name:asc,age:desc'),
                      _=Depends(CustomHttpBearer())):
    try:
        client = ProjectClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.projects(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getProjects.__module__}.{getProjects.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{project_id}", summary='Get project',
            response_model=ProjectDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getProject(*, project_id: str = Path(...,
                                               description='Project id that is used to fetch project data'),
                     _=Depends(CustomHttpBearer())):
    """Get a Project by id
    """
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
                f'[{getProject.__module__}.{getProject.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__project_project_py__update, "Update Project", "http(s)", "")
c4model|cb|api:ComponentQueue(api__project_project_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PROJECT.value", "api command topic", "")
c4model:Rel(api__project_project_py__update, api__project_project_py__update__api_command_topic, "CommonCommandConstant.UPDATE_PROJECT.value", "message")
"""


@router.put("/{project_id}", summary='Update a project', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 project_id: str = Path(...,
                                        description='Project id that is used in order to update the project'),
                 name: str = Body(..., description='Title of the project', embed=True),
                 city_id: str = Body(..., description='City id of this project', embed=True),
                 country_id: str = Body(..., description='Country id of this project', embed=True),
                 address_line: str = Body(..., description='Address line of the project', embed=True),
                 beneficiary_id: str = Body(..., description='The id of the beneficiary', embed=True),
                 state: str = Body(..., description='The state of the project', embed=True),
                 ):
    reqId = f'{CacheType.LIST.value}:{str(uuid4())}:2'
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_PROJECT.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': project_id,
                                         'name': name,
                                         'city_id': city_id,
                                         'country_id': country_id,
                                         'address_line': address_line,
                                         'beneficiary_id': beneficiary_id,
                                         'state': state
                                         })), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


# region Building
"""
c4model|cb|api:Component(api__project_project_py__createBuilding, "Create Building", "http(s)", "")
c4model:Rel(api__project_project_py__createBuilding, project__messaging_project_command_handler__CreateBuildingHandler, "CommonCommandConstant.CREATE_BUILDING.value", "message")
"""
@router.post("/{project_id}/buildings", summary='Create building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createBuilding(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         name: str = Body(..., description='Building name', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_BUILDING.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'name': name,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__deleteBuilding, "Delete Building", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuilding, project__messaging_project_command_handler__DeleteBuildingHandler, "CommonCommandConstant.DELETE_BUILDING.value", "message")
"""
@router.delete("/{project_id}/buildings/{building_id}", summary='Delete building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuilding(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_BUILDING.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__updateBuilding, "Update Building", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuilding, project__messaging_project_command_handler__UpdateBuildingHandler, "CommonCommandConstant.UPDATE_BUILDING.value", "message")
"""
@router.put("/{project_id}/buildings/{building_id}", summary='Update building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateBuilding(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         name: str = Body(..., description='Building name', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_BUILDING.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'name': name,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
# endregion

#region Building Level
"""
c4model|cb|api:Component(api__project_project_py__createBuildingLevel, "Create Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__createBuildingLevel, project__messaging_project_command_handler__CreateBuildingLevelHandler, "CommonCommandConstant.CREATE_BUILDING_LEVEL.value", "message")
"""
@router.post("/{project_id}/buildings/{building_id}/levels", summary='Add level to building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createBuildingLevel(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         name: str = Body(..., description='Building level name', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_BUILDING_LEVEL.value,
                                        metadata=json.dumps({"token": Client.token, "msg_key": building_id}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'name': name,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__deleteBuildingLevel, "Delete Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuildingLevel, project__messaging_project_command_handler__DeleteBuildingLevelHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL.value", "message")
"""
@router.delete("/{project_id}/buildings/{building_id}/levels/{level_id}", summary='Delete building level', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuildingLevel(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_BUILDING_LEVEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__updateBuildingLevel, "Update Building Level", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuildingLevel, project__messaging_project_command_handler__UpdateBuildingLevelHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL.value", "message")
"""
@router.put("/{project_id}/buildings/{building_id}/levels/{level_id}", summary='Update building level', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateBuildingLevel(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         name: str = Body(..., description='Building name', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_BUILDING_LEVEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             'name': name,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__linkBuildingLevelToBuilding, "Link Building Level to Building", "http(s)", "")
c4model:Rel(api__project_project_py__linkBuildingLevelToBuilding, project__messaging_project_command_handler__LinkBuildingLevelToBuildingHandler, "CommonCommandConstant.LINK_BUILDING_LEVEL_TO_BUILDING.value", "message")
"""
@router.put("/{project_id}/buildings/{building_id}/levels/{level_id}/link", summary='Link building level to building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def linkBuildingLevelToBuilding(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.LINK_BUILDING_LEVEL_TO_BUILDING.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__unlinkBuildingLevelFromBuilding, "Unlink Building Level from Building", "http(s)", "")
c4model:Rel(api__project_project_py__unlinkBuildingLevelFromBuilding, project__messaging_project_command_handler__UnlinkBuildingLevelFromBuildingHandler, "CommonCommandConstant.UNLINK_BUILDING_LEVEL_FROM_BUILDING.value", "message")
"""
@router.put("/{project_id}/buildings/{building_id}/levels/{level_id}/unlink", summary='Unlink building level from building', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def unlinkBuildingLevelFromBuilding(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UNLINK_BUILDING_LEVEL_FROM_BUILDING.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
#endregion

#region Building Level Room
"""
c4model|cb|api:Component(api__project_project_py__createBuildingLevelRoom, "Create Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__createBuildingLevelRoom, project__messaging_project_command_handler__CreateBuildingLevelRoomHandler, "CommonCommandConstant.CREATE_BUILDING_LEVEL_ROOM.value", "message")
"""
@router.post("/{project_id}/buildings/{building_id}/levels/{level_id}/rooms", summary='Add room to building level', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createBuildingLevelRoom(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         name: str = Body(..., description='Building level room name', embed=True),
                         description: str = Body(..., description='Building level room description', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_BUILDING_LEVEL_ROOM.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             'name': name,
                                             'description': description,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__deleteBuildingLevelRoom, "Delete Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__deleteBuildingLevelRoom, project__messaging_project_command_handler__DeleteBuildingLevelRoomHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL_ROOM.value", "message")
"""
@router.delete("/{project_id}/buildings/{building_id}/levels/{level_id}/rooms/{room_id}", summary='Delete building level room', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteBuildingLevelRoom(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         room_id: str = Path(..., description='Building level room id'),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_BUILDING_LEVEL_ROOM.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             'building_level_room_id': room_id,
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}

"""  
c4model|cb|api:Component(api__project_project_py__updateBuildingLevelRoom, "Update Building Level Room", "http(s)", "")
c4model:Rel(api__project_project_py__updateBuildingLevelRoom, project__messaging_project_command_handler__UpdateBuildingLevelRoomHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL_ROOM.value", "message")
"""
@router.put("/{project_id}/buildings/{building_id}/levels/{level_id}/rooms/{room_id}", summary='Update building level room', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateBuildingLevelRoom(*, _=Depends(CustomHttpBearer()),
                         project_id: str = Path(..., description='Project id'),
                         building_id: str = Path(..., description='Building id'),
                         level_id: str = Path(..., description='Building level id'),
                         room_id: str = Path(..., description='Building level room id'),
                         name: str = Body(..., description='Building level room name', embed=True),
                         description: str = Body(..., description='Building level room description', embed=True),
                         ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_BUILDING_LEVEL_ROOM.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'project_id': project_id,
                                             'building_id': building_id,
                                             'building_level_id': level_id,
                                             'building_level_room_id': room_id,
                                             'name': name,
                                             'description': description
                                             }), external=[]), schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
#endregion