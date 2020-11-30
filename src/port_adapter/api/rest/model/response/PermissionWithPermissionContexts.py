"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Permission import Permission
from src.port_adapter.api.rest.model.response.PermissionContext import PermissionContext


class PermissionWithPermissionContexts(BaseModel):
    permission: Permission
    permission_contexts: List[PermissionContext]
