"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Permission import (
    PermissionDescriptor,
)


class Permissions(BaseModel):
    permissions: List[PermissionDescriptor]
    total_item_count: int
