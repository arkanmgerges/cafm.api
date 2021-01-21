"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc
from fastapi import APIRouter, Depends, Query
from fastapi import Response
from grpc.beta.interfaces import StatusCode
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.v1.project.lookup.user.UserLookupClient import UserLookupClient
from src.port_adapter.api.rest.model.response.v1.project.UserLookups import UserLookups
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="user_lookups", summary='Get users with other related data', response_model=UserLookups)
@OpenTelemetry.fastApiTraceOTel
async def getUserLookups(*,
                         result_from: int = Query(0, description='Starting offset for fetching data'),
                         result_size: int = Query(10, description='Item count to be fetched'),
                         order: str = Query('',
                                            description='e.g. user.id:asc,user.email:desc,role.name:asc,organization.name:desc'),
                         _=Depends(CustomHttpBearer())):
    try:
        client = UserLookupClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.userLookups(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getUserLookups.__module__}.{getUserLookups.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)
