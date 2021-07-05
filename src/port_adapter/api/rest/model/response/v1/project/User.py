"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    address_one: Optional[str]
    address_two: Optional[str]
    postal_code: Optional[str]
    phone_number: Optional[str]
    avatar_image: Optional[str]
    country_id: Optional[int] = 0
    city_id: Optional[int] = 0
    country_state_name: Optional[str]
    country_state_iso_code: Optional[str]
    start_date: Optional[int] = 0


class UserDescriptor(User):
    pass
