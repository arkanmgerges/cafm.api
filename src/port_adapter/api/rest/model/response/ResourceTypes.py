"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.ResourceType import ResourceType


class ResourceTypes(BaseModel):
    resourceTypes: List[ResourceType]
    item_count: int
