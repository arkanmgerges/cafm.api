"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.OrganizationLocation import OrganizationLocationDescriptor
from typing import List, Optional

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.common.UserIncludesRoles import \
    UserIncludesRolesDescriptor
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor


class OrganizationIncludesUsersIncludeRoles(BaseModel):
    id: str = ''
    name: str = ''
    website_url: Optional[str]
    organization_type: Optional[str]
    address_one: Optional[str]
    address_two: Optional[str]
    postal_code: Optional[str]
    country_id: Optional[int]
    city_id: Optional[int]
    country_state_name: Optional[str]
    country_state_iso_code: Optional[str]
    manager_first_name: Optional[str]
    manager_last_name: Optional[str]
    manager_email: Optional[str]
    manager_phone_number: Optional[str]
    manager_avatar: Optional[str]
    users_include_roles: List[UserIncludesRolesDescriptor] = []
    locations: List[OrganizationLocationDescriptor] = []



class OrganizationIncludesUsersIncludeRolesDescriptor(OrganizationIncludesUsersIncludeRoles):
    pass
