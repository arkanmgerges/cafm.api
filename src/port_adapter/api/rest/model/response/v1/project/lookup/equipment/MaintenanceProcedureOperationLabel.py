"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from pydantic import BaseModel


class MaintenanceProcedureOperationLabel(BaseModel):
    id: str
    label: str
    generate_alert: int


class MaintenanceProcedureOperationLabelDescriptor(
    MaintenanceProcedureOperationLabel
):
    pass