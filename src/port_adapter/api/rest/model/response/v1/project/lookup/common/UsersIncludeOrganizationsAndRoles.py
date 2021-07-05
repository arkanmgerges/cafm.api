"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.common.UserIncludesOrganizationsAndRoles import \
    UserIncludesOrganizationsAndRoles


class UsersIncludeOrganizationsAndRoles(BaseModel):
    users_include_organizations_and_roles: List[UserIncludesOrganizationsAndRoles]
    total_item_count: int
