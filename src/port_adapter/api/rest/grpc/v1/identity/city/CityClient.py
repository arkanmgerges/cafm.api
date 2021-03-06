"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Cities import (
    Cities,
    CityDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.identity.City import City
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.city_app_service_pb2 import (
    CityAppService_citiesRequest,
    CityAppService_citiesResponse,
    CityAppService_cityByIdResponse,
    CityAppService_cityByIdRequest,
)
from src.resource.proto._generated.identity.city_app_service_pb2_grpc import (
    CityAppServiceStub,
)


class CityClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def cities(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Cities:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CityAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CityClient.cities.__qualname__}] - grpc call to retrieve cities from server {self._server}:{self._port}"
                )
                request = CityAppService_citiesRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                # metadata=(('token', self.token), ('opentel', AppDi.instance.get(
                #     OpenTelemetry).serializedContext(
                #     CityClient.cities.__qualname__))))
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: CityAppService_citiesResponse = stub.cities.with_call(
                    request, metadata=(("token", self.token),)
                )
                logger.debug(
                    f"[{CityClient.cities.__qualname__}] - grpc response: {response}"
                )

                return Cities(
                    cities=[
                        City(
                            id=city.id,
                            locale_code=city.locale_code,
                            continent_code=city.continent_code,
                            continent_name=city.continent_name,
                            country_iso_code=city.country_iso_code,
                            country_name=city.country_name,
                            subdivision_1_iso_code=city.subdivision_one_iso_code,
                            subdivision_1_name=city.subdivision_one_iso_name,
                            city_name=city.city_name,
                            time_zone=city.time_zone,
                            is_in_european_union=city.is_in_european_union,
                        )
                        for city in response[0].cities
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def cityById(self, cityId: int = "") -> CityDescriptor:

        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CityAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CityClient.cityById.__qualname__}] - grpc call to retrieve city with cityId: {cityId} from server {self._server}:{self._port}"
                )
                response: CityAppService_cityByIdResponse = stub.city_by_id.with_call(
                    CityAppService_cityByIdRequest(id=cityId),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                CityClient.cityById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{CityClient.cityById.__qualname__}] - grpc response: {response}"
                )

                return CityDescriptor(
                    id=response[0].city.id,
                    locale_code=response[0].city.locale_code,
                    continent_code=response[0].city.continent_code,
                    continent_name=response[0].city.continent_name,
                    country_iso_code=response[0].city.country_iso_code,
                    country_name=response[0].city.country_name,
                    subdivision_1_iso_code=response[0].city.subdivision_one_iso_code,
                    subdivision_1_name=response[0].city.subdivision_one_iso_name,
                    city_name=response[0].city.city_name,
                    time_zone=response[0].city.time_zone,
                    is_in_european_union=response[0].city.is_in_european_union,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
