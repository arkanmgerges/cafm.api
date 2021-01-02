"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from uuid import uuid4

from fastapi import APIRouter, Depends, Body
from starlette import status

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.post("/role_to_resource", summary='Link access for a role to a resource', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to link access to a resource', embed=True),
                 resource_id: str = Body(..., description='Resource is for a role to have access to', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.PROVIDE_ACCESS_ROLE_TO_RESOURCE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'resource_id': resource_id})),
                     schema=ApiCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/role_to_resource", summary='Remove a link access for a role to a resource',
               status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 role_id: str = Body(..., description='Role id to remove link access to a resource', embed=True),
                 resource_id: str = Body(..., description='Resource is for a role to remove the access to', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=ApiCommand(id=reqId, name=CommandConstant.REVOKE_ACCESS_ROLE_TO_RESOURCE.value,
                                    metadata=json.dumps({"token": Client.token}),
                                    data=json.dumps(
                                        {'role_id': role_id, 'resource_id': resource_id})),
                     schema=ApiCommand.get_schema())
