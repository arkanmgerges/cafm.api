"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedure import (
    DailyCheckProcedureDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedures import (
    DailyCheckProcedures,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2 import (
    DailyCheckProcedureAppService_dailyCheckProceduresResponse,
    DailyCheckProcedureAppService_dailyCheckProceduresRequest,
    DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest,
    DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse,
    DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentOrGroupIdResponse,
    DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentOrGroupIdRequest,
    DailyCheckProcedureAppService_newIdRequest,
    DailyCheckProcedureAppService_newIdResponse, DailyCheckProcedureAppService_dailyCheckProceduresByProjectIdRequest,
    DailyCheckProcedureAppService_dailyCheckProceduresByProjectIdResponse,
)
from src.resource.proto._generated.project.daily_check_procedure_app_service_pb2_grpc import (
    DailyCheckProcedureAppServiceStub,
)


class DailyCheckProcedureClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                request = DailyCheckProcedureAppService_newIdRequest()
                response: DailyCheckProcedureAppService_newIdResponse = (
                    stub.new_id.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    DailyCheckProcedureClient.newId.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{DailyCheckProcedureClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedures(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> DailyCheckProcedures:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProcedures.__qualname__}] - grpc call to retrieve dailyCheckProcedures from server {self._server}:{self._port}"
                )
                request = DailyCheckProcedureAppService_dailyCheckProceduresRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: DailyCheckProcedureAppService_dailyCheckProceduresResponse = stub.daily_check_procedures.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                DailyCheckProcedureClient.dailyCheckProcedures.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProcedures.__qualname__}] - grpc response: {response}"
                )

                return DailyCheckProcedures(
                    daily_check_procedures=[
                        self._descriptorByObject(obj=dailyCheckProcedure)
                        for dailyCheckProcedure in response[0].daily_check_procedures
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProcedureById(self, id) -> DailyCheckProcedureDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProcedureById.__qualname__}] - grpc call to retrieve dailyCheckProcedure with dailyCheckProcedureId: {id} from server {self._server}:{self._port}"
                )
                response: DailyCheckProcedureAppService_dailyCheckProcedureByIdResponse = stub.daily_check_procedure_by_id.with_call(
                    DailyCheckProcedureAppService_dailyCheckProcedureByIdRequest(id=id),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                DailyCheckProcedureClient.dailyCheckProcedures.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProcedureById.__qualname__}] - grpc response: {response}"
                )
                dailyCheckProcedure = response[0].daily_check_procedure
                return self._descriptorByObject(obj=dailyCheckProcedure)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProceduresByEquipmentOrGroupId(
        self,
        equipmentOrGroupId: str = None,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> DailyCheckProcedures:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProceduresByEquipmentOrGroupId.__qualname__}] - grpc call to retrieve dailyCheckProcedures from server {self._server}:{self._port}"
                )
                request = DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentOrGroupIdRequest(
                    equipment_or_group_id=equipmentOrGroupId,
                    result_from=resultFrom,
                    result_size=resultSize,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: DailyCheckProcedureAppService_dailyCheckProceduresByEquipmentOrGroupIdResponse = stub.daily_check_procedures_by_equipment_or_group_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                DailyCheckProcedureClient.dailyCheckProceduresByEquipmentOrGroupId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProceduresByEquipmentOrGroupId.__qualname__}] - grpc response: {response}"
                )

                return DailyCheckProcedures(
                    daily_check_procedures=[
                        self._descriptorByObject(obj=dailyCheckProcedure)
                        for dailyCheckProcedure in response[0].daily_check_procedures
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def dailyCheckProceduresByProjectId(
            self,
            projectId: str = None,
            resultFrom: int = 0,
            resultSize: int = 10,
            orders: List[dict] = None,
    ) -> DailyCheckProcedures:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProceduresByProjectId.__qualname__}] - grpc call to {self._server}:{self._port}"
                )
                request = DailyCheckProcedureAppService_dailyCheckProceduresByProjectIdRequest(
                    project_id=projectId,
                    result_from=resultFrom,
                    result_size=resultSize,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: DailyCheckProcedureAppService_dailyCheckProceduresByProjectIdResponse = stub.daily_check_procedures_by_project_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                DailyCheckProcedureClient.dailyCheckProceduresByProjectId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{DailyCheckProcedureClient.dailyCheckProceduresByProjectId.__qualname__}] - grpc response: {response}"
                )

                return DailyCheckProcedures(
                    daily_check_procedures=[
                        self._descriptorByObject(obj=dailyCheckProcedure)
                        for dailyCheckProcedure in response[0].daily_check_procedures
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> DailyCheckProcedureDescriptor:
        return DailyCheckProcedureDescriptor(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            project_id=obj.project_id,
            equipment_id=obj.equipment_id,
            equipment_category_group_id=obj.equipment_category_group_id,
        )
