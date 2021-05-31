"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.City import CityDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.Country import CountryDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.State import StateDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.SubcontractorCategory import \
    SubcontractorCategoryDescriptor


class SubcontractorLookup(BaseModel):
    id: str
    company_name: str
    website_url: str
    contact_person: str
    email: str
    phone_number: str
    address_one: str
    address_two: str
    description: str
    postal_code: str
    subcontractor_category: SubcontractorCategoryDescriptor
    country: CountryDescriptor
    state: StateDescriptor
    city: CityDescriptor


class SubcontractorLookupDescriptor(SubcontractorLookup):
    pass
