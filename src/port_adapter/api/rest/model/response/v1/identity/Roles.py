"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Role import Role


class Roles(BaseModel):
    roles: List[Role]
    item_count: int

