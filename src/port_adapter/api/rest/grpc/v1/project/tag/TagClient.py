"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.tag.Tag import TagDescriptor
from src.port_adapter.api.rest.model.response.v1.project.tag.Tags import Tags
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.tag_app_service_pb2 import \
    TagAppService_tagsResponse, \
    TagAppService_tagsRequest, TagAppService_tagByIdRequest, \
    TagAppService_tagByIdResponse, TagAppService_newIdResponse, \
    TagAppService_newIdRequest
from src.resource.proto._generated.project.tag_app_service_pb2_grpc import TagAppServiceStub

class TagClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = TagAppServiceStub(channel)
            try:
                request = TagAppService_newIdRequest()
                response: TagAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            TagClient.newId.__qualname__))))
                logger.debug(
                    f'[{TagClient.newId.__qualname__}] - grpc response: {response}')
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def tags(self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None) -> Tags:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = TagAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{TagClient.tags.__qualname__}] - grpc call to retrieve tags from server {self._server}:{self._port}')
                request = TagAppService_tagsRequest(result_from=resultFrom, result_size=resultSize)
                [request.orders.add(order_by=o["orderBy"], direction=o["direction"]) for o in orders]
                response: TagAppService_tagsResponse = stub.tags.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            TagClient.tags.__qualname__)),))
                logger.debug(
                    f'[{TagClient.tags.__qualname__}] - grpc response: {response}')

                return Tags(tags=[self._descriptorByObject(obj=tag) for tag in
                                                    response[0].tags],
                                     total_item_count=response[0].total_item_count)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def tagById(self, id) -> TagDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = TagAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{TagClient.tagById.__qualname__}] - grpc call to retrieve tag with tagId: {id} from server {self._server}:{self._port}')
                response: TagAppService_tagByIdResponse = stub.tag_by_id.with_call(
                    TagAppService_tagByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            TagClient.tagById.__qualname__))))
                logger.debug(
                    f'[{TagClient.tagById.__qualname__}] - grpc response: {response}')
                tag = response[0].tag
                return self._descriptorByObject(obj=tag)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> TagDescriptor:
        return TagDescriptor(id=obj.id,
                                      name=obj.name,
                                      )
