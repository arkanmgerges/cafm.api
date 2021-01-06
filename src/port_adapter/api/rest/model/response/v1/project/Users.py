"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.User import UserDescriptor


class Users(BaseModel):
    users: List[UserDescriptor]
    item_count: int
