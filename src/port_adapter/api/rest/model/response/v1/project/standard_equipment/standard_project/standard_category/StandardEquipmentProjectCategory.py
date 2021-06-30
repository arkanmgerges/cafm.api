"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class StandardEquipmentProjectCategory(BaseModel):
    id: str
    name: str
    organization_id: str


class StandardEquipmentProjectCategoryDescriptor(StandardEquipmentProjectCategory):
    pass
