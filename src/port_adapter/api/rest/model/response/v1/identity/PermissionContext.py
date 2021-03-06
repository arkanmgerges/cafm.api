"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class PermissionContext(BaseModel):
    id: str
    type: str
    data: dict


class PermissionContextDescriptor(PermissionContext):
    pass
