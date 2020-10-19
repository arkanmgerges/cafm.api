"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel


class Permission(BaseModel):
    id: str
    name: str
    allowed_actions: List[str]

