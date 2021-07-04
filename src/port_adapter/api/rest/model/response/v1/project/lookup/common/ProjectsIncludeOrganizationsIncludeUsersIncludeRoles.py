"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.common.ProjectIncludesOrganizationsIncludeUsersIncludeRoles import \
    ProjectIncludesOrganizationsIncludeUsersIncludeRolesDescriptor


class ProjectsIncludeOrganizationsIncludeUsersIncludeRoles(BaseModel):
    projects_include_organizations_include_users_include_roles: List[ProjectIncludesOrganizationsIncludeUsersIncludeRolesDescriptor] = []
    total_item_count: int
