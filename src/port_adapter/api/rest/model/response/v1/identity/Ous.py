"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.Ou import OuDescriptor


class Ous(BaseModel):
    ous: List[OuDescriptor]
    total_item_count: int
