"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    address_line_one: Optional[str]
    address_line_two: Optional[str]
    postal_code: Optional[str]
    avatar_image: Optional[str]


class UserDescriptor(BaseModel):
    id: str
    name: str
    first_name: Optional[str]
    last_name: Optional[str]
    address_line_one: Optional[str]
    address_line_two: Optional[str]
    postal_code: Optional[str]
    avatar_image: Optional[str]
