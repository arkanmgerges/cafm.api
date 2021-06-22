"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor


class OrganizationLookup(BaseModel):
    users: List[UserDescriptor]
    roles: List[RoleDescriptor]
    organization: OrganizationDescriptor
    projects: List[ProjectDescriptor]


class OrganizationLookupDescriptor(OrganizationLookup):
    pass
