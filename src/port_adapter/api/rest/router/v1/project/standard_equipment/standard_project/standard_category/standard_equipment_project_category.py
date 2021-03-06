"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json
from uuid import uuid4

import grpc
from fastapi import APIRouter, Depends, Query, Body
from fastapi import Response
from fastapi.params import Path
from grpc.beta.interfaces import StatusCode
from starlette import status
from starlette.status import (
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_403_FORBIDDEN,
)


import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategoryClient import (
    StandardEquipmentProjectCategoryClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategories import (
    StandardEquipmentProjectCategories,
)
from src.port_adapter.api.rest.model.response.v1.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategory import (
    StandardEquipmentProjectCategoryDescriptor,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(
    path="",
    summary="Get all standard equipment project category(s)",
    response_model=StandardEquipmentProjectCategories,
)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentProjectCategories(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        print(f"___________________\n{orders}")
        client = StandardEquipmentProjectCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.standardEquipmentProjectCategories(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getStandardEquipmentProjectCategories.__module__}.{getStandardEquipmentProjectCategories.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(
    path="/by_organization_id/{organization_id}",
    summary="Get all standard equipment project category by organization id",
    response_model=StandardEquipmentProjectCategories,
)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentProjectCategoriesByOrganizationId(
    *,
    organization_id: str = Path(
        ...,
        description="organization id that is used to fetch standard equipment project category data",
    ),
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
):
    try:
        print(f"___________________\n{orders}")
        client = StandardEquipmentProjectCategoryClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.standardEquipmentProjectCategoriesByOrganizationId(
            resultFrom=result_from,
            resultSize=result_size,
            orders=orders,
            organizationId=organization_id,
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getStandardEquipmentProjectCategoriesByOrganizationId.__module__}.{getStandardEquipmentProjectCategoriesByOrganizationId.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        print("===================")

        logger.info(e)


@router.get(
    path="/{standard_equipment_project_category_id}",
    summary="Get standard equipment project category by id",
    response_model=StandardEquipmentProjectCategoryDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getStandardEquipmentProjectCategoryById(
    *,
    standard_equipment_project_category_id: str = Path(
        ...,
        description="standard equipment project category id that is used to fetch standard equipment project category data",
    ),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    """Get a standard equipment project category by id"""
    try:
        client = StandardEquipmentProjectCategoryClient()
        return client.standardEquipmentProjectCategoryById(
            id=standard_equipment_project_category_id
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getStandardEquipmentProjectCategoryById.__module__}.{getStandardEquipmentProjectCategoryById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post(
    "",
    summary="Create standard equipment project category",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def createStandardEquipmentProjectCategory(
    *,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    name: str = Body(
        ..., description="name of standard equipment project category", embed=True
    ),
    organization_id: str = Body(
        ...,
        description="organization id of standard equipment project category",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    client = StandardEquipmentProjectCategoryClient()
    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.CREATE_STANDARD_EQUIPMENT_PROJECT_CATEGORY.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_project_category_id": client.newId(),
                    "name": name,
                    "organization_id": organization_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.put(
    "/{standard_equipment_project_category_id}",
    summary="Update standard equipment project category",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateStandardEquipmentProjectCategory(
    *,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_equipment_project_category_id: str = Path(
        ...,
        description="standard equipment project category id that is used in order to update the standard equipment project category",
    ),
    name: str = Body(
        ..., description="name of standard equipment project category", embed=True
    ),
    organization_id: str = Body(
        ...,
        description="organization id of standard equipment project category",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_STANDARD_EQUIPMENT_PROJECT_CATEGORY.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_project_category_id": standard_equipment_project_category_id,
                    "name": name,
                    "organization_id": organization_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{standard_equipment_project_category_id}",
    summary="Partial update standard equipment project category",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateStandardEquipmentProjectCategory(
    *,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_equipment_project_category_id: str = Path(
        ...,
        description="standard equipment project category id that is used in order to update the standard equipment project category",
    ),
    name: str = Body(
        None, description="name of standard equipment project category", embed=True
    ),
    organization_id: str = Body(
        None,
        description="organization id of standard equipment project category",
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_STANDARD_EQUIPMENT_PROJECT_CATEGORY.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_project_category_id": standard_equipment_project_category_id,
                    "name": name,
                    "organization_id": organization_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    "/{standard_equipment_project_category_id}",
    summary="Delete a standard equipment project categories",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def deleteStandardEquipmentProjectCategory(
    *,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_equipment_project_category_id: str = Path(
        ...,
        description="standard equipment project category id that is used in order to delete the standard equipment project category",
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.DELETE_STANDARD_EQUIPMENT_PROJECT_CATEGORY.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "standard_equipment_project_category_id": standard_equipment_project_category_id
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
