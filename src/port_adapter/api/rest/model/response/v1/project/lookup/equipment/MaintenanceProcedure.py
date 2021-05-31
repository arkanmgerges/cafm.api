"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional, List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.MaintenanceProcedureOperation import \
    MaintenanceProcedureOperation


class MaintenanceProcedure(BaseModel):
    id: str
    name: str
    type: str
    sub_type: Optional[str]
    frequency: str
    start_date: int
    maintenance_procedure_operations: Optional[List[MaintenanceProcedureOperation]]


class MaintenanceProcedureDescriptor(MaintenanceProcedure):
    pass
