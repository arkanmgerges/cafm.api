"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Dict, List, TypedDict

from pydantic import BaseModel

class BulkBodyDataItemValue(BaseModel):
    data: dict

class BulkBodyData(BaseModel):
    data: List[Dict[str, BulkBodyDataItemValue]]
    class Config:
        schema_extra = {
            'example':
                {
                    'data': [
                        {"create_ou": {"data": {"name": "test_bulk_ou_2"}}},
                        {"create_manufacturer": {"data": {"name": "test_bulk_manufacturer_2"}}},
                        {"update_manufacturer": {"data": {"name": "test_bulk_manufacturer_2_update",
                                                          "manufacture_id": "8efb144b-0f07-4464-9c8a-ec194f2234d3"}}},
                        {"delete_manufacturer": {"data": {"manufacture_id": "3355144b-4564-4224-9467-abc94f23ad54"}}}
                    ]
                }
        }