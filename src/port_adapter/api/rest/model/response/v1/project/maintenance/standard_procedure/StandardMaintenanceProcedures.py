"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedure import (
    StandardMaintenanceProcedureDescriptor,
)


class StandardMaintenanceProcedures(BaseModel):
    standard_maintenance_procedures: List[StandardMaintenanceProcedureDescriptor]
    total_item_count: int
