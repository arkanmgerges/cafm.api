"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureLookup import \
    DailyCheckProcedureLookupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureLookups import \
    DailyCheckProcedureLookups
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperation import \
    DailyCheckProcedureOperationDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperationParameter import \
    DailyCheckProcedureOperationParameterDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.EquipmentCategoryGroup import \
    EquipmentCategoryGroupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.Unit import UnitDescriptor
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2 import \
    DailyCheckProcedureLookupAppService_lookupRequest, DailyCheckProcedureLookupAppService_lookupResponse
from src.resource.proto._generated.project.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2_grpc import \
    DailyCheckProcedureLookupAppServiceStub


class DailyCheckProcedureLookupClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def lookup(
        self,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
        filters: List[dict] = None,
    ) -> DailyCheckProcedureLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = DailyCheckProcedureLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{DailyCheckProcedureLookupClient.lookup.__qualname__}] - grpc call to retrieve lookups from server {self._server}:{self._port}"
                )
                request = DailyCheckProcedureLookupAppService_lookupRequest(
                    result_from=resultFrom, result_size=resultSize, orders=orders, filters=filters
                )
                [request.orders.add(orderBy=o["orderBy"], direction=o["direction"]) for o in orders]
                response: DailyCheckProcedureLookupAppService_lookupResponse = stub.lookup.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                DailyCheckProcedureLookupClient.lookup.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(f"[{DailyCheckProcedureLookupClient.lookup.__qualname__}] - grpc response: {response}")

                return DailyCheckProcedureLookups(
                    daily_check_procedure_lookups=[
                        self._descriptorByObject(obj=obj) for obj in response[0].daily_check_procedures
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> DailyCheckProcedureLookupDescriptor:
        operations = []
        for operation in obj.daily_check_procedure_operations:
                params = []
                for param in operation.daily_check_procedure_operation_parameters:
                    params.append(
                        DailyCheckProcedureOperationParameterDescriptor(
                            id=param.id,
                            name=param.name,
                            min_value=param.min_value,
                            max_value=param.max_value,
                            unit=UnitDescriptor(
                                id=param.unit.id,
                                name=param.unit.name,
                            )
                        )
                    )
                operations.append(
                    DailyCheckProcedureOperationDescriptor(
                        id=operation.id,
                        name=operation.name,
                        description=operation.description,
                        type=operation.type,
                        daily_check_procedure_operation_parameters=params,
                    )
                )


        return DailyCheckProcedureLookupDescriptor(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            equipment_id=obj.equipment_id,
            project_id=obj.project_id,
            equipment_category_group=EquipmentCategoryGroupDescriptor(
                id=obj.equipment_category_group.id,
                name=obj.equipment_category_group.name,
            ),
            daily_check_procedure_operations=operations
        )
