"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class DailyCheckProcedureOperationLabel(BaseModel):
    id: str
    label: str
    generate_alert: int
    daily_check_procedure_operation_id: str


class DailyCheckProcedureOperationLabelDescriptor(DailyCheckProcedureOperationLabel):
    pass
