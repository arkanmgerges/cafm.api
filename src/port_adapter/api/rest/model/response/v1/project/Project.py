"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Optional

from pydantic import BaseModel


class Project(BaseModel):
    id: str
    name: str
    city_id: int
    country_id: int
    address_line: str
    address_line_two: Optional[str]
    beneficiary_id: str
    state: str
    start_date: Optional[str]
    developerName: Optional[str]
    developerCityId: Optional[int]
    developerCountryId: Optional[int]
    developerAddressLineOne: Optional[str]
    developerAddressLineTwo: Optional[str]
    developerContact: Optional[str]
    developerEmail: Optional[str]
    developerPhoneNumber: Optional[str]
    developerWarranty: Optional[str]


class ProjectDescriptor(Project):
    pass
