"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from pydantic import BaseModel


class Subcontractor(BaseModel):
    id: str
    company_name: str


class SubcontractorDescriptor(Subcontractor):
    pass
