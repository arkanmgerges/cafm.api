"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc
from fastapi import APIRouter, Depends, Query
from fastapi import Response
from grpc.beta.interfaces import StatusCode
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)

import src.port_adapter.AppDi as AppDi
from src.domain_model.FilterService import FilterService
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.v1.project.lookup.daily_check_procedure.DailyCheckProcedureLookupClient import (
    DailyCheckProcedureLookupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.lookup.equipment.EquipmentLookupClient import (
    EquipmentLookupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.lookup.organization.OrganizationLookupClient import (
    OrganizationLookupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.lookup.project.ProjectLookupClient import (
    ProjectLookupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.lookup.subcontractor.SubcontractorLookupClient import (
    SubcontractorLookupClient,
)
from src.port_adapter.api.rest.grpc.v1.project.lookup.user.UserLookupClient import (
    UserLookupClient,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.organization.OrganizationLookups import (
    OrganizationLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.project.ProjectLookups import (
    ProjectLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.user.UserLookups import (
    UserLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.daily_check_procedure.DailyCheckProcedureLookups import (
    DailyCheckProcedureLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.equipment.EquipmentLookups import (
    EquipmentLookups,
)
from src.port_adapter.api.rest.model.response.v1.project.lookup.subcontractor.SubcontractorLookups import (
    SubcontractorLookups,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="/daily_check_procedures",
    summary="Get daily check procedures with related data",
    response_model=DailyCheckProcedureLookups,
)
@OpenTelemetry.fastApiTraceOTel
async def getDailyCheckProcedureLookups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query(
        "",
        description="e.g. phone_number:asc,country.id:desc",
    ),
    filters: str = Query("", description="e.g. _all:*abcd*,phone_number:*33453*"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = DailyCheckProcedureLookupClient()
        orderService = AppDi.instance.get(OrderService)
        filterService = AppDi.instance.get(FilterService)
        orders = orderService.orderStringToListOfDict(orders)
        filters = filterService.filterStringToListOfDict(filters)
        return client.lookup(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            filters=filters,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUserLookups.__module__}.{getUserLookups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/equipments",
    summary="Get equipments with related data",
    response_model=EquipmentLookups,
)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentLookups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query(
        "",
        description="e.g. phone_number:asc,country.id:desc",
    ),
    filters: str = Query("", description="e.g. _all:*abcd*,phone_number:*33453*"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = EquipmentLookupClient()
        orderService = AppDi.instance.get(OrderService)
        filterService = AppDi.instance.get(FilterService)
        orders = orderService.orderStringToListOfDict(orders)
        filters = filterService.filterStringToListOfDict(filters)
        return client.lookup(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            filters=filters,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getEquipmentLookups.__module__}.{getEquipmentLookups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/subcontractors",
    summary="Get subcontractors with related data",
    response_model=SubcontractorLookups,
)
@OpenTelemetry.fastApiTraceOTel
async def getSubcontractorLookups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query(
        "",
        description="e.g. phone_number:asc,country.id:desc",
    ),
    filters: str = Query("", description="e.g. _all:*abcd*,phone_number:*33453*"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = SubcontractorLookupClient()
        orderService = AppDi.instance.get(OrderService)
        filterService = AppDi.instance.get(FilterService)
        orders = orderService.orderStringToListOfDict(orders)
        filters = filterService.filterStringToListOfDict(filters)
        return client.lookup(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            filters=filters,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getUserLookups.__module__}.{getUserLookups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


# @router.get(
#     path="/users",
#     summary="Get users with other related data",
#     response_model=UserLookups,
# )
# @OpenTelemetry.fastApiTraceOTel
# async def getUserLookups(
#     *,
#     result_from: int = Query(0, description="Starting offset for fetching data"),
#     result_size: int = Query(10, description="Item count to be fetched"),
#     orders: str = Query(
#         "",
#         description="e.g. user.id:asc,user.email:desc,role.name:asc,organization.name:desc",
#     ),
#     filters: str = Query("", description="e.g. column_name:column_value"),
#     _=Depends(CustomHttpBearer()),
#     __=Depends(CustomAuthorization()),
# ):
#     try:
#         client = UserLookupClient()
#         orderService = AppDi.instance.get(OrderService)
#         filterService = AppDi.instance.get(FilterService)
#         orders = orderService.orderStringToListOfDict(orders)
#         filters = filterService.filterStringToListOfDict(filters)
#
#         return client.userLookups(
#             resultFrom=result_from,
#             resultSize=result_size,
#             orders=orders,
#             filters=filters,
#         )
#     except grpc.RpcError as e:
#         if e.code() == StatusCode.PERMISSION_DENIED:
#             return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
#         if e.code() == StatusCode.NOT_FOUND:
#             return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
#         else:
#             logger.error(
#                 f"[{getUserLookups.__module__}.{getUserLookups.__qualname__}] - error response e: {e}"
#             )
#             return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
#     except Exception as e:
#         logger.info(e)


@router.get(
    path="/projects",
    summary="Get projects with other related data",
    response_model=ProjectLookups,
)
@OpenTelemetry.fastApiTraceOTel
async def getProjectLookups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query(
        "",
        description="e.g. user.id:asc,user.email:desc,role.name:asc,organization.name:desc",
    ),
    filters: str = Query("", description="e.g. column_name:column_value"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = ProjectLookupClient()
        orderService = AppDi.instance.get(OrderService)
        filterService = AppDi.instance.get(FilterService)
        orders = orderService.orderStringToListOfDict(orders)
        filters = filterService.filterStringToListOfDict(filters)

        return client.projectLookups(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            filters=filters,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getProjectLookups.__module__}.{getProjectLookups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/organizations",
    summary="Get organizations with other related data",
    response_model=OrganizationLookups,
)
@OpenTelemetry.fastApiTraceOTel
async def getOrganizationLookups(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query(
        "",
        description="e.g. user.id:asc,user.email:desc,role.name:asc,organization.name:desc",
    ),
    filters: str = Query("", description="e.g. column_name:column_value"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = OrganizationLookupClient()
        orderService = AppDi.instance.get(OrderService)
        filterService = AppDi.instance.get(FilterService)
        orders = orderService.orderStringToListOfDict(orders)
        filters = filterService.filterStringToListOfDict(filters)

        return client.organizationLookups(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            filters=filters,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getOrganizationLookups.__module__}.{getOrganizationLookups.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)