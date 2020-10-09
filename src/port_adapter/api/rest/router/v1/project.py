"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from src.port_adapter.api.rest.grpc.project.ProjectClient import ProjectClient
from src.port_adapter.api.rest.model.request.Project import Project
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all projects', response_model=List[Project])
async def getAllProjects(*, result_from: int = Query(0, description='Starting offset for fetching data'),
                         result_size: int = Query(10, description='Item count to be fetched'),
                         _=Depends(CustomHttpBearer())):
    """Return all projects
    """
    try:
        client = ProjectClient()
        return client.projects(resultFrom=result_from, resultSize=result_size)
    except grpc.RpcError as e:
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getAllProjects.__module__}.{getAllProjects.__qualname__}] - error response e: {e}')
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
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getProject.__module__}.{getProject.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new project', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the project',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
