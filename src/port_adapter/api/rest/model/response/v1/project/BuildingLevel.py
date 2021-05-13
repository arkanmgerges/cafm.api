"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRoom import (
    BuildingLevelRoomDescriptor,
)


class BuildingLevel(BaseModel):
    id: str
    name: str
    is_subLevel: bool
    building_level_rooms: List[BuildingLevelRoomDescriptor]
    building_ids: List[str]


class BuildingLevelDescriptor(BuildingLevel):
    pass
