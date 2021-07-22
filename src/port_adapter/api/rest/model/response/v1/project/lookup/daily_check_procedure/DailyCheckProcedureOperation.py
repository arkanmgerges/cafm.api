"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperationParameter import \
    DailyCheckProcedureOperationParameterDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperationLabel import \
    DailyCheckProcedureOperationLabelDescriptor

class DailyCheckProcedureOperation(BaseModel):
    id: str
    name: str
    description: str
    type: str
    daily_check_procedure_operation_parameters: List[DailyCheckProcedureOperationParameterDescriptor]
    daily_check_procedure_operation_labels: List[DailyCheckProcedureOperationLabelDescriptor]

class DailyCheckProcedureOperationDescriptor(DailyCheckProcedureOperation):
    pass
