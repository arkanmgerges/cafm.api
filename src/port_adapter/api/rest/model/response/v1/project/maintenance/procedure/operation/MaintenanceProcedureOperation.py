"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class MaintenanceProcedureOperation(BaseModel):
    id: str
    name: str
    description: str
    type: str
    maintenance_procedure_id: str


class MaintenanceProcedureOperationDescriptor(MaintenanceProcedureOperation):
    pass