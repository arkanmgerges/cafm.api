"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class CacheType(Enum):
    KEY = "0"
    LIST = "1"

    @staticmethod
    def valueToEnum(value: str):
        if value == "1":
            return CacheType.LIST
        return CacheType.KEY
