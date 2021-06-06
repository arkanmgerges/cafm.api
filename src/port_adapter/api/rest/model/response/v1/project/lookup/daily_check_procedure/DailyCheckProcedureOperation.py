"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperationParameter import \
    DailyCheckProcedureOperationParameterDescriptor


class DailyCheckProcedureOperation(BaseModel):
    id: str
    name: str
    description: str
    type: str
    daily_check_procedure_operation_parameters: List[DailyCheckProcedureOperationParameterDescriptor]

class DailyCheckProcedureOperationDescriptor(DailyCheckProcedureOperation):
    pass
