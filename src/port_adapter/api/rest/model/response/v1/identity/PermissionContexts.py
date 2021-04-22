"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.PermissionContext import (
    PermissionContextDescriptor,
)


class PermissionContexts(BaseModel):
    permission_contexts: List[PermissionContextDescriptor]
    item_count: int
