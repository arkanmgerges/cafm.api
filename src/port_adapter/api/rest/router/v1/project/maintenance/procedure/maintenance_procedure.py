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
from src.port_adapter.api.rest.grpc.v1.project.maintenance.procedure.MaintenanceProcedureClient import MaintenanceProcedureClient
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.MaintenanceProcedures import MaintenanceProcedures
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.MaintenanceProcedure import MaintenanceProcedureDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.project.maintenance.procedure.MaintenanceProcedureFrequency import \
    MaintenanceProcedureFrequency
from src.port_adapter.api.rest.router.v1.project.maintenance.procedure.MaintenanceProcedureType import \
    MaintenanceProcedureType
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all maintenance procedure(s)', response_model=MaintenanceProcedures)
@OpenTelemetry.fastApiTraceOTel
async def getMaintenanceProcedures(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = MaintenanceProcedureClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.maintenanceProcedures(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getMaintenanceProcedures.__module__}.{getMaintenanceProcedures.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/by_equipment_id/{equipment_id}", summary='Get all maintenance procedure by equipment id', response_model=MaintenanceProcedures)
@OpenTelemetry.fastApiTraceOTel
async def getMaintenanceProceduresByEquipmentId(*,
                            equipment_id: str = Path(..., description='equipment id that is used to fetch maintenance procedure data'),
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = MaintenanceProcedureClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.maintenanceProceduresByEquipmentId(equipmentId=equipment_id, resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getMaintenanceProcedures.__module__}.{getMaintenanceProcedures.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/{maintenance_procedure_id}", summary='Get maintenance procedure by id',
            response_model=MaintenanceProcedureDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getMaintenanceProcedureById(*, maintenance_procedure_id: str = Path(...,
                                                                description='maintenance procedure id that is used to fetch maintenance procedure data'),
                               _=Depends(CustomHttpBearer())):
    """Get a maintenance procedure by id
    """
    try:
        client = MaintenanceProcedureClient()
        return client.maintenanceProcedureById(id=maintenance_procedure_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getMaintenanceProcedureById.__module__}.{getMaintenanceProcedureById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create maintenance procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createMaintenanceProcedure(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of maintenance procedure', embed=True),
                 type: MaintenanceProcedureType = Body(..., description='hard or soft', embed=True),
                 frequency: MaintenanceProcedureFrequency = Body(..., description='procedure frequency', embed=True),
                 start_date: int = Body(..., description='start date of maintenance procedure', embed=True),
                 subcontractor_id: str = Body(..., description='subcontractor id of maintenance procedure', embed=True),
                 equipment_id: str = Body(..., description='equipment id of maintenance procedure', embed=True),
                ):
    reqId = str(uuid4())
    start_date = start_date if start_date is not None and start_date > DateTimeHelper.intOneYearAfterEpochTimeInSecond() else None
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_MAINTENANCE_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'name': name,
                                             'type': type,
                                             'frequency': frequency,
                                             'start_date': start_date,
                                             'subcontractor_id': subcontractor_id,
                                             'equipment_id': equipment_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{maintenance_procedure_id}", summary='Update maintenance procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateMaintenanceProcedure(*, _=Depends(CustomHttpBearer()),
                 maintenance_procedure_id: str = Path(..., description='maintenance procedure id that is used in order to update the maintenance procedure'),
                 name: str = Body(..., description='name of name', embed=True),
                 type: MaintenanceProcedureType = Body(..., description='hard or soft', embed=True),
                 frequency: MaintenanceProcedureFrequency = Body(..., description='procedure frequency', embed=True),
                 start_date: int = Body(..., description='start date of start date', embed=True),
                 subcontractor_id: str = Body(..., description='subcontractor id of subcontractor id', embed=True),
                 equipment_id: str = Body(..., description='equipment id of maintenance procedure', embed=True),
                 ):
    reqId = str(uuid4())
    start_date = start_date if start_date is not None and start_date > DateTimeHelper.intOneYearAfterEpochTimeInSecond() else None
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_MAINTENANCE_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_id': maintenance_procedure_id,
                                            'name': name,
                                            'type': type,
                                            'frequency': frequency,
                                            'start_date': start_date,
                                            'equipment_id': equipment_id,
                                            'subcontractor_id': subcontractor_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{maintenance_procedure_id}", summary='Partial update maintenance procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateMaintenanceProcedure(*, _=Depends(CustomHttpBearer()),
                        maintenance_procedure_id: str = Path(..., description='maintenance procedure id that is used in order to update the maintenance procedure'),
                        name: str = Body(..., description='name of name', embed=True),
                                            type: MaintenanceProcedureType = Body(..., description='hard or soft',
                                                                                  embed=True),
                                            frequency: MaintenanceProcedureFrequency = Body(...,
                                                                                            description='procedure frequency',
                                                                                            embed=True),
                        start_date: int = Body(..., description='start date of start date', embed=True),
                        subcontractor_id: str = Body(..., description='subcontractor id of subcontractor id', embed=True),
                        equipment_id: str = Body(..., description='equipment id of maintenance procedure', embed=True),
                        ):
    reqId = str(uuid4())
    start_date = start_date if start_date is not None and start_date > DateTimeHelper.intOneYearAfterEpochTimeInSecond() else None
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_MAINTENANCE_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_id': maintenance_procedure_id,
                                            'name': name,
                                            'type': type,
                                            'frequency': frequency,
                                            'start_date': start_date,
                                            'subcontractor_id': subcontractor_id,
                                             'equipment_id': equipment_id,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{maintenance_procedure_id}", summary='Delete a maintenance procedures', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteMaintenanceProcedure(*, _=Depends(CustomHttpBearer()),
                 maintenance_procedure_id: str = Path(..., description='maintenance procedure id that is used in order to delete the maintenance procedure'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_MAINTENANCE_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_id': maintenance_procedure_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
