"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Cities import Cities, CityDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.City import City
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.city_app_service_pb2 import (CityAppService_citiesRequest,
                                                                         CityAppService_citiesResponse,
                                                                         CityAppService_cityByIdResponse,
                                                                         CityAppService_cityByIdRequest,
                                                                         CityAppService_citiesByStateIdResponse,
                                                                         CityAppService_citiesByStateIdRequest)
from src.resource.proto._generated.identity.city_app_service_pb2_grpc import CityAppServiceStub


class CityClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def cities(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Cities:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = CityAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CityClient.cities.__qualname__}] - grpc call to retrieve cities from server {self._server}:{self._port}')
                request = CityAppService_citiesRequest(resultFrom=resultFrom, resultSize=resultSize)
                # metadata=(('token', self.token), ('opentel', AppDi.instance.get(
                #     OpenTelemetry).serializedContext(
                #     CityClient.cities.__qualname__))))
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: CityAppService_citiesResponse = stub.cities.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{CityClient.cities.__qualname__}] - grpc response: {response}')

                return Cities(
                    cities=[City(id=city.id, locale_code=city.localeCode,
                                 continent_code=city.continentCode, continent_name=city.continentName,
                                 country_iso_code=city.countryIsoCode, country_name=city.countryName,
                                 subdivision_1_iso_code=city.subdivisionOneIsoCode,
                                 subdivision_1_name=city.subdivisionOneIsoName,
                                 city_name=city.cityName, time_zone=city.timeZone,
                                 is_in_european_union=city.isInEuropeanUnion) for city in response[0].cities],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def cityById(self, cityId: int = '') -> CityDescriptor:

        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = CityAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CityClient.cityById.__qualname__}] - grpc call to retrieve city with cityId: {cityId} from server {self._server}:{self._port}')
                response: CityAppService_cityByIdResponse = stub.cityById.with_call(
                    CityAppService_cityByIdRequest(id=cityId),
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            CityClient.cityById.__qualname__))))
                logger.debug(
                    f'[{CityClient.cityById.__qualname__}] - grpc response: {response}')

                return CityDescriptor(id=response[0].city.id,
                                      locale_code=response[0].city.localeCode,
                                      continent_code=response[0].city.continentCode,
                                      continent_name=response[0].city.continentName,
                                      country_iso_code=response[0].city.countryIsoCode,
                                      country_name=response[0].city.countryName,
                                      subdivision_1_iso_code=response[0].city.subdivisionOneIsoCode,
                                      subdivision_1_name=response[0].city.subdivisionOneIsoName,
                                      city_name=response[0].city.cityName,
                                      time_zone=response[0].city.timeZone,
                                      is_in_european_union=response[
                                          0].city.isInEuropeanUnion)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def citiesByStateId(self, stateId: str = '', resultFrom: int = 0, resultSize: int = 10,
                        order: List[dict] = None) -> Cities:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = CityAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CityClient.cities.__qualname__}] - grpc call to retrieve citiesByStateId from server {self._server}:{self._port}')
                request = CityAppService_citiesByStateIdRequest(id=stateId, resultFrom=resultFrom,
                                                                resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: CityAppService_citiesByStateIdResponse = stub.citiesByStateId.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{CityClient.citiesByStateId.__qualname__}] - grpc response: {response}')

                return Cities(
                    cities=[City(id=city.id, locale_code=city.localeCode,
                                 continent_code=city.continentCode, continent_name=city.continentName,
                                 country_iso_code=city.countryIsoCode, country_name=city.countryName,
                                 subdivision_1_iso_code=city.subdivisionOneIsoCode,
                                 subdivision_1_name=city.subdivisionOneIsoName,
                                 city_name=city.cityName, time_zone=city.timeZone,
                                 is_in_european_union=city.isInEuropeanUnion) for city in response[0].cities],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
