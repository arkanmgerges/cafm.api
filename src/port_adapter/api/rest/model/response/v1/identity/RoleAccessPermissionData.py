"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.AccessNode import AccessNode
from src.port_adapter.api.rest.model.response.v1.identity.PermissionWithPermissionContexts import (
    PermissionWithPermissionContexts,
)
from src.port_adapter.api.rest.model.response.v1.identity.Resource import Resource
from src.port_adapter.api.rest.model.response.v1.identity.Role import Role


class RoleAccessPermissionData(BaseModel):
    role: Role
    permissions: List[PermissionWithPermissionContexts]
    owned_by: Resource
    owner_of: List[Resource]
    access_tree: List[AccessNode]


class RoleAccessPermissionDataDescriptor(RoleAccessPermissionData):
    pass
