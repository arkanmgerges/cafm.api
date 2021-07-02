"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureOperation import \
    DailyCheckProcedureOperationDescriptor
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.EquipmentCategoryGroup import \
    EquipmentCategoryGroupDescriptor


class DailyCheckProcedureLookup(BaseModel):
    id: str
    name: str
    description: str
    equipment_id: str
    project_id: str
    equipment_category_group: EquipmentCategoryGroupDescriptor
    daily_check_procedure_operations: List[DailyCheckProcedureOperationDescriptor]

class DailyCheckProcedureLookupDescriptor(DailyCheckProcedureLookup):
    pass
