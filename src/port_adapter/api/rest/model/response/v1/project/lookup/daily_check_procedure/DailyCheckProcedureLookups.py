"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureLookup import \
    DailyCheckProcedureLookupDescriptor


class DailyCheckProcedureLookups(BaseModel):
    daily_check_procedure_lookups: List[DailyCheckProcedureLookupDescriptor]
    total_item_count: int
