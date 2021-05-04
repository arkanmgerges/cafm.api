"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel


from src.port_adapter.api.rest.model.response.v1.project.BuildingLevelRoom import (
    BuildingLevelRoomDescriptor,
)


class BuildingLevelRooms(BaseModel):
    building_level_rooms: List[BuildingLevelRoomDescriptor]
    total_item_count: int
