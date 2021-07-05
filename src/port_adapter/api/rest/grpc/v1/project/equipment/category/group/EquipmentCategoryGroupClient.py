"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroups import (
    EquipmentCategoryGroups,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.equipment_category_group_app_service_pb2 import (
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest,
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse,
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse,
    EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest,
    EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest,
    EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse,
    EquipmentCategoryGroupAppService_newIdRequest,
    EquipmentCategoryGroupAppService_newIdResponse,
)
from src.resource.proto._generated.project.equipment_category_group_app_service_pb2_grpc import (
    EquipmentCategoryGroupAppServiceStub,
)


class EquipmentCategoryGroupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                request = EquipmentCategoryGroupAppService_newIdRequest()
                response: EquipmentCategoryGroupAppService_newIdResponse = (
                    stub.new_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    EquipmentCategoryGroupClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroups(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> EquipmentCategoryGroups:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__}] - grpc call to retrieve equipmentCategoryGroups from server {self._server}:{self._port}"
                )
                request = (
                    EquipmentCategoryGroupAppService_equipmentCategoryGroupsRequest(
                        result_from=resultFrom, result_size=resultSize
                    )
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: EquipmentCategoryGroupAppService_equipmentCategoryGroupsResponse = stub.equipment_category_groups.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__}] - grpc response: {response}"
                )

                return EquipmentCategoryGroups(
                    equipment_category_groups=[
                        self._descriptorByObject(obj=equipmentCategoryGroup)
                        for equipmentCategoryGroup in response[
                            0
                        ].equipment_category_groups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None, equipmentProjectCategoryId:str = None
    ) -> EquipmentCategoryGroups:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroupsByEquipmentProjectCategoryId.__qualname__}] - grpc call to retrieve equipmentCategoryGroups from server {self._server}:{self._port}"
                )
                request = (
                    EquipmentCategoryGroupAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdRequest(
                        result_from=resultFrom, result_size=resultSize, equipment_project_category_id=equipmentProjectCategoryId
                    )
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: EquipmentCategoryGroupAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse = stub.equipment_category_groups_by_equipment_project_category_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryGroupClient.equipmentCategoryGroupsByEquipmentProjectCategoryId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroupsByEquipmentProjectCategoryId.__qualname__}] - grpc response: {response}"
                )

                return EquipmentCategoryGroups(
                    equipment_category_groups=[
                        self._descriptorByObject(obj=equipmentCategoryGroup)
                        for equipmentCategoryGroup in response[
                            0
                        ].equipment_category_groups
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroupById(self, id) -> EquipmentCategoryGroupDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroupById.__qualname__}] - grpc call to retrieve equipmentCategoryGroup with equipmentCategoryGroupId: {id} from server {self._server}:{self._port}"
                )
                response: EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdResponse = stub.equipment_category_group_by_id.with_call(
                    EquipmentCategoryGroupAppService_equipmentCategoryGroupByIdRequest(
                        id=id
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryGroupClient.equipmentCategoryGroups.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryGroupClient.equipmentCategoryGroupById.__qualname__}] - grpc response: {response}"
                )
                equipmentCategoryGroup = response[0].equipment_category_group
                return self._descriptorByObject(obj=equipmentCategoryGroup)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> EquipmentCategoryGroupDescriptor:
        return EquipmentCategoryGroupDescriptor(
            id=obj.id,
            name=obj.name,
            project_id=obj.project_id,
            equipment_project_category_id=obj.equipment_project_category_id
        )
