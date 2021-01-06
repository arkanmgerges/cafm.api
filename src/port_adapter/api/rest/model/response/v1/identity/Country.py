"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import Optional

from pydantic import BaseModel


class Country(BaseModel):
    id: str
    geo_name_id: str
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    is_in_european_union: bool


class CountryDescriptor(BaseModel):
    id: str
    geo_name_id: str
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    is_in_european_union: bool
