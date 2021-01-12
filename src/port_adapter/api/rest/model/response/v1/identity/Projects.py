"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Project import ProjectDescriptor


class Projects(BaseModel):
    projects: List[ProjectDescriptor]
    item_count: int
