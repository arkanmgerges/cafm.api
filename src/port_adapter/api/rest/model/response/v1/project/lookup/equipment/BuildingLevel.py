"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class BuildingLevel(BaseModel):
    id: str
    name: str
    is_sub_level: bool


class BuildingLevelDescriptor(BuildingLevel):
    pass
