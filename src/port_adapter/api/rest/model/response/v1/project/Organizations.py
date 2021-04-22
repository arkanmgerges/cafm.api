"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)


class Organizations(BaseModel):
    organizations: List[OrganizationDescriptor]
    item_count: int
