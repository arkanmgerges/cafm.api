"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Building import BuildingDescriptor, Building
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevel import BuildingLevelDescriptor, BuildingLevel
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRoom import BuildingLevelRoomDescriptor, \
    BuildingLevelRoom
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRooms import BuildingLevelRooms
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevels import BuildingLevels
from src.port_adapter.api.rest.model.response.v1.project.Buildings import Buildings
from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Projects import Projects
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.project_app_service_pb2 import ProjectAppService_projectsResponse, \
    ProjectAppService_projectsRequest, ProjectAppService_projectByIdRequest, ProjectAppService_projectByIdResponse, \
    ProjectAppService_buildingsRequest, ProjectAppService_buildingsResponse, ProjectAppService_buildingLevelsRequest, \
    ProjectAppService_buildingLevelsResponse, ProjectAppService_buildingByIdRequest, \
    ProjectAppService_buildingByIdResponse, ProjectAppService_buildingLevelByIdRequest, \
    ProjectAppService_buildingLevelByIdResponse, ProjectAppService_buildingLevelRoomByIdRequest, \
    ProjectAppService_buildingLevelRoomByIdResponse, ProjectAppService_newIdRequest, ProjectAppService_newIdResponse, \
    ProjectAppService_newBuildingIdRequest, ProjectAppService_newBuildingIdResponse, \
    ProjectAppService_newBuildingLevelIdRequest, ProjectAppService_newBuildingLevelIdResponse, \
    ProjectAppService_newBuildingLevelRoomIdRequest, ProjectAppService_newBuildingLevelRoomIdResponse, \
    ProjectAppService_buildingLevelRoomsRequest, ProjectAppService_buildingLevelRoomsResponse
from src.resource.proto._generated.project.project_app_service_pb2_grpc import ProjectAppServiceStub


class ProjectClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newIdRequest()
                response: ProjectAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(ProjectClient.newId.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    # region Project
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
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.projects.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.projects.__qualname__}] - grpc response: {response}')

                return Projects(
                    projects=[self._descriptorByObject(project) for project in response[0].projects],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def projectById(self, projectId) -> ProjectDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc call to retrieve project with projectId: {projectId} from server {self._server}:{self._port}')
                response: ProjectAppService_projectByIdResponse = stub.projectById.with_call(
                    ProjectAppService_projectByIdRequest(id=projectId),
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.projectById.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.projectById.__qualname__}] - grpc response: {response}')

                return self._descriptorByObject(response[0].project)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> ProjectDescriptor:
        return ProjectDescriptor(id=obj.id,
                                 name=obj.name,
                                 city_id=obj.cityId,
                                 country_id=obj.countryId,
                                 address_line=obj.addressLine,
                                 address_line_two=obj.addressLineTwo,
                                 beneficiary_id=obj.beneficiaryId,
                                 start_date=obj.startDate,
                                 state=obj.state
                                 )

    # endregion

    # region Building, level & room
    @OpenTelemetry.grpcTraceOTel
    def buildings(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None,
                  include: List[str] = None, projectId: str = None) -> Buildings:
        order = [] if order is None else order
        include = [] if include is None else include
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildings.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingsRequest(resultFrom=resultFrom, resultSize=resultSize,
                                                             include=include, projectId=projectId)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: ProjectAppService_buildingsResponse = stub.buildings.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildings.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildings.__qualname__}] - grpc response: {response}')

                return Buildings(
                    buildings=[self._buildingDescriptor(obj=obj) for obj in response[0].buildings],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingIdRequest()
                response: ProjectAppService_newBuildingIdResponse = stub.newBuildingId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(ProjectClient.newBuildingId.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.newBuildingId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingById(self, id: str = None, include: List[str] = None) -> Building:
        include = [] if include is None else include
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildingById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingByIdRequest(id=id, include=include)
                response: ProjectAppService_buildingByIdResponse = stub.buildingById.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildingById.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildingById.__qualname__}] - grpc response: {response}')

                return self._buildingDescriptor(obj=response[0].building)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevels(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None,
                       include: List[str] = None, buildingId: str = None) -> BuildingLevels:
        order = [] if order is None else order
        include = [] if include is None else include
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildingLevels.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingLevelsRequest(resultFrom=resultFrom, resultSize=resultSize,
                                                                  include=include, buildingId=buildingId)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: ProjectAppService_buildingLevelsResponse = stub.buildingLevels.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildingLevels.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildingLevels.__qualname__}] - grpc response: {response}')

                return BuildingLevels(
                    building_levels=[self._buildingLevelDescriptor(obj=obj) for obj in response[0].buildingLevels],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingLevelIdRequest()
                response: ProjectAppService_newBuildingLevelIdResponse = stub.newBuildingLevelId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            ProjectClient.newBuildingLevelId.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.newBuildingLevelId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelById(self, id: str = None, include: List[str] = None) -> BuildingLevel:
        include = [] if include is None else include
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildingLevelById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingLevelByIdRequest(id=id, include=include)
                response: ProjectAppService_buildingLevelByIdResponse = stub.buildingLevelById.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildingLevelById.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildingLevelById.__qualname__}] - grpc response: {response}')

                return self._buildingLevelDescriptor(obj=response[0].buildingLevel)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRooms(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None,
                           buildingLevelId: str = None) -> BuildingLevelRooms:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildingLevelRooms.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingLevelRoomsRequest(resultFrom=resultFrom, resultSize=resultSize,
                                                                      buildingLevelId=buildingLevelId)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: ProjectAppService_buildingLevelRoomsResponse = stub.buildingLevelRooms.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildingLevelRooms.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildingLevelRooms.__qualname__}] - grpc response: {response}')

                return BuildingLevelRooms(
                    building_level_rooms=[self._buildingLevelRoomDescriptor(obj=obj) for obj in
                                          response[0].buildingLevelRooms],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelRoomId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingLevelRoomIdRequest()
                response: ProjectAppService_newBuildingLevelRoomIdResponse = stub.newBuildingLevelRoomId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            ProjectClient.newBuildingLevelRoomId.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.newBuildingLevelRoomId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRoomById(self, id: str = None) -> BuildingLevelRoom:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{ProjectClient.buildingLevelRoomById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}')
                request = ProjectAppService_buildingLevelRoomByIdRequest(id=id)
                response: ProjectAppService_buildingLevelRoomByIdResponse = stub.buildingLevelRoomById.with_call(
                    request,
                    metadata=(('token', self.token), ('opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                        ProjectClient.buildingLevelRoomById.__qualname__))))
                logger.debug(
                    f'[{ProjectClient.buildingLevelRoomById.__qualname__}] - grpc response: {response}')

                return self._buildingLevelRoomDescriptor(obj=response[0].buildingLevelRoom)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _buildingDescriptor(self, obj: Any) -> BuildingDescriptor:
        logger.debug(f'_buildingDescriptor --> {obj}')
        return BuildingDescriptor(id=obj.id,
                                  name=obj.name,
                                  project_id=obj.projectId,
                                  building_levels=[self._buildingLevelDescriptor(x) for x in obj.buildingLevels])

    def _buildingLevelDescriptor(self, obj: Any) -> BuildingLevelDescriptor:
        logger.debug(f'_buildingLevelDescriptor --> {obj}')
        return BuildingLevelDescriptor(id=obj.id,
                                       name=obj.name,
                                       is_sublevel=obj.isSubLevel,
                                       building_ids=[x for x in obj.buildingIds],
                                       building_level_rooms=[self._buildingLevelRoomDescriptor(x) for x in
                                                             obj.buildingLevelRooms])

    def _buildingLevelRoomDescriptor(self, obj: Any) -> BuildingLevelRoomDescriptor:
        logger.debug(f'_buildingLevelRoomDescriptor --> {obj}')
        return BuildingLevelRoomDescriptor(id=obj.id,
                                           name=obj.name,
                                           description=obj.description,
                                           index=obj.index,
                                           building_level_id=obj.buildingLevelId)

    # endregion
