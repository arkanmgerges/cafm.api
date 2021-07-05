"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Optional

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Project import ProjectDescriptor
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor
from src.port_adapter.api.rest.model.response.v1.project.role.Role import RoleDescriptor


class UserIncludesRoles(BaseModel):
    id: str = ''
    email: str = ''
    first_name: Optional[str]
    last_name: Optional[str]
    address_one: Optional[str]
    address_two: Optional[str]
    postal_code: Optional[str]
    phone_number: Optional[str]
    avatar_image: Optional[str]
    country_id: Optional[int]
    city_id: Optional[int]
    country_state_name: Optional[str]
    country_state_iso_code: Optional[str]
    start_date: Optional[int]
    roles: List[RoleDescriptor] = []


class UserIncludesRolesDescriptor(UserIncludesRoles):
    pass
