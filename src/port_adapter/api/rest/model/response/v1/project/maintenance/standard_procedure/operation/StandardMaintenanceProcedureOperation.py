"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class StandardMaintenanceProcedureOperation(BaseModel):
    id: str
    name: str
    description: str
    type: str
    standard_maintenance_procedure_id: str


class StandardMaintenanceProcedureOperationDescriptor(StandardMaintenanceProcedureOperation):
    pass
