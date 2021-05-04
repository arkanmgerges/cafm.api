"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroupDescriptor,
)


class StandardEquipmentCategoryGroups(BaseModel):
    standard_equipment_category_groups: List[StandardEquipmentCategoryGroupDescriptor]
    total_item_count: int
