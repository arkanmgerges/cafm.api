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
from src.port_adapter.api.rest.grpc.project.ProjectClient import ProjectClient
from src.port_adapter.api.rest.model.response.Project import Project
from src.port_adapter.api.rest.model.response.Projects import Projects
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all projects', response_model=Projects)
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


@router.get(path="/{project_id}/", summary='Get project',
            response_model=Project)
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


@router.post("/create", summary='Create a new project', status_code=status.HTTP_200_OK)
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='Title of the project', embed=True)):
    reqId = f'{CacheType.LIST.value}:{str(uuid4())}:2'
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.CREATE_PROJECT.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{project_id}", summary='Delete a project', status_code=status.HTTP_200_OK)
async def delete(*, _=Depends(CustomHttpBearer()),
                 project_id: str = Path(...,
                                        description='Project id that is used in order to delete the project')):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.DELETE_PROJECT.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': project_id})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{project_id}", summary='Update a project', status_code=status.HTTP_200_OK)
async def update(*, _=Depends(CustomHttpBearer()),
                 project_id: str = Path(...,
                                        description='Project id that is used in order to delete the project'),
                 name: str = Body(..., description='Title of the project', embed=True)):
    reqId = f'{CacheType.LIST.value}:{str(uuid4())}:2'
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.UPDATE_PROJECT.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'id': project_id, 'name': name})), schema=ApiCommand.get_schema())
    return {"request_id": reqId}
