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
from src.port_adapter.api.rest.grpc.v1.identity.realm.RealmClient import RealmClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.identity.Realm import RealmDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Realms import Realms
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.api.rest.router.v1.identity.realm.RealmType import RealmType
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()

"""
c4model|cb|api:Component(api__identity_realm_py__getRealms, "Get Realms", "http(s)", "")
c4model:Rel(api__identity_realm_py__getRealms, identity__grpc__RealmAppServiceListener__realms, "Get realms", "grpc")
"""


@router.get(path="", summary="Get all realms", response_model=Realms)
@OpenTelemetry.fastApiTraceOTel
async def getRealms(
    *,
    result_from: int = Query(0, description="Starting offset for fetching data"),
    result_size: int = Query(10, description="Item count to be fetched"),
    orders: str = Query("", description="e.g. name:asc,age:desc"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    try:
        client = RealmClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(orders)
        return client.realms(
            resultFrom=result_from, resultSize=result_size, orders=orders
        )
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRealms.__module__}.{getRealms.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_realm_py__getRealm, "Get Realm", "http(s)", "Get realm by id")
c4model:Rel(api__identity_realm_py__getRealm, identity__grpc__RealmAppServiceListener__realmById, "Get realm by id", "grpc")
"""


@router.get(path="/{realm_id}", summary="Get realm", response_model=RealmDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getRealm(
    *,
    realm_id: str = Path(..., description="Realm id that is used to fetch realm data"),
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
):
    """Get a Realm by id"""
    try:
        client = RealmClient()
        return client.realmById(realmId=realm_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f"[{getRealm.__module__}.{getRealm.__qualname__}] - error response e: {e}"
            )
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


"""
c4model|cb|api:Component(api__identity_realm_py__create, "Create Realm", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_realm_py__create__api_command_topic, "CommonCommandConstant.CREATE_REALM.value", "api command topic", "")
c4model:Rel(api__identity_realm_py__create, api__identity_realm_py__create__api_command_topic, "CommonCommandConstant.CREATE_REALM.value", "message")
"""


@router.post("", summary="Create a new realm", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createRealm(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    name: str = Body(..., description="Title of the realm", embed=True),
    realm_type: str = Body(
        ...,
        description="The type can be " + ", ".join([e.value for e in RealmType]),
        embed=True,
    ),
):
    reqId = RequestIdGenerator.generateListId(2)
    realm_type = realm_type.lower()
    if realm_type not in [e.value for e in RealmType]:
        raise ValueError(
            "Invalid realm_type, it should be one of these: "
            + ", ".join([e.value for e in RealmType])
        )
    producer = AppDi.instance.get(SimpleProducer)
    client = RealmClient()
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.CREATE_REALM.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps(
                {"realm_id": client.newId(), "name": name, "realm_type": realm_type}
            ),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}


"""
c4model|cb|api:Component(api__identity_realm_py__delete, "Delete Realm", "http(s)", "")
c4model|cb|api:ComponentQueue(api__identity_realm_py__delete__api_command_topic, "CommonCommandConstant.DELETE_REALM.value", "api command topic", "")
c4model:Rel(api__identity_realm_py__delete, api__identity_realm_py__delete__api_command_topic, "CommonCommandConstant.DELETE_REALM.value", "message")
"""


@router.delete("/{realm_id}", summary="Delete a realm", status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteRealm(
    *,
    _=Depends(CustomHttpBearer()),
    __=Depends(CustomAuthorization()),
    realm_id: str = Path(
        ..., description="Realm id that is used in order to delete the realm"
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(
        obj=ApiCommand(
            id=reqId,
            name=CommandConstant.DELETE_REALM.value,
            metadata=json.dumps({"token": Client.token}),
            data=json.dumps({"realm_id": realm_id}),
        ),
        schema=ApiCommand.get_schema(),
    )
    return {"request_id": reqId}
