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
from src.port_adapter.api.rest.grpc.v1.project.equipment.EquipmentClient import EquipmentClient
from src.port_adapter.api.rest.model.response.v1.project.equipment.Equipments import Equipments
from src.port_adapter.api.rest.model.response.v1.project.equipment.Equipment import EquipmentDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all equipment(s)', response_model=Equipments)
@OpenTelemetry.fastApiTraceOTel
async def getEquipments(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = EquipmentClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.equipments(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipments.__module__}.{getEquipments.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{equipment_id}", summary='Get equipment by id',
            response_model=EquipmentDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getEquipmentById(*, equipment_id: str = Path(...,
                                                                description='equipment id that is used to fetch equipment data'),
                               _=Depends(CustomHttpBearer())):
    """Get a equipment by id
    """
    try:
        client = EquipmentClient()
        return client.equipmentById(id=equipment_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getEquipmentById.__module__}.{getEquipmentById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create equipment', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of equipment', embed=True),
                 project_id: str = Body(..., description='project id of equipment', embed=True),
                 equipment_project_category_id: str = Body(..., description='equipment project category id of equipment', embed=True),
                 equipment_category_id: str = Body(..., description='equipment category id of equipment', embed=True),
                 equipment_category_group_id: str = Body(..., description='equipment category group id of equipment', embed=True),
                 building_id: str = Body(..., description='building id of equipment', embed=True),
                 building_level_id: str = Body(..., description='building level id of equipment', embed=True),
                 building_level_room_id: str = Body(..., description='building level room id of equipment', embed=True),
                 manufacturer_id: str = Body(..., description='manufacturer id of equipment', embed=True),
                 equipment_model_id: str = Body(..., description='equipment model id of equipment', embed=True),
                 quantity: int = Body(..., description='quantity of equipment', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = EquipmentClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_EQUIPMENT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'id': client.newId(),
                                             'name': name,
                                             'project_id': project_id,
                                             'equipment_project_category_id': equipment_project_category_id,
                                             'equipment_category_id': equipment_category_id,
                                             'equipment_category_group_id': equipment_category_group_id,
                                             'building_id': building_id,
                                             'building_level_id': building_level_id,
                                             'building_level_room_id': building_level_room_id,
                                             'manufacturer_id': manufacturer_id,
                                             'equipment_model_id': equipment_model_id,
                                             'quantity': quantity,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{equipment_id}", summary='Update equipment', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 equipment_id: str = Path(..., description='equipment id that is used in order to update the equipment'),
                 name: str = Body(..., description='name of name', embed=True),
                 project_id: str = Body(..., description='project id of project id', embed=True),
                 equipment_project_category_id: str = Body(..., description='equipment project category id of equipment project category id', embed=True),
                 equipment_category_id: str = Body(..., description='equipment category id of equipment category id', embed=True),
                 equipment_category_group_id: str = Body(..., description='equipment category group id of equipment category group id', embed=True),
                 building_id: str = Body(..., description='building id of building id', embed=True),
                 building_level_id: str = Body(..., description='building level id of building level id', embed=True),
                 building_level_room_id: str = Body(..., description='building level room id of building level room id', embed=True),
                 manufacturer_id: str = Body(..., description='manufacturer id of manufacturer id', embed=True),
                 equipment_model_id: str = Body(..., description='equipment model id of equipment model id', embed=True),
                 quantity: int = Body(..., description='quantity of quantity', embed=True),                 
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_id': equipment_id,
                                            'name': name,
                                            'project_id': project_id,
                                            'equipment_project_category_id': equipment_project_category_id,
                                            'equipment_category_id': equipment_category_id,
                                            'equipment_category_group_id': equipment_category_group_id,
                                            'building_id': building_id,
                                            'building_level_id': building_level_id,
                                            'building_level_room_id': building_level_room_id,
                                            'manufacturer_id': manufacturer_id,
                                            'equipment_model_id': equipment_model_id,
                                            'quantity': quantity,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{equipment_id}", summary='Partial update equipment', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdate(*, _=Depends(CustomHttpBearer()),
                        equipment_id: str = Path(..., description='equipment id that is used in order to update the equipment'),
                        name: str = Body(..., description='name of name', embed=True),
                        project_id: str = Body(..., description='project id of project id', embed=True),
                        equipment_project_category_id: str = Body(..., description='equipment project category id of equipment project category id', embed=True),
                        equipment_category_id: str = Body(..., description='equipment category id of equipment category id', embed=True),
                        equipment_category_group_id: str = Body(..., description='equipment category group id of equipment category group id', embed=True),
                        building_id: str = Body(..., description='building id of building id', embed=True),
                        building_level_id: str = Body(..., description='building level id of building level id', embed=True),
                        building_level_room_id: str = Body(..., description='building level room id of building level room id', embed=True),
                        manufacturer_id: str = Body(..., description='manufacturer id of manufacturer id', embed=True),
                        equipment_model_id: str = Body(..., description='equipment model id of equipment model id', embed=True),
                        quantity: int = Body(..., description='quantity of quantity', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_EQUIPMENT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_id': equipment_id,
                                            'name': name,
                                            'project_id': project_id,
                                            'equipment_project_category_id': equipment_project_category_id,
                                            'equipment_category_id': equipment_category_id,
                                            'equipment_category_group_id': equipment_category_group_id,
                                            'building_id': building_id,
                                            'building_level_id': building_level_id,
                                            'building_level_room_id': building_level_room_id,
                                            'manufacturer_id': manufacturer_id,
                                            'equipment_model_id': equipment_model_id,
                                            'quantity': quantity,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{equipment_id}", summary='Delete a equipments', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 equipment_id: str = Path(..., description='equipment id that is used in order to delete the equipment'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_EQUIPMENT.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'equipment_id': equipment_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
