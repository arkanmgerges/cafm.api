"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.Subcontractor import SubcontractorDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Subcontractors import Subcontractors
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.subcontractor_app_service_pb2_grpc import SubcontractorAppServiceStub
from src.resource.proto._generated.project.subcontractor_app_service_pb2 import \
    SubcontractorppService_subcontractorByIdResponse, SubcontractorAppService_subcontractorsRequest, \
    SubcontractorAppService_subcontractorsResponse, SubcontractorppService_subcontractorByIdRequest


class SubcontractorClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def subcontractors(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> Subcontractors:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = SubcontractorAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{SubcontractorClient.subcontractors.__qualname__}] - grpc call to retrieve subcontractors from server {self._server}:{self._port}')
                request = SubcontractorAppService_subcontractorsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: SubcontractorAppService_subcontractorsResponse = stub.subcontractors.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            SubcontractorClient.subcontractors.__qualname__)),))
                logger.debug(
                    f'[{SubcontractorClient.subcontractors.__qualname__}] - grpc response: {response}')

                return Subcontractors(subcontractors=[self._descriptorByObject(obj=subcontractor) for subcontractor in
                                                      response[0].subcontractors],
                                      item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def subcontractorById(self, id) -> SubcontractorDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = SubcontractorAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{SubcontractorClient.subcontractorById.__qualname__}] - grpc call to retrieve subcontractor with SubcontractorId: {id} from server {self._server}:{self._port}')
                response: SubcontractorppService_subcontractorByIdResponse = stub.subcontractorById.with_call(
                    SubcontractorppService_subcontractorByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            SubcontractorClient.subcontractorById.__qualname__))))
                logger.debug(
                    f'[{SubcontractorClient.subcontractorById.__qualname__}] - grpc response: {response}')
                subcontractor = response[0].subcontractor
                return self._descriptorByObject(obj=subcontractor)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> SubcontractorDescriptor:
        return SubcontractorDescriptor(id=obj.id,
                                       company_name=obj.name,
                                       website_url=obj.websiteUrl,
                                       contact_person=obj.contactPerson,
                                       email=obj.email,
                                       phone_number=obj.phoneNumber,
                                       address_one=obj.addressOne,
                                       address_two=obj.addressTwo)