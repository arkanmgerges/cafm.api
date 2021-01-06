"""
@author: Mohammad S. moso<moso@develoop.run>
"""

import grpc
from fastapi import APIRouter, Depends, Query
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.v1.identity.country.CountryClient import CountryClient
from src.port_adapter.api.rest.model.response.v1.identity.Countries import Countries, CountryDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all countries', response_model=Countries)
async def getCountries(*,
                       result_from: int = Query(0, description='Starting offset for fetching data'),
                       result_size: int = Query(10, description='Item count to be fetched'),
                       order: str = Query('', description='e.g. name:asc,age:desc'),
                       _=Depends(CustomHttpBearer())):
    try:
        client = CountryClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.countries(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getCountries.__module__}.{getCountries.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{country_id}/", summary='Get country', response_model=CountryDescriptor)
async def getCountry(*, country_id: str = Path(..., description='Country id that is used to fetch country data'),
                     _=Depends(CustomHttpBearer())):
    """Get a Country by id
    """
    try:
        client = CountryClient()
        return client.countryById(countryId=country_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getCountry.__module__}.{getCountry.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
