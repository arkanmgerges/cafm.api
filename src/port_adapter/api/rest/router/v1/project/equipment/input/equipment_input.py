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
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_403_FORBIDDEN

import src.port_adapter.AppDi as AppDi
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.grpc.v1.project.equipment.input.EquipmentInputClient import EquipmentInputClient
from src.port_adapter.api.rest.model.response.v1.project.equipment.input.EquipmentInputs import EquipmentInputs
from src.port_adapter.api.rest.model.response.v1.project.equipment.input.EquipmentInput import EquipmentInputDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all equipment input(s)', response_model=EquipmentInputs)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentInputs(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = EquipmentInputClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.equipmentInputs(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentInputs.__module__}.{getEquipmentInputs.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{equipment_input_id}", summary='Get equipment input by id',
            response_model=EquipmentInputDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentInputById(*, equipment_input_id: str = Path(...,
                                                                description='equipment input id that is used to fetch equipment input data'),
                               _=Depends(CustomHttpBearer())):
    """Get a equipment input by id
    """
    try:
        client = EquipmentInputClient()
        return client.equipmentInputById(id=equipment_input_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentInputById.__module__}.{getEquipmentInputById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create equipment input', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createEquipmentInput(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of equipment input', embed=True),
                 value: str = Body(..., description='value of equipment input', embed=True),
                 unit_id: str = Body(..., description='unit id of equipment input', embed=True),
                 equipment_id: str = Body(..., description='equipment id of equipment input', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = EquipmentInputClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_EQUIPMENT_INPUT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'equipment_input_id': client.newId(),
                                             'name': name,
                                             'value': value,
                                             'unit_id': unit_id,
                                             'equipment_id': equipment_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{equipment_input_id}", summary='Update equipment input', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateEquipmentInput(*, _=Depends(CustomHttpBearer()),
                 equipment_input_id: str = Path(..., description='equipment input id that is used in order to update the equipment input'),
                 name: str = Body(..., description='name of name', embed=True),
                 value: str = Body(..., description='value of value', embed=True),
                 unit_id: str = Body(..., description='unit id of unit id', embed=True),
                 equipment_id: str = Body(..., description='equipment id of equipment input', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_INPUT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_input_id': equipment_input_id,
                                            'name': name,
                                            'value': value,
                                            'unit_id': unit_id,
                                            'equipment_id': equipment_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{equipment_input_id}", summary='Partial update equipment input', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateEquipmentInput(*, _=Depends(CustomHttpBearer()),
                        equipment_input_id: str = Path(..., description='equipment input id that is used in order to update the equipment input'),
                        name: str = Body(None, description='name of name', embed=True),
                        value: str = Body(None, description='value of value', embed=True),
                        unit_id: str = Body(None, description='unit id of unit id', embed=True),
                        equipment_id: str = Body(None, description='equipment id of equipment input', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT_INPUT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_input_id': equipment_input_id,
                                            'name': name,
                                            'value': value,
                                            'unit_id': unit_id,
                                            'equipment_id': equipment_id,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{equipment_input_id}", summary='Delete a equipment inputs', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteEquipmentInput(*, _=Depends(CustomHttpBearer()),
                 equipment_input_id: str = Path(..., description='equipment input id that is used in order to delete the equipment input'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_EQUIPMENT_INPUT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_input_id': equipment_input_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
