"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.identity.City import CityDescriptor


class Cities(BaseModel):
    cities: List[CityDescriptor]
    item_count: int
