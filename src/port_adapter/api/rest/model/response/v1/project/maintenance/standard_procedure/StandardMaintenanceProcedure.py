"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class StandardMaintenanceProcedure(BaseModel):
    id: str
    name: str
    type: str
    subtype: str
    frequency: str
    start_date: int
    organization_id: str
    standard_equipment_category_group_id: str


class StandardMaintenanceProcedureDescriptor(StandardMaintenanceProcedure):
    pass
