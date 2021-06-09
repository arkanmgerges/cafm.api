"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client

from src.port_adapter.api.rest.model.response.v1.identity.City import City
from src.port_adapter.api.rest.model.response.v1.identity.Cities import (
    Cities,
    CityDescriptor,
)

from src.port_adapter.api.rest.model.response.v1.identity.Country import Country
from src.port_adapter.api.rest.model.response.v1.identity.Countries import (
    Countries,
    CountryDescriptor,
)

from src.port_adapter.api.rest.model.response.v1.identity.State import State
from src.port_adapter.api.rest.model.response.v1.identity.States import (
    States,
    StateDescriptor,
)

from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.country_app_service_pb2 import (
    CountryAppService_countriesRequest,
    CountryAppService_countriesResponse,
    CountryAppService_countryByIdRequest,
    CountryAppService_countryByIdResponse,
    CountryAppService_citiesByCountryIdResponse,
    CountryAppService_citiesByCountryIdRequest,
    CountryAppService_cityByCountryIdResponse,
    CountryAppService_cityByCountryIdRequest,
    CountryAppService_statesByCountryIdRequest,
    CountryAppService_statesByCountryIdResponse,
    CountryAppService_stateByCountryIdAndStateIdRequest,
    CountryAppService_stateByCountryIdAndStateIdResponse,
    CountryAppService_citiesByCountryIdAndStateIdRequest,
    CountryAppService_citiesByCountryIdAndStateIdResponse,
)
from src.resource.proto._generated.identity.country_app_service_pb2_grpc import (
    CountryAppServiceStub,
)


class CountryClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def countries(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> Countries:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.countries.__qualname__}] - grpc call to retrieve countries from server {self._server}:{self._port}"
                )
                request = CountryAppService_countriesRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                CountryAppService_countriesRequest()
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: CountryAppService_countriesResponse = (
                    stub.countries.with_call(request, metadata=(("token", self.token),))
                )
                logger.debug(
                    f"[{CountryClient.countries.__qualname__}] - grpc response: {response}"
                )

                return Countries(
                    countries=[
                        Country(
                            id=country.id,
                            locale_code=country.localeCode,
                            continent_code=country.continentCode,
                            continent_name=country.continentName,
                            country_iso_code=country.countryIsoCode,
                            country_name=country.countryName,
                            is_in_european_union=country.isInEuropeanUnion,
                        )
                        for country in response[0].countries
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def countryById(self, countryId: int = None) -> CountryDescriptor:

        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.countryById.__qualname__}] - grpc call to retrieve country with countryId: {countryId} from server {self._server}:{self._port}"
                )
                response: CountryAppService_countryByIdResponse = (
                    stub.countryById.with_call(
                        CountryAppService_countryByIdRequest(id=countryId),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    CountryClient.countryById.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{CountryClient.countryById.__qualname__}] - grpc response: {response}"
                )

                return CountryDescriptor(
                    id=response[0].country.id,
                    locale_code=response[0].country.localeCode,
                    continent_code=response[0].country.continentCode,
                    continent_name=response[0].country.continentName,
                    country_iso_code=response[0].country.countryIsoCode,
                    country_name=response[0].country.countryName,
                    is_in_european_union=response[0].country.isInEuropeanUnion,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def citiesByCountryId(
        self,
        countryId: int,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> Cities:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.citiesByCountryId.__qualname__}] - grpc call to retrieve a country cities: {countryId} from server {self._server}:{self._port}"
                )
                request = CountryAppService_citiesByCountryIdRequest(
                    id=countryId, resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: CountryAppService_citiesByCountryIdResponse = (
                    stub.citiesByCountryId.with_call(
                        request, metadata=(("token", self.token),)
                    )
                )

                logger.debug(
                    f"[{CountryClient.countryById.__qualname__}] - grpc response: {response}"
                )

                return Cities(
                    cities=[
                        City(
                            id=city.id,
                            locale_code=city.localeCode,
                            continent_code=city.continentCode,
                            continent_name=city.continentName,
                            country_iso_code=city.countryIsoCode,
                            country_name=city.countryName,
                            subdivision_1_iso_code=city.subdivisionOneIsoCode,
                            subdivision_1_name=city.subdivisionOneIsoName,
                            city_name=city.cityName,
                            time_zone=city.timeZone,
                            is_in_european_union=city.isInEuropeanUnion,
                        )
                        for city in response[0].cities
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def cityByCountryId(self, countryId: int, cityId: int) -> CityDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.cityByCountryId.__qualname__}] - grpc call to retrieve city with countryId: {countryId} & cityId: {cityId} from server {self._server}:{self._port}"
                )
                response: CountryAppService_cityByCountryIdResponse = (
                    stub.cityByCountryId.with_call(
                        CountryAppService_cityByCountryIdRequest(
                            countryId=countryId, cityId=cityId
                        ),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    CountryClient.cityByCountryId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{CountryClient.cityByCountryId.__qualname__}] - grpc response: {response}"
                )

                city = response[0].city
                return CityDescriptor(
                    id=city.id,
                    locale_code=city.localeCode,
                    continent_code=city.continentCode,
                    continent_name=city.continentName,
                    country_iso_code=city.countryIsoCode,
                    country_name=city.countryName,
                    subdivision_1_iso_code=city.subdivisionOneIsoCode,
                    subdivision_1_name=city.subdivisionOneIsoName,
                    city_name=city.cityName,
                    time_zone=city.timeZone,
                    is_in_european_union=city.isInEuropeanUnion,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def stateByCountryIdAndStateId(self, countryId: int, stateId: str):
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.stateByCountryIdAndStateId.__qualname__}] - grpc call to retrieve city with countryId: {countryId} & stateId: {stateId} from server {self._server}:{self._port}"
                )
                response: CountryAppService_stateByCountryIdAndStateIdResponse = stub.stateByCountryIdAndStateId.with_call(
                    CountryAppService_stateByCountryIdAndStateIdRequest(
                        countryId=countryId,
                        stateId=stateId,
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                CountryClient.stateByCountryIdAndStateId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{CountryClient.stateByCountryIdAndStateId.__qualname__}] - grpc response: {response}"
                )

                state = response[0].state
                return StateDescriptor(
                    id=state.id,
                    name=state.name,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def statesByCountryId(
        self,
        countryId: int,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> States:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.statesByCountryId.__qualname__}] - grpc call to retrieve a country states: {countryId} from server {self._server}:{self._port}"
                )
                request = CountryAppService_statesByCountryIdRequest(
                    id=countryId, resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: CountryAppService_statesByCountryIdResponse = (
                    stub.statesByCountryId.with_call(
                        request, metadata=(("token", self.token),)
                    )
                )

                logger.debug(
                    f"[{CountryClient.statesByCountryId.__qualname__}] - grpc response: {response}"
                )

                return States(
                    states=[
                        State(id=state.id, name=state.name)
                        for state in response[0].states
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def citiesByCountryIdAndStateId(
        self,
        countryId: int = 0,
        stateId: str = "",
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> Cities:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{CountryClient.citiesByCountryIdAndStateId.__qualname__}] - grpc call to retrieve citiesByStateId from server {self._server}:{self._port}"
                )
                request = CountryAppService_citiesByCountryIdAndStateIdRequest(
                    countryId=countryId,
                    stateId=stateId,
                    resultFrom=resultFrom,
                    resultSize=resultSize,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: CountryAppService_citiesByCountryIdAndStateIdResponse = (
                    stub.citiesByCountryIdAndStateId.with_call(
                        request, metadata=(("token", self.token),)
                    )
                )
                logger.debug(
                    f"[{CountryClient.citiesByCountryIdAndStateId.__qualname__}] - grpc response: {response}"
                )

                return Cities(
                    cities=[
                        City(
                            id=city.id,
                            locale_code=city.localeCode,
                            continent_code=city.continentCode,
                            continent_name=city.continentName,
                            country_iso_code=city.countryIsoCode,
                            country_name=city.countryName,
                            subdivision_1_iso_code=city.subdivisionOneIsoCode,
                            subdivision_1_name=city.subdivisionOneIsoName,
                            city_name=city.cityName,
                            time_zone=city.timeZone,
                            is_in_european_union=city.isInEuropeanUnion,
                        )
                        for city in response[0].cities
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
