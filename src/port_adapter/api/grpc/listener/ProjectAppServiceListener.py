"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.TokenService import TokenService
from src.domain_model.project.Project import Project
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.resource.logging.logger import logger
from src.resource.proto._generated.project_app_service_pb2 import ProjectAppService_projectByNameResponse, \
    ProjectAppService_projectsResponse, ProjectAppService_projectByIdResponse
from src.resource.proto._generated.project_app_service_pb2_grpc import ProjectAppServiceServicer


class ProjectAppServiceListener(ProjectAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    def projectByName(self, request, context):
        try:
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
            project: Project = projectAppService.projectByName(name=request.name)
            response = ProjectAppService_projectByNameResponse()
            response.project.id = project.id()
            response.project.name = project.name()
            return response
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Project does not exist')
            return ProjectAppService_projectByNameResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.ProjectResponse()

    def projects(self, request, context):
        try:
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize > 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            ownedProjects = claims['project'] if 'project' in claims else []
            logger.debug(f'[{ProjectAppServiceListener.projects.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t ownedProjects {ownedProjects}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}')
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)

            projects: List[Project] = projectAppService.projects(ownedProjects=ownedProjects, resultFrom=request.resultFrom,
                                                     resultSize=resultSize)
            response = ProjectAppService_projectsResponse()
            for project in projects:
                response.projects.add(id=project.id(), name=project.name())
            logger.debug(f'[{ProjectAppServiceListener.projects.__qualname__}] - response: {response}')
            return ProjectAppService_projectsResponse(projects=response.projects)
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_projectByNameResponse()

    def projectById(self, request, context):
        try:
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
            project: Project = projectAppService.projectById(id=request.id)
            logger.debug(f'[{ProjectAppServiceListener.projectById.__qualname__}] - response: {project}')
            response = ProjectAppService_projectByIdResponse()
            response.project.id = project.id()
            response.project.name = project.name()
            return response
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Project does not exist')
            return ProjectAppService_projectByIdResponse()