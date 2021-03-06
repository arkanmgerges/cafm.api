"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.user.UserLookup import (
    UserLookupDescriptor,
)


class UserLookups(BaseModel):
    user_lookups: List[UserLookupDescriptor]
    total_item_count: int
