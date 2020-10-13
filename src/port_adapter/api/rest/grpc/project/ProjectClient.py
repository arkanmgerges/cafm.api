"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.Project import Project
from src.resource.logging.logger import logger
from src.resource.proto._generated.project_app_service_pb2 import ProjectAppService_projectsResponse, \
    ProjectAppService_projectsRequest, ProjectAppService_projectByIdRequest, ProjectAppService_projectByIdResponse
from src.resource.proto._generated.project_app_service_pb2_grpc import ProjectAppServiceStub


class ProjectClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    def projects(self, resultFrom: int = 0, resultSize: int = 10) -> List[Project]:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.projects.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}')
                response: ProjectAppService_projectsResponse = stub.projects.with_call(
                    ProjectAppService_projectsRequest(resultFrom=resultFrom, resultSize=resultSize),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{ProjectClient.projects.__qualname__}] - grpc response: {response}')

                return [Project(id=project.id, name=project.name) for project in response[0].projects]
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def projectById(self, projectId) -> Project:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc call to retrieve project with projectId: {projectId} from server {self._server}:{self._port}')
                response: ProjectAppService_projectByIdResponse = stub.projectById.with_call(
                    ProjectAppService_projectByIdRequest(id=projectId),
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc response: {response}')

                return Project(id=response[0].project.id, name=response[0].project.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e