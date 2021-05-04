"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Route import RouteDescriptor


class Routes(BaseModel):
    routes: List[RouteDescriptor]
    total_item_count: int
