"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.project.ProjectLookup import ProjectLookupDescriptor


class ProjectLookups(BaseModel):
    project_lookups: List[ProjectLookupDescriptor]
    total_item_count: int
