"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class MaintenanceProcedure(BaseModel):
    id: str
    name: str
    type: str
    sub_type: Optional[str]
    frequency: str
    start_date: int
    subcontractor_id: str
    equipment_id: str


class MaintenanceProcedureDescriptor(MaintenanceProcedure):
    pass
