"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.StandardEquipmentCategory import (
    StandardEquipmentCategoryDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.StandardEquipmentCategories import (
    StandardEquipmentCategories,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_equipment_category_app_service_pb2 import (
    StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse,
    StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest,
    StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest,
    StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse,
    StandardEquipmentCategoryAppService_newIdResponse,
    StandardEquipmentCategoryAppService_newIdRequest,
)
from src.resource.proto._generated.project.standard_equipment_category_app_service_pb2_grpc import (
    StandardEquipmentCategoryAppServiceStub,
)


class StandardEquipmentCategoryClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryAppServiceStub(channel)
            try:
                request = StandardEquipmentCategoryAppService_newIdRequest()
                response: StandardEquipmentCategoryAppService_newIdResponse = (
                    stub.new_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    StandardEquipmentCategoryClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardEquipmentCategories(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> StandardEquipmentCategories:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardEquipmentCategoryClient.standardEquipmentCategories.__qualname__}] - grpc call to retrieve standardEquipmentCategories from server {self._server}:{self._port}"
                )
                request = StandardEquipmentCategoryAppService_standardEquipmentCategoriesRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: StandardEquipmentCategoryAppService_standardEquipmentCategoriesResponse = stub.standard_equipment_categories.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardEquipmentCategoryClient.standardEquipmentCategories.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryClient.standardEquipmentCategories.__qualname__}] - grpc response: {response}"
                )

                return StandardEquipmentCategories(
                    standard_equipment_categories=[
                        self._descriptorByObject(obj=standardEquipmentCategory)
                        for standardEquipmentCategory in response[
                            0
                        ].standard_equipment_categories
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardEquipmentCategoryById(self, id) -> StandardEquipmentCategoryDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardEquipmentCategoryClient.standardEquipmentCategoryById.__qualname__}] - grpc call to retrieve standardEquipmentCategory with standardEquipmentCategoryId: {id} from server {self._server}:{self._port}"
                )
                response: StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdResponse = stub.standard_equipment_category_by_id.with_call(
                    StandardEquipmentCategoryAppService_standardEquipmentCategoryByIdRequest(
                        id=id
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardEquipmentCategoryClient.standardEquipmentCategoryById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryClient.standardEquipmentCategoryById.__qualname__}] - grpc response: {response}"
                )
                standardEquipmentCategory = response[0].standard_equipment_category
                return self._descriptorByObject(obj=standardEquipmentCategory)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> StandardEquipmentCategoryDescriptor:
        return StandardEquipmentCategoryDescriptor(
            id=obj.id,
            name=obj.name,
        )
