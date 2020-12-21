"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.Country import CountryDescriptor


class Countries(BaseModel):
    countries: List[CountryDescriptor]
    item_count: int
