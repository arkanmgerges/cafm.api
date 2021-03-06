"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.OrganizationLocation import OrganizationLocationDescriptor
from typing import List, Any

import grpc

from src.port_adapter.api.rest.model.response.v1.project.lookup.common.OrganizationIncludesUsersIncludeRoles import \
    OrganizationIncludesUsersIncludeRolesDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.ProjectIncludesOrganizationsIncludeUsersIncludeRoles import \
    ProjectIncludesOrganizationsIncludeUsersIncludeRoles
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.ProjectsIncludeOrganizationsIncludeUsersIncludeRoles import \
    ProjectsIncludeOrganizationsIncludeUsersIncludeRoles
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.UserIncludesRoles import \
    UserIncludesRolesDescriptor
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
    ) -> ProjectsIncludeOrganizationsIncludeUsersIncludeRoles:
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

                return ProjectsIncludeOrganizationsIncludeUsersIncludeRoles(
                    projects_include_organizations_include_users_include_roles=[
                        self._descriptorByObject(protoObj=projectLookup)
                        for projectLookup in response[0].projects_include_organizations_include_users_include_roles
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, protoObj: Any) -> ProjectIncludesOrganizationsIncludeUsersIncludeRoles:
        responseModel = ProjectIncludesOrganizationsIncludeUsersIncludeRoles()
        [setattr(responseModel, attribute, getattr(protoObj, attribute)) for attribute in
         self._responseModelAttributues(ProjectDescriptor)]
        responseModel.organizations_include_users_include_roles = []
        for organizationIncludesUsersIncludeRolesProtoObj in protoObj.organizations_include_users_include_roles:
            organizationIncludesUsersIncludeRolesResponseModel = OrganizationIncludesUsersIncludeRolesDescriptor()
            [setattr(organizationIncludesUsersIncludeRolesResponseModel, attribute, getattr(organizationIncludesUsersIncludeRolesProtoObj, attribute)) for attribute in
             self._responseModelAttributues(OrganizationDescriptor)]

            organizationIncludesUsersIncludeRolesResponseModel.locations = []
            for locationProtoObj in organizationIncludesUsersIncludeRolesProtoObj.locations:
                organizationLocationModel = OrganizationLocationDescriptor()
                [setattr(organizationLocationModel, attribute, getattr(locationProtoObj, attribute)) for
                 attribute in
                 self._responseModelAttributues(OrganizationLocationDescriptor)]
                organizationIncludesUsersIncludeRolesResponseModel.locations.append(organizationLocationModel)

            organizationIncludesUsersIncludeRolesResponseModel.users_include_roles = []
            for userIncludesRolesProtoObj in organizationIncludesUsersIncludeRolesProtoObj.users_include_roles:
                userIncludesRolesResponseModel = UserIncludesRolesDescriptor()
                [setattr(userIncludesRolesResponseModel, attribute, getattr(userIncludesRolesProtoObj, attribute)) for
                 attribute in
                 self._responseModelAttributues(UserDescriptor)]

                userIncludesRolesResponseModel.roles = []
                for roleProtoObj in userIncludesRolesProtoObj.roles:
                    roleResponseModel = RoleDescriptor()
                    [setattr(roleResponseModel, attribute, getattr(roleProtoObj, attribute)) for attribute
                     in
                     self._responseModelAttributues(RoleDescriptor)]
                    userIncludesRolesResponseModel.roles.append(roleResponseModel)
                organizationIncludesUsersIncludeRolesResponseModel.users_include_roles.append(userIncludesRolesResponseModel)
            responseModel.organizations_include_users_include_roles.append(organizationIncludesUsersIncludeRolesResponseModel)

        return responseModel

    def _responseModelAttributues(self, model):
        return list(model.__fields__.keys())

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


