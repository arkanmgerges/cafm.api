"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategoryDescriptor


class EquipmentProjectCategories(BaseModel):
    equipment_project_categories: List[EquipmentProjectCategoryDescriptor]
    item_count: int