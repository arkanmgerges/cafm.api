"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.BuildingLevel import (
    BuildingLevelDescriptor,
)


class BuildingLevels(BaseModel):
    building_levels: List[BuildingLevelDescriptor]
    total_item_count: int
