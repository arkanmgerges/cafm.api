"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Project import (
    ProjectDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.Projects import Projects
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.project_app_service_pb2 import (
    ProjectAppService_projectsResponse,
    ProjectAppService_projectsRequest,
    ProjectAppService_projectByIdRequest,
    ProjectAppService_projectByIdResponse,
    ProjectAppService_newIdRequest,
    ProjectAppService_newIdResponse,
)
from src.resource.proto._generated.identity.project_app_service_pb2_grpc import (
    ProjectAppServiceStub,
)


class ProjectClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectClient.newId.__qualname__}] - grpc call to retrieve projects from server {self._server}:{self._port}"
                )
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
                        self._descriptorByObject(obj=project)
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

                return self._descriptorByObject(obj=response[0].project)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> ProjectDescriptor:
        return ProjectDescriptor(id=obj.id, name=obj.name)
