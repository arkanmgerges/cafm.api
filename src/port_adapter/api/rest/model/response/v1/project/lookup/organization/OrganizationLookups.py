"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.organization.OrganizationLookup import OrganizationLookupDescriptor


class OrganizationLookups(BaseModel):
    organization_lookups: List[OrganizationLookupDescriptor]
    total_item_count: int
