"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.City import CityDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.Country import CountryDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.State import StateDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.SubcontractorCategory import (
    SubcontractorCategoryDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.SubcontractorLookup import SubcontractorLookupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.SubcontractorLookups import SubcontractorLookups
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.lookup.subcontractor.subcontractor_lookup_app_service_pb2 import (
    SubcontractorLookupAppService_lookupRequest,
    SubcontractorLookupAppService_lookupResponse,
)
from src.resource.proto._generated.project.lookup.subcontractor.subcontractor_lookup_app_service_pb2_grpc import (
    SubcontractorLookupAppServiceStub,
)


class SubcontractorLookupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def lookup(
        self,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
        filters: List[dict] = None,
    ) -> SubcontractorLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = SubcontractorLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{SubcontractorLookupClient.lookup.__qualname__}] - grpc call to retrieve lookups from server {self._server}:{self._port}"
                )
                request = SubcontractorLookupAppService_lookupRequest(
                    result_from=resultFrom, result_size=resultSize, orders=orders, filters=filters
                )
                [request.orders.add(orderBy=o["orderBy"], direction=o["direction"]) for o in orders]
                response: SubcontractorLookupAppService_lookupResponse = stub.lookup.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                SubcontractorLookupClient.lookup.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(f"[{SubcontractorLookupClient.lookup.__qualname__}] - grpc response: {response}")

                return SubcontractorLookups(
                    subcontractor_lookups=[
                        self._descriptorByObject(obj=obj) for obj in response[0].subcontractors
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> SubcontractorLookupDescriptor:
        return SubcontractorLookupDescriptor(
            id=obj.id,
            company_name=obj.company_name,
            website_url=obj.website_url,
            contact_person=obj.contact_person,
            email=obj.email,
            phone_number=obj.phone_number,
            address_one=obj.address_one,
            address_two=obj.address_two,
            description=obj.description,
            postal_code=obj.postal_code,
            subcontractor_category=SubcontractorCategoryDescriptor(
                id=obj.subcontractor_category.id, name=obj.subcontractor_category.name
            ),
            country=CountryDescriptor(id=obj.country.id, name=obj.country.name),
            state=StateDescriptor(id=obj.state.id, name=obj.state.name),
            city=CityDescriptor(id=obj.city.id, name=obj.city.name),
        )
