"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class Role(BaseModel):
    id: str
    name: str
    title: str


class RoleDescriptor(Role):
    pass
