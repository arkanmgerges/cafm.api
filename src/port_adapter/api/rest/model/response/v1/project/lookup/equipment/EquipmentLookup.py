"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentProjectCategory import EquipmentProjectCategoryDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentCategoryGroup import EquipmentCategoryGroupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.Building import BuildingDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.BuildingLevel import BuildingLevelDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.BuildingLevelRoom import BuildingLevelRoomDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.Manufacturer import ManufacturerDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentModel import EquipmentModelDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.MaintenanceProcedure import MaintenanceProcedureDescriptor


class EquipmentLookup(BaseModel):
    id: str
    name: str
    quantity: int
    project_id: str
    equipment_project_category: EquipmentProjectCategoryDescriptor
    equipment_category_group: EquipmentCategoryGroupDescriptor
    building: BuildingDescriptor
    building_level: BuildingLevelDescriptor
    building_level_room: BuildingLevelRoomDescriptor
    manufacturer: ManufacturerDescriptor
    equipment_model: EquipmentModelDescriptor
    maintenance_procedures: List[MaintenanceProcedureDescriptor]


class EquipmentLookupDescriptor(EquipmentLookup):
    pass
