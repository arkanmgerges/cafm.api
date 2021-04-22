"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperationDescriptor,
)


class MaintenanceProcedureOperations(BaseModel):
    maintenance_procedure_operations: List[MaintenanceProcedureOperationDescriptor]
    item_count: int
