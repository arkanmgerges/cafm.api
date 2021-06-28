"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

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
from src.port_adapter.api.rest.grpc.v1.project.organization.OrganizationClient import (
    OrganizationClient,
)
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.Organization import (
    OrganizationDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.Organizations import (
    Organizations,
)
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary="Get all organizations", response_model=Organizations)
@OpenTelemetry.fastApiTraceOTel
async def getOrganizations(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        client = OrganizationClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.organizations(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getOrganizations.__module__}.{getOrganizations.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/by_type/{organization_type}", summary="Get all organizations by type", response_model=Organizations)
@OpenTelemetry.fastApiTraceOTel
async def getOrganizationsByType(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    organization_type: str = Path(
        ...,
        description="Organization type that is used in order to retrieve the organizations",
    ),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        client = OrganizationClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.organizationsByType(
            resultFrom=result_from, resultSize=result_size, orders=orders, organizationType=organization_type
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getOrganizationsByType.__module__}.{getOrganizationsByType.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.put(
    "/{organization_id}",
    summary="Update a organization",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def updateOrganization(
    *,
    _=Depends(CustomHttpBearer()),
    organization_id: str = Path(
        ...,
        description="Organization id that is used in order to update the organization",
    ),
    name: str = Body(..., description="Organization name", embed=True),
    website_url: str = Body(
        None, description="The website url of the organization", embed=True
    ),
    organization_type: str = Body(
        None, description="The type of the organization", embed=True
    ),
    address_one: str = Body(None, description="Organization first address", embed=True),
    address_two: str = Body(None, description="Organization second address", embed=True),
    postal_code: str = Body(
        None, description="Postal code of the organization", embed=True
    ),
    country_id: int = Body(None, description="Country id", embed=True),
    city_id: int = Body(None, description="City id", embed=True),
    country_state_name: str = Body(None, description="Country State name", embed=True),
    country_state_iso_code: str = Body(
        None, description="Country State Iso code", embed=True
    ),
    manager_first_name: str = Body(
        None, description="First name of the manager", embed=True
    ),
    manager_last_name: str = Body(
        None, description="Last name of the manager", embed=True
    ),
    manager_email: str = Body(None, description="Email of the manager", embed=True),
    manager_phone_number: str = Body(
        None, description="Phone number of the manager", embed=True
    ),
    manager_avatar: str = Body(
        None, description="Avatar image of the manager", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_ORGANIZATION.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "website_url": website_url,
                    "organization_type": organization_type,
                    "address_one": address_one,
                    "address_two": address_two,
                    "postal_code": postal_code,
                    "country_id": country_id,
                    "city_id": city_id,
                    "country_state_name": country_state_name,
                    "country_state_iso_code": country_state_iso_code,
                    "manager_first_name": manager_first_name,
                    "manager_last_name": manager_last_name,
                    "manager_email": manager_email,
                    "manager_phone_number": manager_phone_number,
                    "manager_avatar": manager_avatar,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.patch(
    "/{organization_id}",
    summary="Partial update a organization",
    status_code=status.HTTP_200_OK,
)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateOrganization(
    *,
    _=Depends(CustomHttpBearer()),
    organization_id: str = Path(
        ...,
        description="Organization id that is used in order to update the organization",
    ),
    name: str = Body(None, description="Organization name", embed=True),
    website_url: str = Body(
        None, description="The website url of the organization", embed=True
    ),
    organization_type: str = Body(
        None, description="The type of the organization", embed=True
    ),
    address_one: str = Body(None, description="Organization first address", embed=True),
    address_two: str = Body(
        None, description="Organization second address", embed=True
    ),
    postal_code: str = Body(
        None, description="Postal code of the organization", embed=True
    ),
    country_id: int = Body(None, description="Country id", embed=True),
    city_id: int = Body(None, description="City id", embed=True),
    country_state_name: str = Body(None, description="Country State name", embed=True),
    country_state_iso_code: str = Body(
        None, description="Country State Iso code", embed=True
    ),
    manager_first_name: str = Body(
        None, description="First name of the manager", embed=True
    ),
    manager_last_name: str = Body(
        None, description="Last name of the manager", embed=True
    ),
    manager_email: str = Body(None, description="Email of the manager", embed=True),
    manager_phone_number: str = Body(
        None, description="Phone number of the manager", embed=True
    ),
    manager_avatar: str = Body(
        None, description="Avatar image of the manager", embed=True
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UPDATE_ORGANIZATION.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "organization_id": organization_id,
                    "name": name,
                    "website_url": website_url,
                    "organization_type": organization_type,
                    "address_one": address_one,
                    "address_two": address_two,
                    "postal_code": postal_code,
                    "country_id": country_id,
                    "city_id": city_id,
                    "country_state_name": country_state_name,
                    "country_state_iso_code": country_state_iso_code,
                    "manager_first_name": manager_first_name,
                    "manager_last_name": manager_last_name,
                    "manager_email": manager_email,
                    "manager_phone_number": manager_phone_number,
                    "manager_avatar": manager_avatar,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}

@router.get(path="/by_type/{type}", summary="Get all organizations by type", response_model=Organizations)
@OpenTelemetry.fastApiTraceOTel
async def getOrganizations(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. id:asc,email:desc"),
    type: str = Path(
        ...,
        description="Organization type to filter by",
    ),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        client = OrganizationClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.organizationsByType(
            type=type, resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getOrganizations.__module__}.{getOrganizations.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(
    path="/{organization_id}",
    summary="Get organization by id",
    response_model=OrganizationDescriptor,
)
@OpenTelemetry.fastApiTraceOTel
async def getOrganizationById(
    *,
    organization_id: str = Path(
        ..., description="Organization id that is used to fetch organization data"
    ),
    _=Depends(CustomHttpBearer()),
):
    """Get a Organization by id"""
    try:
        client = OrganizationClient()
        return client.organizationById(id=organization_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getOrganizationById.__module__}.{getOrganizationById.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post(
    path="/{organization_id}/link_to_building",
    summary="Link organization to a building",
    status_code=status.HTTP_200_OK,
)
async def linkOrganizationToBuilding(
    *,
    organization_id: str = Path(
        ..., description="Organization id that is used to fetch organization data"
    ),
    building_id: str = Body(..., description="Building id", embed=True),
    building_level_id: str = Body(None, description="Building level id", embed=True),
    building_level_room_id: str = Body(
        None, description="Building level room id", embed=True
    ),
    _=Depends(CustomHttpBearer()),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.LINK_ORGANIZATION_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "organization_id": organization_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "building_level_room_id": building_level_room_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}


@router.delete(
    path="/{organization_id}/link_to_building",
    summary="Unlink organization from a building",
    status_code=status.HTTP_200_OK,
)
async def unLinkOrganizationToBuilding(
    *,
    organization_id: str = Path(
        ..., description="Organization id that is used to fetch organization data"
    ),
    building_id: str = Body(..., description="Building id", embed=True),
    building_level_id: str = Body(None, description="Building level id", embed=True),
    building_level_room_id: str = Body(
        None, description="Building level room id", embed=True
    ),
    _=Depends(CustomHttpBearer()),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand

    producer.produce(
        obj=ProjectCommand(
            id=reqId,
            name=CommandConstant.UNLINK_ORGANIZATION_BUILDING.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {
                    "organization_id": organization_id,
                    "building_id": building_id,
                    "building_level_id": building_level_id,
                    "building_level_room_id": building_level_room_id,
                }
            ),
            external=[],
        ),
        schema=ProjectCommand.get_schema(),
    )
    return {"request_id": reqId}
