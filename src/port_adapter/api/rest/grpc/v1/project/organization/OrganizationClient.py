"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.Organizations import (
    Organizations,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.organization_app_service_pb2 import (
    OrganizationAppService_organizationsResponse,
    OrganizationAppService_organizationsRequest,
    OrganizationAppService_organizationByIdRequest,
    OrganizationAppService_organizationByIdResponse,
    OrganizationAppService_newIdRequest,
    OrganizationAppService_newIdResponse, OrganizationAppService_organizationsByTypeRequest,
    OrganizationAppService_organizationsByTypeResponse,
)
from src.resource.proto._generated.project.organization_app_service_pb2_grpc import (
    OrganizationAppServiceStub,
)


class OrganizationClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                request = OrganizationAppService_newIdRequest()
                response: OrganizationAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                OrganizationClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{OrganizationClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def organizations(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Organizations:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{OrganizationClient.organizations.__qualname__}] - grpc call to retrieve organizations from server {self._server}:{self._port}"
                )
                request = OrganizationAppService_organizationsRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(
                        orderBy=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: OrganizationAppService_organizationsResponse = (
                    stub.organizations.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    OrganizationClient.organizations.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{OrganizationClient.organizations.__qualname__}] - grpc response: {response}"
                )

                return Organizations(
                    organizations=[
                        self._descriptorByObject(obj=organization)
                        for organization in response[0].organizations
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def organizationsByType(
            self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None, organizationType: str = None,
    ) -> Organizations:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{OrganizationClient.organizationsByType.__qualname__}] - grpc call to retrieve organizations from server {self._server}:{self._port}"
                )
                request = OrganizationAppService_organizationsByTypeRequest(
                    result_from=resultFrom, result_size=resultSize, type=organizationType
                )
                [
                    request.orders.add(
                        orderBy=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: OrganizationAppService_organizationsByTypeResponse = (
                    stub.organizations_by_type.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    OrganizationClient.organizationsByType.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{OrganizationClient.organizationsByType.__qualname__}] - grpc response: {response}"
                )

                return Organizations(
                    organizations=[
                        self._descriptorByObject(obj=organization)
                        for organization in response[0].organizations
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def organizationById(self, id) -> OrganizationDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{OrganizationClient.organizationById.__qualname__}] - grpc call to retrieve organization with organizationId: {id} from server {self._server}:{self._port}"
                )
                response: OrganizationAppService_organizationByIdResponse = (
                    stub.organization_by_id.with_call(
                        OrganizationAppService_organizationByIdRequest(id=id),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    OrganizationClient.organizations.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{OrganizationClient.organizationById.__qualname__}] - grpc response: {response}"
                )
                organization = response[0].organization
                return self._descriptorByObject(obj=organization)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> OrganizationDescriptor:
        return OrganizationDescriptor(
            id=obj.id,
            name=obj.name,
            website_url=obj.website_url,
            organization_type=obj.organization_type,
            address_one=obj.address_one,
            address_two=obj.address_two,
            postal_code=obj.postal_code,
            country_id=obj.country_id,
            city_id=obj.city_id,
            country_state_name=obj.country_state_name,
            country_state_iso_code=obj.country_state_iso_code,
            manager_first_name=obj.manager_first_name,
            manager_last_name=obj.manager_last_name,
            manager_email=obj.manager_email,
            manager_phone_number=obj.manager_phone_number,
            manager_avatar=obj.manager_avatar,
        )
