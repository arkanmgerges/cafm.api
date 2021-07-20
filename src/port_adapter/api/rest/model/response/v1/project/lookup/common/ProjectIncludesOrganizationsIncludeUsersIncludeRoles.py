"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Optional

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.common.OrganizationIncludesUsersIncludeRoles import \
    OrganizationIncludesUsersIncludeRolesDescriptor


class ProjectIncludesOrganizationsIncludeUsersIncludeRoles(BaseModel):
    id: str = ''
    name: str = ''
    city_id: int = 0
    country_id: int = 0
    address_line: str = ''
    address_line_two: Optional[str]
    beneficiary_id: str = ''
    postal_code: Optional[str]
    country_state_name: Optional[str]
    country_state_iso_code: Optional[str]
    state: Optional[str]
    start_date: Optional[int]
    developer_name: Optional[str]
    developer_city_id: Optional[int]
    developer_country_id: Optional[int]
    developer_address_line_one: Optional[str]
    developer_address_line_two: Optional[str]
    developer_postal_code: Optional[str]
    developer_contact: Optional[str]
    developer_email: Optional[str]
    developer_phone_number: Optional[str]
    developer_warranty: Optional[str]
    developer_country_state_name: Optional[str]
    developer_country_state_iso_code: Optional[str]
    created_at: Optional[int]
    modified_at: Optional[int]
    organizations_include_users_include_roles: List[OrganizationIncludesUsersIncludeRolesDescriptor] = []


class ProjectIncludesOrganizationsIncludeUsersIncludeRolesDescriptor(ProjectIncludesOrganizationsIncludeUsersIncludeRoles):
    pass
