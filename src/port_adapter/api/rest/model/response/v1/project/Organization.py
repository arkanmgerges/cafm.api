"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class Organization(BaseModel):
    id: str
    name: str
    website_url: Optional[str]
    organization_type: Optional[str]
    address_one: Optional[str]
    address_two: Optional[str]
    postal_code: Optional[str]
    country_id: Optional[int]
    city_id: Optional[int]
    country_state_name: Optional[str]
    manager_first_name: Optional[str]
    manager_last_name: Optional[str]
    manager_email: Optional[str]
    manager_phone_number: Optional[str]
    manager_avatar: Optional[str]


class OrganizationDescriptor(Organization):
    pass
