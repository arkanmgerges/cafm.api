"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class DailyCheckProcedureOperationType(str, Enum):
    VISUAL = "visual"
    PARAMETER = "parameter"
