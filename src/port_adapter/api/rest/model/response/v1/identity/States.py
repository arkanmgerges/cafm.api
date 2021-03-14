"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.State import StateDescriptor


class States(BaseModel):
    states: List[StateDescriptor]
    item_count: int
