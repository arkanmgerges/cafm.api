"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc
from src.port_adapter.api.rest.model.response.v1.project.lookup.organization.OrganizationLookup import (
    OrganizationLookupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.organization.OrganizationLookups import OrganizationLookups

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
from src.resource.proto._generated.project.lookup.organization.organization_lookup_app_service_pb2 import \
    OrganizationLookupAppService_organizationLookupsRequest, OrganizationLookupAppService_organizationLookupsResponse
from src.resource.proto._generated.project.lookup.organization.organization_lookup_app_service_pb2_grpc import \
    OrganizationLookupAppServiceStub


class OrganizationLookupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def organizationLookups(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None, filters: List[dict] = None
    ) -> OrganizationLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters

        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = OrganizationLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{OrganizationLookupClient.organizationLookups.__qualname__}] - grpc call to retrieve user lookups from server {self._server}:{self._port}"
                )
                request = OrganizationLookupAppService_organizationLookupsRequest(
                    result_from=resultFrom, result_size=resultSize, orders=orders, filters=filters
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]

                response: OrganizationLookupAppService_organizationLookupsResponse = (
                    stub.lookup.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    OrganizationLookupClient.organizationLookups.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{OrganizationLookupClient.organizationLookups.__qualname__}] - grpc response: {response}"
                )

                return OrganizationLookups(
                    organization_lookups=[
                        self._descriptorByObject(obj=organizationLookup)
                        for organizationLookup in response[0].organization_lookups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> OrganizationLookupDescriptor:
        return OrganizationLookupDescriptor(
            organization=OrganizationDescriptor(
                **(self._constructResponseModelKwargs(protoObject=obj.organization))
            ),
            roles=[RoleDescriptor(id=x.id, name=x.name, title=x.title) for x in obj.roles],
            users=[
                UserDescriptor(
                    **(self._constructResponseModelKwargs(protoObject=x))
                )
                for x in obj.users
            ],
            projects=[
                ProjectDescriptor(
                    **(self._constructResponseModelKwargs(protoObject=x))
                )
                for x in obj.projects
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


