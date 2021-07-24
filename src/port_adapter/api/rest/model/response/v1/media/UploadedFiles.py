"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from pydantic import BaseModel

from src.port_adapter.api.rest.model.response.v1.media.UploadedFile import UploadedFileDescriptor


class Users(BaseModel):
    uploaded_files: List[UploadedFileDescriptor]
    total_item_count: int
