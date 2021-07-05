"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.common.OrganizationIncludesUsersIncludeRoles import \
    OrganizationIncludesUsersIncludeRolesDescriptor


class OrganizationsIncludeUsersIncludeRoles(BaseModel):
    organizations_include_users_include_roles: List[OrganizationIncludesUsersIncludeRolesDescriptor]
    total_item_count: int
