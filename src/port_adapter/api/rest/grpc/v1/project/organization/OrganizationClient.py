"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Organization import OrganizationDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Organizations import Organizations
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.organization_app_service_pb2 import \
    OrganizationAppService_organizationsResponse, \
    OrganizationAppService_organizationsRequest, OrganizationAppService_organizationByIdRequest, \
    OrganizationAppService_organizationByIdResponse, OrganizationAppService_newIdRequest, \
    OrganizationAppService_newIdResponse
from src.resource.proto._generated.project.organization_app_service_pb2_grpc import OrganizationAppServiceStub


class OrganizationClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                request = OrganizationAppService_newIdRequest()
                response: OrganizationAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(OrganizationClient.newId.__qualname__))))
                logger.debug(
                    f'[{OrganizationClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def organizations(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Organizations:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{OrganizationClient.organizations.__qualname__}] - grpc call to retrieve organizations from server {self._server}:{self._port}')
                request = OrganizationAppService_organizationsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: OrganizationAppService_organizationsResponse = stub.organizations.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            OrganizationClient.organizations.__qualname__)),))
                logger.debug(
                    f'[{OrganizationClient.organizations.__qualname__}] - grpc response: {response}')

                return Organizations(organizations=[self._descriptorByObject(obj=organization) for organization in
                                                    response[0].organizations],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def organizationById(self, id) -> OrganizationDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = OrganizationAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{OrganizationClient.organizationById.__qualname__}] - grpc call to retrieve organization with organizationId: {id} from server {self._server}:{self._port}')
                response: OrganizationAppService_organizationByIdResponse = stub.organizationById.with_call(
                    OrganizationAppService_organizationByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            OrganizationClient.organizations.__qualname__))))
                logger.debug(
                    f'[{OrganizationClient.organizationById.__qualname__}] - grpc response: {response}')
                organization = response[0].organization
                return self._descriptorByObject(obj=organization)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> OrganizationDescriptor:
        return OrganizationDescriptor(id=obj.id,
                                      name=obj.name,
                                      website_url=obj.websiteUrl,
                                      organization_type=obj.organizationType,
                                      address_one=obj.addressOne,
                                      address_two=obj.addressTwo,
                                      postal_code=obj.postalCode,
                                      country_id=obj.countryId,
                                      city_id=obj.cityId,
                                      country_state_name=obj.countryStateName,
                                      manager_first_name=obj.managerFirstName,
                                      manager_last_name=obj.managerLastName,
                                      manager_email=obj.managerEmail,
                                      manager_phone_number=obj.managerPhoneNumber,
                                      manager_avatar=obj.managerAvatar
                                      )
