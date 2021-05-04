"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.subcontractor.Subcontractor import (
    SubcontractorDescriptor,
)


class Subcontractors(BaseModel):
    subcontractors: List[SubcontractorDescriptor]
    total_item_count: int
