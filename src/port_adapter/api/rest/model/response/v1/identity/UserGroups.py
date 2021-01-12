"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.UserGroup import UserGroupDescriptor


class UserGroups(BaseModel):
    user_groups: List[UserGroupDescriptor]
    item_count: int
