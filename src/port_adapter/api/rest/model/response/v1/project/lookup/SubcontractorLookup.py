"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.CityLookup import CityLookupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.CountryLookup import CountryLookupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.StateLookup import StateLookupDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.SubcontractorCategoryLookup import \
    SubcontractorCategoryLookupDescriptor


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
    subcontractor_category: SubcontractorCategoryLookupDescriptor
    country: CountryLookupDescriptor
    state: StateLookupDescriptor
    city: CityLookupDescriptor


class SubcontractorLookupDescriptor(SubcontractorLookup):
    pass
