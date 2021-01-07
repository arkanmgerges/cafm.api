"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from pydantic import BaseModel


class City(BaseModel):
    id: str
    geo_name_id: str
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    subdivision_one_iso_code: str
    subdivision_one_iso_name: str
    subdivision_two_iso_code: str
    subdivision_two_iso_name: str
    city_name: str
    metro_code: str
    time_zone: str
    is_in_european_union: bool


class CityDescriptor(BaseModel):
    id: str
    geo_name_id: str
    locale_code: str
    continent_code: str
    continent_name: str
    country_iso_code: str
    country_name: str
    subdivision_one_iso_code: str
    subdivision_one_iso_name: str
    subdivision_two_iso_code: str
    subdivision_two_iso_name: str
    city_name: str
    metro_code: str
    time_zone: str
    is_in_european_union: bool
