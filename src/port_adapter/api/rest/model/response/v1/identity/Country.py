"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import Optional

from pydantic import BaseModel


class Country(BaseModel):
    geoname_id: int
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    is_in_european_union: bool


class CountryDescriptor(BaseModel):
    geoname_id: int
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    is_in_european_union: bool
