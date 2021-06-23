"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.Building import (
    BuildingDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.BuildingLevel import (
    BuildingLevelDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.BuildingLevelRoom import (
    BuildingLevelRoomDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentCategoryGroup import (
    EquipmentCategoryGroupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentLookup import (
    EquipmentLookupDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentLookups import (
    EquipmentLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentModel import (
    EquipmentModelDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentProjectCategory import (
    EquipmentProjectCategoryDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.MaintenanceProcedure import (
    MaintenanceProcedureDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameterDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.Manufacturer import (
    ManufacturerDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.Unit import (
    UnitDescriptor,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.lookup.equipment.equipment_lookup_app_service_pb2 import (
    EquipmentLookupAppService_lookupRequest,
    EquipmentLookupAppService_lookupResponse,
)
from src.resource.proto._generated.project.lookup.equipment.equipment_lookup_app_service_pb2_grpc import (
    EquipmentLookupAppServiceStub,
)


class EquipmentLookupClient(Client):
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
    ) -> EquipmentLookups:
        orders = [] if orders is None else orders
        filters = [] if filters is None else filters
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = EquipmentLookupAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{EquipmentLookupClient.lookup.__qualname__}] - grpc call to retrieve lookups from server {self._server}:{self._port}"
                )
                request = EquipmentLookupAppService_lookupRequest(
                    result_from=resultFrom,
                    result_size=resultSize,
                    orders=orders,
                    filters=filters,
                )
                [
                    request.orders.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: EquipmentLookupAppService_lookupResponse = (
                    stub.lookup.with_call(
                        request,
                        metadata=(
                            ("token", self.token),
                            (
                                "opentel",
                                AppDi.instance.get(OpenTelemetry).serializedContext(
                                    EquipmentLookupClient.lookup.__qualname__
                                ),
                            ),
                        ),
                    )
                )
                logger.debug(
                    f"[{EquipmentLookupClient.lookup.__qualname__}] - grpc response: {response}"
                )

                return EquipmentLookups(
                    equipment_lookups=[
                        self._descriptorByObject(obj=obj)
                        for obj in response[0].equipments
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> EquipmentLookupDescriptor:
        maintenances = []
        for maintenance in obj.maintenance_procedures:
            operations = []
            for operation in maintenance.maintenance_procedure_operations:
                params = []
                for param in operation.maintenance_procedure_operation_parameters:
                    params.append(
                        MaintenanceProcedureOperationParameterDescriptor(
                            id=param.id,
                            name=param.name,
                            min_value=param.min_value,
                            max_value=param.max_value,
                            unit=UnitDescriptor(
                                id=param.unit.id,
                                name=param.unit.name,
                            ),
                        )
                    )
                operations.append(
                    MaintenanceProcedureOperationDescriptor(
                        id=operation.id,
                        name=operation.name,
                        description=operation.description,
                        type=operation.type,
                        maintenance_procedure_operation_parameters=params,
                    )
                )

            maintenances.append(
                MaintenanceProcedureDescriptor(
                    id=maintenance.id,
                    name=maintenance.name,
                    type=maintenance.type,
                    sub_type=maintenance.sub_type,
                    frequency=maintenance.frequency,
                    start_date=maintenance.start_date,
                    maintenance_procedure_operations=operations,
                )
            )

        return EquipmentLookupDescriptor(
            id=obj.id,
            name=obj.name,
            quantity=obj.quantity,
            project_id=obj.project_id,
            equipment_project_category=EquipmentProjectCategoryDescriptor(
                id=obj.equipment_project_category.id,
                name=obj.equipment_project_category.name,
            ),
            equipment_category_group=EquipmentCategoryGroupDescriptor(
                id=obj.equipment_category_group.id,
                name=obj.equipment_category_group.name,
            ),
            building=BuildingDescriptor(id=obj.building.id, name=obj.building.name),
            building_level=BuildingLevelDescriptor(
                id=obj.building_level.id,
                name=obj.building_level.name,
                is_sub_level=obj.building_level.is_sub_level,
            ),
            building_level_room=BuildingLevelRoomDescriptor(
                id=obj.building_level_room.id,
                name=obj.building_level_room.name,
                description=obj.building_level_room.description,
            ),
            manufacturer=ManufacturerDescriptor(
                id=obj.manufacturer.id,
                name=obj.manufacturer.name,
            ),
            equipment_model=EquipmentModelDescriptor(
                id=obj.equipment_model.id,
                name=obj.equipment_model.name,
            ),
            maintenance_procedures=maintenances,
        )
