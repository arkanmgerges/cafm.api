"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class SubcontractorCategoryLookup(BaseModel):
    id: str
    name: str

class SubcontractorCategoryLookupDescriptor(SubcontractorCategoryLookup):
    pass
