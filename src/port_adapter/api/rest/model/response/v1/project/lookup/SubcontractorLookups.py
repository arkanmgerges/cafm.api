"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.SubcontractorLookup import SubcontractorLookupDescriptor


class SubcontractorLookups(BaseModel):
    subcontractor_lookups: List[SubcontractorLookupDescriptor]
    total_item_count: int
