"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class Subcontractor(BaseModel):
    id: str
    company_name: str
    website_url: Optional[str]
    contact_person: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    address_one: Optional[str]
    address_two: Optional[str]


class SubcontractorDescriptor(Subcontractor):
    pass
