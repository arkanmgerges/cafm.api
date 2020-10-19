"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Project import Project


class Projects(BaseModel):
    projects: List[Project]
    item_count: int
