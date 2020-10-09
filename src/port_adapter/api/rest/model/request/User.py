"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    password: Optional[str]


class UserDescriptor(BaseModel):
    id: str
    name: str
