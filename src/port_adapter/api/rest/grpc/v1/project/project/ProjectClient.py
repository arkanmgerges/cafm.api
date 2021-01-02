"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Project import Project
from src.port_adapter.api.rest.model.response.v1.project.Projects import Projects
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.project_app_service_pb2 import ProjectAppService_projectsResponse, \
    ProjectAppService_projectsRequest, ProjectAppService_projectByIdRequest, ProjectAppService_projectByIdResponse
from src.resource.proto._generated.project.project_app_service_pb2_grpc import ProjectAppServiceStub


class ProjectClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def projects(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Projects:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.projects.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}')
                request = ProjectAppService_projectsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: ProjectAppService_projectsResponse = stub.projects.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(ProjectClient.projects.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.projects.__qualname__}] - grpc response: {response}')

                return Projects(
                    projects=[Project(id=project.id, name=project.name) for project in response[0].projects],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def projectById(self, projectId) -> Project:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc call to retrieve project with projectId: {projectId} from server {self._server}:{self._port}')
                response: ProjectAppService_projectByIdResponse = stub.projectById.with_call(
                    ProjectAppService_projectByIdRequest(id=projectId),
                    metadata=(('token', self.token),('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(ProjectClient.projectById.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc response: {response}')

                return Project(id=response[0].project.id, name=response[0].project.name)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
