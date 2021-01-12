"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from pydantic import BaseModel


class Project(BaseModel):
    id: str
    name: str
    city_id: int
    country_id: int
    address_line: str
    beneficiary_id: str
    state: str


class ProjectDescriptor(Project):
    pass
