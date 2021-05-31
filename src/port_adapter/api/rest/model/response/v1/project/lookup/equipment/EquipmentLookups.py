"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentLookup import EquipmentLookupDescriptor


class EquipmentLookups(BaseModel):
    equipment_lookups: List[EquipmentLookupDescriptor]
    total_item_count: int
