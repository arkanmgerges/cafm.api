"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import Optional

from pydantic import BaseModel


class DailyCheckProcedureOperation(BaseModel):
    id: str
    name: str
    description: str
    type: str
    daily_check_procedure_id: str


class DailyCheckProcedureOperationDescriptor(DailyCheckProcedureOperation):
    pass
