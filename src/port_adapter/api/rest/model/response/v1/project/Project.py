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
    postal_code: Optional[str]
    state: Optional[str]
    start_date: Optional[int]
    developer_name: Optional[str]
    developer_city_id: Optional[int]
    developer_country_id: Optional[int]
    developer_address_line_one: Optional[str]
    developer_address_line_two: Optional[str]
    developer_postal_code: Optional[str]
    developer_contact: Optional[str]
    developer_email: Optional[str]
    developer_phone_number: Optional[str]
    developer_warranty: Optional[str]


class ProjectDescriptor(Project):
    pass
