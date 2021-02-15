"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Building import BuildingDescriptor


class Buildings(BaseModel):
    buildings: List[BuildingDescriptor]
    item_count: int
