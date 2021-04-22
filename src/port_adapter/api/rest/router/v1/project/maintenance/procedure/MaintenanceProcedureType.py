"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class MaintenanceProcedureType(str, Enum):
    HARD = "hard"
    SOFT = "soft"
