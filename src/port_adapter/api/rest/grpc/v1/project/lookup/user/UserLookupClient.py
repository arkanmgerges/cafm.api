"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.user.UserLookup import (
    UserLookupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.user.UserLookups import UserLookups
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.lookup.user.user_lookup_app_service_pb2 import \
    UserLookupAppService_userLookupsRequest, UserLookupAppService_userLookupsResponse
from src.resource.proto._generated.project.lookup.user.user_lookup_app_service_pb2_grpc import UserLookupAppServiceStub


class UserLookupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def userLookups(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None, filters: List[dict] = None
    ) -> UserLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters

        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserLookupClient.userLookups.__qualname__}] - grpc call to retrieve user lookups from server {self._server}:{self._port}"
                )
                request = UserLookupAppService_userLookupsRequest(
                    result_from=resultFrom, result_size=resultSize, orders=orders, filters=filters
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]

                response: UserLookupAppService_userLookupsResponse = (
                    stub.user_lookups.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    UserLookupClient.userLookups.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{UserLookupClient.userLookups.__qualname__}] - grpc response: {response}"
                )

                return UserLookups(
                    user_lookups=[
                        self._descriptorByObject(obj=userLookup)
                        for userLookup in response[0].user_lookups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> UserLookupDescriptor:
        return UserLookupDescriptor(
            user=UserDescriptor(
                **(self._constructProjectKwargs(protoObject=obj.user))
            ),
            roles=[RoleDescriptor(id=x.id, name=x.name, title=x.title) for x in obj.roles],
            organizations=[
                OrganizationDescriptor(
                    **(self._constructProjectKwargs(protoObject=x))
                )
                for x in obj.organizations
            ],
            projects=[
                ProjectDescriptor(
                    **(self._constructProjectKwargs(protoObject=x, intAttributes=['city_id', 'country_id', 'start_date', 'developer_city_id', 'developer_country_id']))
                )
                for x in obj.projects
            ],
        )

    def _constructProjectKwargs(self, protoObject, intAttributes: List[str]=None):
        kwargs = {}
        intAttributes = intAttributes if intAttributes is not None else []
        for fieldDescriptor in protoObject.DESCRIPTOR.fields:
            attribute = fieldDescriptor.name
            value = getattr(protoObject, attribute, None)
            if attribute in intAttributes and value is None:
                value = 0
            kwargs[attribute] = value
        return kwargs


