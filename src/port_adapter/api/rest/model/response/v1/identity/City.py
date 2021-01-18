"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from pydantic import BaseModel


class City(BaseModel):
    geoname_id: int
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    subdivision_1_iso_code: str
    subdivision_1_name: str
    city_name: str
    time_zone: str
    is_in_european_union: bool


class CityDescriptor(BaseModel):
    geoname_id: int
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    subdivision_1_iso_code: str
    subdivision_1_name: str
    city_name: str
    time_zone: str
    is_in_european_union: bool
