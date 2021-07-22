"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class ProjectStatistic(BaseModel):
    project_id: str
    project_name: str
    project_created_at: int
    project_modified_at: int
    building_count: int
    equipment_count: int
    maintenance_procedure_count: int

class ProjectStatisticDescriptor(ProjectStatistic):
    pass
