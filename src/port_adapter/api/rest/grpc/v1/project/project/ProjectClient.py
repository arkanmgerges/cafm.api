"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Building import (
    BuildingDescriptor,
    Building,
)
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevel import (
    BuildingLevelDescriptor,
    BuildingLevel,
)
from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRoom import (
    BuildingLevelRoomDescriptor,
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
from src.port_adapter.api.rest.model.response.v1.project.statistic.project.ProjectStatistic import \
    ProjectStatisticDescriptor
from src.port_adapter.api.rest.model.response.v1.project.statistic.project.ProjectsStatistics import ProjectsStatistics
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.project_app_service_pb2 import (
    ProjectAppService_projectsByStateRequest,
    ProjectAppService_projectsByStateResponse,
    ProjectAppService_projectsResponse,
    ProjectAppService_projectsRequest,
    ProjectAppService_projectsByOrganizationIdResponse,
    ProjectAppService_projectsByOrganizationIdRequest,
    ProjectAppService_projectByIdRequest,
    ProjectAppService_projectByIdResponse,
    ProjectAppService_buildingsRequest,
    ProjectAppService_buildingsResponse,
    ProjectAppService_buildingLevelsRequest,
    ProjectAppService_buildingLevelsResponse,
    ProjectAppService_buildingByIdRequest,
    ProjectAppService_buildingByIdResponse,
    ProjectAppService_buildingLevelByIdRequest,
    ProjectAppService_buildingLevelByIdResponse,
    ProjectAppService_buildingLevelRoomByIdRequest,
    ProjectAppService_buildingLevelRoomByIdResponse,
    ProjectAppService_newIdRequest,
    ProjectAppService_newIdResponse,
    ProjectAppService_newBuildingIdRequest,
    ProjectAppService_newBuildingIdResponse,
    ProjectAppService_newBuildingLevelIdRequest,
    ProjectAppService_newBuildingLevelIdResponse,
    ProjectAppService_newBuildingLevelRoomIdRequest,
    ProjectAppService_newBuildingLevelRoomIdResponse,
    ProjectAppService_buildingLevelRoomsRequest,
    ProjectAppService_buildingLevelRoomsResponse, ProjectAppService_statisticsResponse,
    ProjectAppService_statisticsRequest,
)
from src.resource.proto._generated.project.project_app_service_pb2_grpc import (
    ProjectAppServiceStub,
)


class ProjectClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newIdRequest()
                response: ProjectAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                ProjectClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{ProjectClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    # region Project
    @OpenTelemetry.grpcTraceOTel
    def projects(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Projects:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.projects.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}"
                )
                request = ProjectAppService_projectsRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_projectsResponse = stub.projects.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                ProjectClient.projects.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{ProjectClient.projects.__qualname__}] - grpc response: {response}"
                )

                return Projects(
                    projects=[
                        self._descriptorByObject(project)
                        for project in response[0].projects
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def projectsStatistics(
            self,
    ) -> ProjectsStatistics:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.projectsStatistics.__qualname__}] - grpc call to server {self._server}:{self._port}"
                )
                request = ProjectAppService_statisticsRequest()
                response: ProjectAppService_statisticsResponse = stub.statistics.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                ProjectClient.projectsStatistics.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{ProjectClient.projectsStatistics.__qualname__}] - grpc response: {response}"
                )

                return ProjectsStatistics(
                    statistics=[
                        self._statisticDescriptorByObject(statistic)
                        for statistic in response[0].statistics
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    # region Project
    @OpenTelemetry.grpcTraceOTel
    def projectsByOrganizationId(
        self,
        organizationId,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> Projects:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.projectsByOrganizationId.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}"
                )
                request = ProjectAppService_projectsByOrganizationIdRequest(
                    organization_id=organizationId,
                    result_from=resultFrom,
                    result_size=resultSize,
                )
                [
                    request.orders.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_projectsByOrganizationIdResponse = (
                    stub.projects_by_organization_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.projectsByOrganizationId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.projectsByOrganizationId.__qualname__}] - grpc response: {response}"
                )

                return Projects(
                    projects=[
                        self._descriptorByObject(project)
                        for project in response[0].projects
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def projectsByState(
        self, state: str = None, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Projects:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.projectsByState.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}"
                )
                request = ProjectAppService_projectsByStateRequest(
                    state=state, result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_projectsByStateResponse = stub.projects_by_state.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                ProjectClient.projectsByState.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{ProjectClient.projectsByState.__qualname__}] - grpc response: {response}"
                )

                return Projects(
                    projects=[
                        self._descriptorByObject(project)
                        for project in response[0].projects
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def projectById(self, projectId) -> ProjectDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.projectById.__qualname__}] - grpc call to retrieve project with projectId: {projectId} from server {self._server}:{self._port}"
                )
                response: ProjectAppService_projectByIdResponse = (
                    stub.project_by_id.with_call(
                        ProjectAppService_projectByIdRequest(id=projectId),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.projectById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.projectById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(response[0].project)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> ProjectDescriptor:
        kwargs = {k: getattr(obj, k, None) for k in ProjectDescriptor.__fields__.keys()}
        return ProjectDescriptor(**kwargs)

    def _statisticDescriptorByObject(self, obj: Any) -> ProjectStatisticDescriptor:
        kwargs = {k: getattr(obj, k, None) for k in ProjectStatisticDescriptor.__fields__.keys()}
        return ProjectStatisticDescriptor(**kwargs)

    # endregion

    # region Building, level & room
    @OpenTelemetry.grpcTraceOTel
    def buildings(
        self,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
        include: List[str] = None,
        projectId: str = None,
    ) -> Buildings:
        orders = [] if orders is None else orders
        include = [] if include is None else include
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildings.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingsRequest(
                    result_from=resultFrom,
                    result_size=resultSize,
                    include=include,
                    project_id=projectId,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_buildingsResponse = (
                    stub.buildings.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildings.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildings.__qualname__}] - grpc response: {response}"
                )

                return Buildings(
                    buildings=[
                        self._buildingDescriptor(obj=obj)
                        for obj in response[0].buildings
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingIdRequest()
                response: ProjectAppService_newBuildingIdResponse = (
                    stub.new_building_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.newBuildingId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.newBuildingId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingById(self, id: str = None, include: List[str] = None) -> Building:
        include = [] if include is None else include
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildingById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingByIdRequest(id=id, include=include)
                response: ProjectAppService_buildingByIdResponse = (
                    stub.building_by_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildingById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildingById.__qualname__}] - grpc response: {response}"
                )

                return self._buildingDescriptor(obj=response[0].building)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevels(
        self,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
        include: List[str] = None,
        buildingId: str = None,
    ) -> BuildingLevels:
        orders = [] if orders is None else orders
        include = [] if include is None else include
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildingLevels.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingLevelsRequest(
                    result_from=resultFrom,
                    result_size=resultSize,
                    include=include,
                    building_id=buildingId,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_buildingLevelsResponse = (
                    stub.building_levels.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildingLevels.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildingLevels.__qualname__}] - grpc response: {response}"
                )

                return BuildingLevels(
                    building_levels=[
                        self._buildingLevelDescriptor(obj=obj)
                        for obj in response[0].building_levels
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingLevelIdRequest()
                response: ProjectAppService_newBuildingLevelIdResponse = (
                    stub.new_building_level_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.newBuildingLevelId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.newBuildingLevelId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelById(
        self, id: str = None, include: List[str] = None
    ) -> BuildingLevel:
        include = [] if include is None else include
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildingLevelById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingLevelByIdRequest(
                    id=id, include=include
                )
                response: ProjectAppService_buildingLevelByIdResponse = (
                    stub.building_level_by_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildingLevelById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildingLevelById.__qualname__}] - grpc response: {response}"
                )

                return self._buildingLevelDescriptor(obj=response[0].building_level)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRooms(
        self,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
        buildingLevelId: str = None,
    ) -> BuildingLevelRooms:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildingLevelRooms.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingLevelRoomsRequest(
                    result_from=resultFrom,
                    result_size=resultSize,
                    building_level_id=buildingLevelId,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: ProjectAppService_buildingLevelRoomsResponse = (
                    stub.building_level_rooms.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildingLevelRooms.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildingLevelRooms.__qualname__}] - grpc response: {response}"
                )

                return BuildingLevelRooms(
                    building_level_rooms=[
                        self._buildingLevelRoomDescriptor(obj=obj)
                        for obj in response[0].building_level_rooms
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelRoomId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_newBuildingLevelRoomIdRequest()
                response: ProjectAppService_newBuildingLevelRoomIdResponse = (
                    stub.new_building_level_room_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.newBuildingLevelRoomId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.newBuildingLevelRoomId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRoomById(self, id: str = None) -> BuildingLevelRoom:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.buildingLevelRoomById.__qualname__}] - grpc call to retrieve data from server {self._server}:{self._port}"
                )
                request = ProjectAppService_buildingLevelRoomByIdRequest(id=id)
                response: ProjectAppService_buildingLevelRoomByIdResponse = (
                    stub.building_level_room_by_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectClient.buildingLevelRoomById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectClient.buildingLevelRoomById.__qualname__}] - grpc response: {response}"
                )

                return self._buildingLevelRoomDescriptor(
                    obj=response[0].building_level_room
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _buildingDescriptor(self, obj: Any) -> BuildingDescriptor:
        logger.debug(f"_buildingDescriptor --> {obj}")
        return BuildingDescriptor(
            id=obj.id,
            name=obj.name,
            project_id=obj.project_id,
            building_levels=[
                self._buildingLevelDescriptor(x) for x in obj.building_levels
            ],
        )

    def _buildingLevelDescriptor(self, obj: Any) -> BuildingLevelDescriptor:
        logger.debug(f"_buildingLevelDescriptor --> {obj}")
        return BuildingLevelDescriptor(
            id=obj.id,
            name=obj.name,
            is_sub_level=obj.is_sub_level,
            building_ids=[x for x in obj.building_ids],
            building_level_rooms=[
                self._buildingLevelRoomDescriptor(x) for x in obj.building_level_rooms
            ],
        )

    def _buildingLevelRoomDescriptor(self, obj: Any) -> BuildingLevelRoomDescriptor:
        logger.debug(f"_buildingLevelRoomDescriptor --> {obj}")
        return BuildingLevelRoomDescriptor(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            index=obj.index,
            building_level_id=obj.building_level_id,
        )

    # endregion
