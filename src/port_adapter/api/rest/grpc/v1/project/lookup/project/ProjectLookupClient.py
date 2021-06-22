"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc
from src.port_adapter.api.rest.model.response.v1.project.lookup.project.ProjectLookup import (
    ProjectLookupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.project.ProjectLookups import ProjectLookups

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.lookup.project.project_lookup_app_service_pb2 import \
    ProjectLookupAppService_projectLookupsRequest, ProjectLookupAppService_projectLookupsResponse
from src.resource.proto._generated.project.lookup.project.project_lookup_app_service_pb2_grpc import \
    ProjectLookupAppServiceStub


class ProjectLookupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def projectLookups(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None, filters: List[dict] = None
    ) -> ProjectLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters

        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{ProjectLookupClient.projectLookups.__qualname__}] - grpc call to retrieve user lookups from server {self._server}:{self._port}"
                )
                request = ProjectLookupAppService_projectLookupsRequest(
                    result_from=resultFrom, result_size=resultSize, orders=orders, filters=filters
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]

                response: ProjectLookupAppService_projectLookupsResponse = (
                    stub.lookup.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    ProjectLookupClient.projectLookups.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{ProjectLookupClient.projectLookups.__qualname__}] - grpc response: {response}"
                )

                return ProjectLookups(
                    project_lookups=[
                        self._descriptorByObject(obj=projectLookup)
                        for projectLookup in response[0].project_lookups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> ProjectLookupDescriptor:
        return ProjectLookupDescriptor(
            project=ProjectDescriptor(
                **(self._constructResponseModelKwargs(protoObject=obj.project))
            ),
            roles=[RoleDescriptor(id=x.id, name=x.name, title=x.title) for x in obj.roles],
            users=[
                UserDescriptor(
                    **(self._constructResponseModelKwargs(protoObject=x))
                )
                for x in obj.users
            ],
            organizations=[
                OrganizationDescriptor(
                    **(self._constructResponseModelKwargs(protoObject=x))
                )
                for x in obj.organizations
            ]
        )

    def _constructResponseModelKwargs(self, protoObject, intAttributes: List[str]=None):
        kwargs = {}
        intAttributes = intAttributes if intAttributes is not None else []
        for fieldDescriptor in protoObject.DESCRIPTOR.fields:
            attribute = fieldDescriptor.name
            value = getattr(protoObject, attribute, None)
            if attribute in intAttributes and value is None:
                value = 0
            kwargs[attribute] = value
        return kwargs


