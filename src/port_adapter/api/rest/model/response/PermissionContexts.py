"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.PermissionContext import PermissionContext


class PermissionContexts(BaseModel):
    resource_types: List[PermissionContext]
    item_count: int