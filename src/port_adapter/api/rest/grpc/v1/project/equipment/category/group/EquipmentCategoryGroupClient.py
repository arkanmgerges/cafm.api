"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroups import EquipmentCategoryGroups
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.equipment_category_group_app_service_pb2 import \
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse, \
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest, EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest, \
    EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse
from src.resource.proto._generated.project.equipment_category_group_app_service_pb2_grpc import EquipmentCategoryGroupAppServiceStub


class EquipmentCategoryGroupClient(Client):
    def __init__(self):
        self._server = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE', '')
        self._port = os.getenv('CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT', '')

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroups(self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None) -> EquipmentCategoryGroups:
        order = [] if order is None else order
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__}] - grpc call to retrieve equipmentCategoryGroups from server {self._server}:{self._port}')
                request = EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest(resultFrom=resultFrom, resultSize=resultSize)
                [request.order.add(orderBy=o["orderBy"], direction=o["direction"]) for o in order]
                response: EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse = stub.equipmentCategoryGroups.with_call(
                    request,
                    metadata=(('token', self.token), (
                        'opentel',
                        AppDi.instance.get(OpenTelemetry).serializedContext(
                            EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__)),))
                logger.debug(
                    f'[{EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__}] - grpc response: {response}')

                return EquipmentCategoryGroups(equipment_category_groups=[self._descriptorByObject(obj=equipmentCategoryGroup) for equipmentCategoryGroup in
                                                    response[0].equipmentCategoryGroups],
                                     item_count=response[0].itemCount)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroupById(self, id) -> EquipmentCategoryGroupDescriptor:
        with grpc.insecure_channel(f'{self._server}:{self._port}') as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f'[{EquipmentCategoryGroupClient.equipmentCategoryGroupById.__qualname__}] - grpc call to retrieve equipmentCategoryGroup with equipmentCategoryGroupId: {id} from server {self._server}:{self._port}')
                response: EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse = stub.equipmentCategoryGroupById.with_call(
                    EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest(id=id),
                    metadata=(('token', self.token), (
                        'opentel', AppDi.instance.get(OpenTelemetry).serializedContext(
                            EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__))))
                logger.debug(
                    f'[{EquipmentCategoryGroupClient.equipmentCategoryGroupById.__qualname__}] - grpc response: {response}')
                equipmentCategoryGroup = response[0].equipmentCategoryGroup
                return self._descriptorByObject(obj=equipmentCategoryGroup)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> EquipmentCategoryGroupDescriptor:
        return EquipmentCategoryGroupDescriptor(id=obj.id,
                                      name=obj.name,
                                      equipment_category_id=obj.equipmentCategoryId,
                                      )
