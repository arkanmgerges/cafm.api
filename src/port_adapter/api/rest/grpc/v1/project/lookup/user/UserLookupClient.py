"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    Organization,
)
from src.port_adapter.api.rest.model.response.v1.project.role.Role import Role
from src.port_adapter.api.rest.model.response.v1.project.User import User
from src.port_adapter.api.rest.model.response.v1.project.UserLookup import (
    UserLookupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.UserLookups import UserLookups
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.user_lookup_app_service_pb2 import (
    UserLookupAppService_userLookupsRequest,
    UserLookupAppService_userLookupsResponse,
)
from src.resource.proto._generated.project.user_lookup_app_service_pb2_grpc import (
    UserLookupAppServiceStub,
)


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
            user=User(
                id=obj.user.id,
                email=obj.user.email,
                first_name=obj.user.first_name,
                last_name=obj.user.last_name,
                address_one=obj.user.address_one,
                address_two=obj.user.address_two,
                postal_code=obj.user.postal_code,
                phone_number=obj.user.phone_number,
                avatar_image=obj.user.avatar_image,
                country_id=obj.user.country_id,
                city_id=obj.user.city_id,
                country_state_name=obj.user.country_state_name,
                country_state_iso_code=obj.user.country_state_iso_code,
                start_date=obj.user.start_date,
            ),
            roles=[Role(id=x.id, name=x.name, title=x.title) for x in obj.roles],
            organizations=[
                Organization(
                    id=x.id,
                    name=x.name,
                    website_url=x.website_url,
                    organization_type=x.organization_type,
                    address_one=x.address_one,
                    address_two=x.address_two,
                    postal_code=x.postal_code,
                    country_id=x.country_id,
                    city_id=x.city_id,
                    country_state_name=x.country_state_name,
                    country_state_iso_code=x.country_state_iso_code,
                    manager_first_name=x.manager_first_name,
                    manager_last_name=x.manager_last_name,
                    manager_email=x.manager_email,
                    manager_phone_number=x.manager_phone_number,
                    manager_avatar=x.manager_avatar,
                )
                for x in obj.organizations
            ],
        )
