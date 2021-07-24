"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import hashlib
import os
import shutil
from tempfile import SpooledTemporaryFile
from typing import List

from fastapi import APIRouter, Depends
from fastapi import File, UploadFile

from src.domain_model.token.TokenData import TokenData
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.media.UploadedFile import UploadedFile
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.post(path="/upload_file", summary="Upload file", response_model=UploadedFile)
@OpenTelemetry.fastApiTraceOTel
async def uploadFile(
    *,
    uploadedFile: UploadFile = File(...),
    _=Depends(CustomHttpBearer()),
):
    """
    Upload file
    """
    token = Client.token
    tokenData: TokenData = TokenService.tokenDataFromToken(token)
    newFileName = hashlib.sha256(uploadedFile.filename.encode()).hexdigest()
    await _saveUploadedFileIntoNewLocation(tokenData=tokenData, newFileName=newFileName, uploadedFile=uploadedFile)

    return UploadedFile(filename=uploadedFile.filename, filepath=f"path: {tokenData.id()}/{newFileName}")


@router.post(path="/upload_files", summary="Upload files", response_model=List[UploadedFile])
@OpenTelemetry.fastApiTraceOTel
async def uploadFiles(
    *,
    uploadedFiles: List[UploadFile] = File(...),
    _=Depends(CustomHttpBearer()),
):
    """
    Upload files
    """
    token = Client.token
    tokenData: TokenData = TokenService.tokenDataFromToken(token)
    result: List[UploadedFile] = []
    for uploadedFile in uploadedFiles:
        newFileName = hashlib.sha256(uploadedFile.filename.encode()).hexdigest()
        await _saveUploadedFileIntoNewLocation(tokenData=tokenData, newFileName=newFileName, uploadedFile=uploadedFile)

        result.append(UploadedFile(filename=uploadedFile.filename, filepath=f"path: {tokenData.id()}/{newFileName}"))
    return result

def _createDir(path: str):
    os.makedirs(path, exist_ok=True)

async def _saveUploadedFileIntoNewLocation(tokenData: TokenData = None, newFileName: str = None, uploadedFile: File = None):
    newFilePath = f"{tokenData.id()}/{newFileName}"
    mediaDataPath = os.getenv('MEDIA_DATA_PATH', '/media_data')
    _createDir(f"{mediaDataPath}/{tokenData.id()}")

    content = await uploadedFile.read()
    await uploadedFile.close()
    with open(f"{mediaDataPath}/{newFilePath}", "wb+") as file:
        file.write(content)
