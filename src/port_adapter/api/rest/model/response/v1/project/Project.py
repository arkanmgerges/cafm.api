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
    beneficiary_id: str
    state: str
    start_date: Optional[str]


class ProjectDescriptor(Project):
    pass
