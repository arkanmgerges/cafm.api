"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.UserGroup import UserGroup


class UserGroups(BaseModel):
    userGroups: List[UserGroup]
    itemCount: int
