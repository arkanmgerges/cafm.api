"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from pydantic import BaseModel


class EquipmentModel(BaseModel):
    id: str
    name: str


class EquipmentModelDescriptor(EquipmentModel):
    pass