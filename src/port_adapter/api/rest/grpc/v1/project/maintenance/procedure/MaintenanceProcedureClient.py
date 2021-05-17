"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.MaintenanceProcedure import (
    MaintenanceProcedureDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.MaintenanceProcedures import (
    MaintenanceProcedures,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresResponse,
    MaintenanceProcedureAppService_maintenanceProceduresRequest,
    MaintenanceProcedureAppService_maintenanceProcedureByIdRequest,
    MaintenanceProcedureAppService_maintenanceProcedureByIdResponse,
    MaintenanceProcedureAppService_newIdRequest,
    MaintenanceProcedureAppService_newIdResponse,
)
from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2_grpc import (
    MaintenanceProcedureAppServiceStub,
)
from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest,
)
from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse,
)


class MaintenanceProcedureClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = MaintenanceProcedureAppServiceStub(channel)
            try:
                request = MaintenanceProcedureAppService_newIdRequest()
                response: MaintenanceProcedureAppService_newIdResponse = (
                    stub.newId.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    MaintenanceProcedureClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{MaintenanceProcedureClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedures(
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> MaintenanceProcedures:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = MaintenanceProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProcedures.__qualname__}] - grpc call to retrieve maintenanceProcedures from server {self._server}:{self._port}"
                )
                request = MaintenanceProcedureAppService_maintenanceProceduresRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: MaintenanceProcedureAppService_maintenanceProceduresResponse = stub.maintenanceProcedures.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                MaintenanceProcedureClient.maintenanceProcedures.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProcedures.__qualname__}] - grpc response: {response}"
                )

                return MaintenanceProcedures(
                    maintenance_procedures=[
                        self._descriptorByObject(obj=maintenanceProcedure)
                        for maintenanceProcedure in response[0].maintenanceProcedures
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureById(self, id) -> MaintenanceProcedureDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = MaintenanceProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProcedureById.__qualname__}] - grpc call to retrieve maintenanceProcedure with maintenanceProcedureId: {id} from server {self._server}:{self._port}"
                )
                response: MaintenanceProcedureAppService_maintenanceProcedureByIdResponse = stub.maintenanceProcedureById.with_call(
                    MaintenanceProcedureAppService_maintenanceProcedureByIdRequest(
                        id=id
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                MaintenanceProcedureClient.maintenanceProcedures.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProcedureById.__qualname__}] - grpc response: {response}"
                )
                maintenanceProcedure = response[0].maintenanceProcedure
                return self._descriptorByObject(obj=maintenanceProcedure)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def maintenanceProceduresByEquipmentId(
        self,
        equipmentId: str = None,
        resultFrom: int = 0,
        resultSize: int = 10,
        order: List[dict] = None,
    ) -> MaintenanceProcedures:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = MaintenanceProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProcedures.__qualname__}] - grpc call to retrieve maintenanceProcedures from server {self._server}:{self._port}"
                )
                request = MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest(
                    equipmentId=equipmentId,
                    resultFrom=resultFrom,
                    resultSize=resultSize,
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse = stub.maintenanceProceduresByEquipmentId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                MaintenanceProcedureClient.maintenanceProcedures.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{MaintenanceProcedureClient.maintenanceProceduresByEquipmentId.__qualname__}] - grpc response: {response}"
                )

                return MaintenanceProcedures(
                    maintenance_procedures=[
                        self._descriptorByObject(obj=maintenanceProcedure)
                        for maintenanceProcedure in response[0].maintenanceProcedures
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> MaintenanceProcedureDescriptor:
        return MaintenanceProcedureDescriptor(
            id=obj.id,
            name=obj.name,
            type=obj.type,
            sub_type=obj.subType,
            frequency=obj.frequency,
            start_date=obj.startDate,
            subcontractor_id=obj.subcontractorId,
            equipment_id=obj.equipmentId,
        )
