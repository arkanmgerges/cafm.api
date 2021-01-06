"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
import grpc
import src.port_adapter.AppDi as AppDi

from typing import List
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Countries import Countries, CountryDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Country import Country
from src.resource.logging.logger import logger
from src.resource.proto._generated.identity.country_app_service_pb2 import CountryAppService_countriesRequest, \
    CountryAppService_countriesResponse, CountryAppService_countryByIdRequest, CountryAppService_countryByIdResponse
from src.resource.proto._generated.identity.country_app_service_pb2_grpc import CountryAppServiceStub


class CountryClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def countries(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Countries:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CountryClient.countries.__qualname__}] - grpc call to retrieve countries from server {self._server}:{self._port}')
                request = CountryAppService_countriesRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: CountryAppService_countriesResponse = stub.countries.with_call(
                    request,
                    metadata=(('token', self.token),))
                logger.debug(
                    f'[{CountryClient.countries.__qualname__}] - grpc response: {response}')

                return Countries(
                    countries=[Country(id=country.id,
                                       geo_name_id=country.geoNameId,
                                       locale_code=country.localeCode,
                                       continent_code=country.continentCode,
                                       continent_name=country.continentName,
                                       country_iso_code=country.countryIsoCode,
                                       country_name=country.countryName,
                                       is_in_european_union=country.isInEuropeanUnion)
                               for country in
                               response[0].countries],
                    item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def countryById(self, countryId) -> CountryDescriptor:

        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = CountryAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{CountryClient.countryById.__qualname__}] - grpc call to retrieve country with countryId: {countryId} from server {self._server}:{self._port}')
                response: CountryAppService_countryByIdResponse = stub.countryById.with_call(
                    CountryAppService_countryByIdRequest(id=countryId),
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(CountryClient.countryById.__qualname__))))
                logger.debug(
                    f'[{CountryClient.countryById.__qualname__}] - grpc response: {response}')

                return CountryDescriptor(id=response[0].country.id,
                                         geo_name_id=response[0].country.geoNameId,
                                         locale_code=response[0].country.localeCode,
                                         continent_code=response[0].country.continentCode,
                                         continent_name=response[0].country.continentName,
                                         country_iso_code=response[0].country.countryIsoCode,
                                         country_name=response[0].country.countryName,
                                         is_in_european_union=response[0].country.isInEuropeanUnion)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
