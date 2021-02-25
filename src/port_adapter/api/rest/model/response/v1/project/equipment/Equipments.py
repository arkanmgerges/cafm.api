"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.equipment.Equipment import EquipmentDescriptor


class Equipments(BaseModel):
    equipments: List[EquipmentDescriptor]
    item_count: int
