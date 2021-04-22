"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional, List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Role import Role
from src.port_adapter.api.rest.model.response.v1.project.User import User
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    Organization,
)


class UserLookup(BaseModel):
    user: User
    roles: List[Role]
    organizations: List[Organization]


class UserLookupDescriptor(UserLookup):
    pass
