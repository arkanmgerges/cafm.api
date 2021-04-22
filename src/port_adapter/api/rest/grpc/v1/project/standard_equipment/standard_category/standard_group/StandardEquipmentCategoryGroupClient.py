"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroups import (
    StandardEquipmentCategoryGroups,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_equipment_category_group_app_service_pb2 import (
    StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse,
    StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest,
    StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest,
    StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse,
    StandardEquipmentCategoryGroupAppService_newIdResponse,
    StandardEquipmentCategoryGroupAppService_newIdRequest,
)
from src.resource.proto._generated.project.standard_equipment_category_group_app_service_pb2_grpc import (
    StandardEquipmentCategoryGroupAppServiceStub,
)


class StandardEquipmentCategoryGroupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryGroupAppServiceStub(channel)
            try:
                request = StandardEquipmentCategoryGroupAppService_newIdRequest()
                response: StandardEquipmentCategoryGroupAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardEquipmentCategoryGroupClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryGroupClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardEquipmentCategoryGroups(
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> StandardEquipmentCategoryGroups:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroups.__qualname__}] - grpc call to retrieve standardEquipmentCategoryGroups from server {self._server}:{self._port}"
                )
                request = StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupsResponse = stub.standardEquipmentCategoryGroups.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroups.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroups.__qualname__}] - grpc response: {response}"
                )

                return StandardEquipmentCategoryGroups(
                    standard_equipment_category_groups=[
                        self._descriptorByObject(obj=standardEquipmentCategoryGroup)
                        for standardEquipmentCategoryGroup in response[
                            0
                        ].standardEquipmentCategoryGroups
                    ],
                    item_count=response[0].itemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardEquipmentCategoryGroupById(
        self, id
    ) -> StandardEquipmentCategoryGroupDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardEquipmentCategoryGroupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroupById.__qualname__}] - grpc call to retrieve standardEquipmentCategoryGroup with standardEquipmentCategoryGroupId: {id} from server {self._server}:{self._port}"
                )
                response: StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdResponse = stub.standardEquipmentCategoryGroupById.with_call(
                    StandardEquipmentCategoryGroupAppService_standardEquipmentCategoryGroupByIdRequest(
                        id=id
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroupById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardEquipmentCategoryGroupClient.standardEquipmentCategoryGroupById.__qualname__}] - grpc response: {response}"
                )
                standardEquipmentCategoryGroup = response[
                    0
                ].standardEquipmentCategoryGroup
                return self._descriptorByObject(obj=standardEquipmentCategoryGroup)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> StandardEquipmentCategoryGroupDescriptor:
        return StandardEquipmentCategoryGroupDescriptor(
            id=obj.id,
            name=obj.name,
            standard_equipment_category_id=obj.standardEquipmentCategoryId,
        )
