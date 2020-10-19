"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Permission import Permission


class Permissions(BaseModel):
    permissions: List[Permission]
    item_count: int
