"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class Building(BaseModel):
    id: str
    name: str


class BuildingDescriptor(Building):
    pass
