"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from pydantic import BaseModel


class UploadedFile(BaseModel):
    filename: str
    filepath: str

class UploadedFileDescriptor(UploadedFile):
    pass
