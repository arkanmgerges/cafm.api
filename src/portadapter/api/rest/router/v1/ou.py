"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import traceback
from logging import Logger
from typing import List
from src.resource.logging.logger import logger

from fastapi import APIRouter, Depends, Query, Body
from starlette import status

import src.portadapter.api.rest.AppDi as AppDi
from src.portadapter.api.rest.model.request.OrganizationalUnit import OrganizationalUnit
from src.portadapter.api.rest.router.v1.auth import CustomHttpBearer

router = APIRouter()


@router.get(path="/", summary='Get all organizational units', response_model=List[OrganizationalUnit])
async def getAllOrganizationalUnits(*, _=Depends(CustomHttpBearer())):
    """Return all organizational units
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{ouId}/", summary='Get organizational unit',
            response_model=OrganizationalUnit)
async def getOu(*, ouId: str = Query(...,
                                     description='ou id that is used to fetch organizational unit data'),
                _=Depends(CustomHttpBearer())):
    """Get a OrganizationalUnit by id
    """
    try:
        return OrganizationalUnit()
    except:
        logger.warning(traceback.format_exc())
        return OrganizationalUnit()


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new organizational unit', status_code=status.HTTP_204_NO_CONTENT)
async def create(*, _=Depends(CustomHttpBearer()),
                 title: str = Body(..., description='Title of the organizational unit',
                                   )):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)
