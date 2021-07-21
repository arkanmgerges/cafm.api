"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class DailyCheckProcedureOperationLabel(BaseModel):
    id: str
    label: str
    generate_alert: int

class DailyCheckProcedureOperationLabelDescriptor(DailyCheckProcedureOperationLabel):
    pass
