"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.equipment.input.EquipmentInput import (
    EquipmentInputDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.equipment.input.EquipmentInputs import (
    EquipmentInputs,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.equipment_input_app_service_pb2 import (
    EquipmentInputAppService_equipmentInputsResponse,
    EquipmentInputAppService_equipmentInputsRequest,
    EquipmentInputAppService_equipmentInputByIdRequest,
    EquipmentInputAppService_equipmentInputsByEquipmentIdRequest,
    EquipmentInputAppService_equipmentInputsByEquipmentIdResponse,
    EquipmentInputAppService_equipmentInputByIdResponse,
    EquipmentInputAppService_newIdRequest,
    EquipmentInputAppService_newIdResponse,
)
from src.resource.proto._generated.project.equipment_input_app_service_pb2_grpc import (
    EquipmentInputAppServiceStub,
)


class EquipmentInputClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentInputAppServiceStub(channel)
            try:
                request = EquipmentInputAppService_newIdRequest()
                response: EquipmentInputAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentInputClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentInputClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentInputs(
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> EquipmentInputs:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentInputAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputs.__qualname__}] - grpc call to retrieve equipmentInputs from server {self._server}:{self._port}"
                )
                request = EquipmentInputAppService_equipmentInputsRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: EquipmentInputAppService_equipmentInputsResponse = (
                    stub.equipmentInputs.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    EquipmentInputClient.equipmentInputs.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputs.__qualname__}] - grpc response: {response}"
                )

                return EquipmentInputs(
                    equipment_inputs=[
                        self._descriptorByObject(obj=equipmentInput)
                        for equipmentInput in response[0].equipmentInputs
                    ],
                    item_count=response[0].itemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentInputsByEquipmentId(
        self,
        equipmentId: str = None,
        resultFrom: int = 0,
        resultSize: int = 10,
        order: List[dict] = None,
    ) -> EquipmentInputs:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentInputAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputsByEquipmentId.__qualname__}] - grpc call to retrieve equipmentInputs by equipmentId from server {self._server}:{self._port}"
                )
                request = EquipmentInputAppService_equipmentInputsByEquipmentIdRequest(
                    equipmentId=equipmentId,
                    resultFrom=resultFrom,
                    resultSize=resultSize,
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: EquipmentInputAppService_equipmentInputsByEquipmentIdResponse = stub.equipmentInputsByEquipmentId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                EquipmentInputClient.equipmentInputsByEquipmentId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputsByEquipmentId.__qualname__}] - grpc response: {response}"
                )

                return EquipmentInputs(
                    equipment_inputs=[
                        self._descriptorByObject(obj=equipmentInput)
                        for equipmentInput in response[0].equipmentInputs
                    ],
                    item_count=response[0].itemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def equipmentInputById(self, id) -> EquipmentInputDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentInputAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputById.__qualname__}] - grpc call to retrieve equipmentInput with equipmentInputId: {id} from server {self._server}:{self._port}"
                )
                response: EquipmentInputAppService_equipmentInputByIdResponse = (
                    stub.equipmentInputById.with_call(
                        EquipmentInputAppService_equipmentInputByIdRequest(id=id),
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    EquipmentInputClient.equipmentInputs.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{EquipmentInputClient.equipmentInputById.__qualname__}] - grpc response: {response}"
                )
                equipmentInput = response[0].equipmentInput
                return self._descriptorByObject(obj=equipmentInput)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> EquipmentInputDescriptor:
        return EquipmentInputDescriptor(
            id=obj.id,
            name=obj.name,
            value=obj.value,
            unit_id=obj.unitId,
            equipment_id=obj.equipmentId,
        )
