"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client

from src.port_adapter.api.rest.model.response.v1.project.equipment.category.EquipmentCategory import (
    EquipmentCategoryDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.EquipmentCategories import (
    EquipmentCategories,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.category.group.EquipmentCategoryGroups import (
    EquipmentCategoryGroups,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.equipment_category_app_service_pb2 import (
    EquipmentCategoryAppService_equipmentCategoriesResponse,
    EquipmentCategoryAppService_equipmentCategoriesRequest,
    EquipmentCategoryAppService_equipmentCategoryByIdRequest,
    EquipmentCategoryAppService_equipmentCategoryByIdResponse,
    EquipmentCategoryAppService_newIdRequest,
    EquipmentCategoryAppService_newIdResponse,
    EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest,
    EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse,
)
from src.resource.proto._generated.project.equipment_category_app_service_pb2_grpc import (
    EquipmentCategoryAppServiceStub,
)


class EquipmentCategoryClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryAppServiceStub(channel)
            try:
                request = EquipmentCategoryAppService_newIdRequest()
                response: EquipmentCategoryAppService_newIdResponse = (
                    stub.newId.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    EquipmentCategoryClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{EquipmentCategoryClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategories(
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> EquipmentCategories:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryClient.equipmentCategories.__qualname__}] - grpc call to retrieve equipmentCategories from server {self._server}:{self._port}"
                )
                request = EquipmentCategoryAppService_equipmentCategoriesRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: EquipmentCategoryAppService_equipmentCategoriesResponse = stub.equipmentCategories.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryClient.equipmentCategories.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryClient.equipmentCategories.__qualname__}] - grpc response: {response}"
                )

                return EquipmentCategories(
                    equipment_categories=[
                        self._descriptorByObject(obj=equipmentCategory)
                        for equipmentCategory in response[0].equipmentCategories
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryById(self, id) -> EquipmentCategoryDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryClient.equipmentCategoryById.__qualname__}] - grpc call to retrieve equipmentCategory with equipmentCategoryId: {id} from server {self._server}:{self._port}"
                )
                response: EquipmentCategoryAppService_equipmentCategoryByIdResponse = stub.equipmentCategoryById.with_call(
                    EquipmentCategoryAppService_equipmentCategoryByIdRequest(id=id),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryClient.equipmentCategories.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryClient.equipmentCategoryById.__qualname__}] - grpc response: {response}"
                )
                equipmentCategory = response[0].equipmentCategory
                return self._descriptorByObject(obj=equipmentCategory)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def categoryGroupsByCategoryId(
        self,
        id: str,
        resultFrom: int = 0,
        resultSize: int = 10,
        order: List[dict] = None,
    ) -> EquipmentCategoryGroups:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentCategoryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentCategoryClient.categoryGroupsByCategoryId.__qualname__}] - grpc call to retrieve equipmentCategoryGroups by category Id  from server {self._server}:{self._port}"
                )
                request = EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdRequest(
                    id=id, resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse = stub.equipmentCategoryGroupsByCategoryId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentCategoryClient.categoryGroupsByCategoryId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentCategoryClient.categoryGroupsByCategoryId.__qualname__}] - grpc response: {response}"
                )

                return EquipmentCategoryGroups(
                    equipment_category_groups=[
                        EquipmentCategoryGroupDescriptor(
                            id=group.id,
                            name=group.name,
                            equipment_category_id=group.equipmentCategoryId,
                        )
                        for group in response[0].equipmentCategoryGroups
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> EquipmentCategoryDescriptor:
        return EquipmentCategoryDescriptor(
            id=obj.id,
            name=obj.name,
        )
