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
from src.port_adapter.api.rest.model.response.v1.project.Role import Role
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
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> UserLookups:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{UserLookupClient.userLookups.__qualname__}] - grpc call to retrieve user lookups from server {self._server}:{self._port}"
                )
                request = UserLookupAppService_userLookupsRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: UserLookupAppService_userLookupsResponse = (
                    stub.userLookups.with_call(
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
                        for userLookup in response[0].userLookups
                    ],
                    item_count=response[0].itemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> UserLookupDescriptor:
        return UserLookupDescriptor(
            user=User(
                id=obj.user.id,
                email=obj.user.email,
                first_name=obj.user.firstName,
                last_name=obj.user.lastName,
                address_one=obj.user.addressOne,
                address_two=obj.user.addressTwo,
                postal_code=obj.user.postalCode,
                phone_number=obj.user.phoneNumber,
                avatar_image=obj.user.avatarImage,
                country_id=obj.user.countryId,
                city_id=obj.user.cityId,
                country_state_name=obj.user.countryStateName,
                start_date=obj.user.startDate,
            ),
            roles=[Role(id=x.id, name=x.name) for x in obj.roles],
            organizations=[
                Organization(
                    id=x.id,
                    name=x.name,
                    website_url=x.websiteUrl,
                    organization_type=x.organizationType,
                    address_one=x.addressOne,
                    address_two=x.addressTwo,
                    postal_code=x.postalCode,
                    country_id=x.countryId,
                    city_id=x.cityId,
                    state_name=x.countryStateName,
                    manager_first_name=x.managerFirstName,
                    manager_last_name=x.managerLastName,
                    manager_email=x.managerEmail,
                    manager_phone_number=x.managerPhoneNumber,
                    manager_avatar=x.managerAvatar,
                )
                for x in obj.organizations
            ],
        )
