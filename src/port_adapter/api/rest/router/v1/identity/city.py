"""
@author: Mohammad S. moso<moso@develoop.run>
"""

import grpc
from fastapi import APIRouter, Depends, Query
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.v1.identity.city.CityClient import CityClient
from src.port_adapter.api.rest.model.response.v1.identity.Cities import (
    Cities,
    CityDescriptor,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary="Get all cities", response_model=Cities)
@OpenTelemetry.fastApiTraceOTel
async def getCities(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
):
    """
    Get list of cities
    """
    try:
        client = CityClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.cities(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getCities.__module__}.{getCities.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{city_id}", summary="Get city", response_model=CityDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getCity(
    *,
    city_id: int = Path(..., description="City id that is used to fetch city data"),
    _=Depends(CustomHttpBearer()),
):
    """
    Get a City by id
    """
    try:
        client = CityClient()
        return client.cityById(cityId=city_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getCity.__module__}.{getCity.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

