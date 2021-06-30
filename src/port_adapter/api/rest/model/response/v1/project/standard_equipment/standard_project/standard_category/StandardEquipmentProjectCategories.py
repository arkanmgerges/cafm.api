"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategory import (
    StandardEquipmentProjectCategoryDescriptor,
)


class StandardEquipmentProjectCategories(BaseModel):
    standard_equipment_project_categories: List[
        StandardEquipmentProjectCategoryDescriptor
    ]
    total_item_count: int
