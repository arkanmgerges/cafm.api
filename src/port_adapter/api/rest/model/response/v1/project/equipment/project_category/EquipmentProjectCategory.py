"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class EquipmentProjectCategory(BaseModel):
    id: str
    name: str


class EquipmentProjectCategoryDescriptor(EquipmentProjectCategory):
    pass
