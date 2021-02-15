"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.BuildingLevel import BuildingLevelDescriptor


class Building(BaseModel):
    id: str
    name: str
    project_id: str
    building_levels: List[BuildingLevelDescriptor]


class BuildingDescriptor(Building):
    pass
