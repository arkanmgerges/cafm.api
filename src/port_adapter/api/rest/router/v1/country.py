"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import json
from typing import List
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.AuthenticationService import AuthenticationService
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.country.CountryClient import CountryClient
from src.port_adapter.api.rest.model.response.Country import CountryDescriptor
from src.port_adapter.api.rest.model.response.Countries import Countries
from src.port_adapter.api.rest.router.v1.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
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
        return client.Countries(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUsers.__module__}.{getUsers.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


# @router.get(path="/{country_id}/", summary='Get country',
#             response_model=CountryDescriptor)
# async def getCountry(*, country_id: str = Path(...,
#                                          description='Country id that is used to fetch country data'),
#                   _=Depends(CustomHttpBearer())):
#     """Get a User by id
#     """
#     try:
#         client = UserClient()
#         return client.userById(userId=user_id)
#     except grpc.RpcError as e:
#         if e.code() == StatusCode.PERMISSION_DENIED:
#             return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
#         if e.code() == StatusCode.NOT_FOUND:
#             return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
#         else:
#             logger.error(
#                 f'[{getUser.__module__}.{getUser.__qualname__}] - error response e: {e}')
#             return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
#     except Exception as e:
#         logger.info(e)
