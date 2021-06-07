"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.Unit import UnitDescriptor


class DailyCheckProcedureOperationParameter(BaseModel):
    id: str
    name: str
    min_value: float
    max_value: float
    unit: UnitDescriptor

class DailyCheckProcedureOperationParameterDescriptor(DailyCheckProcedureOperationParameter):
    pass
