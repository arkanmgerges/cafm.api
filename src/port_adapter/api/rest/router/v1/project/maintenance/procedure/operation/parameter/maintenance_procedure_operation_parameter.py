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
from src.port_adapter.api.rest.grpc.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterClient import \
    MaintenanceProcedureOperationParameterClient
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import \
    MaintenanceProcedureOperationParameterDescriptor
from src.port_adapter.api.rest.model.response.v1.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameters import \
    MaintenanceProcedureOperationParameters
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters", summary='Get all maintenance procedure operation parameter(s)', response_model=MaintenanceProcedureOperationParameters)
@OpenTelemetry.fastApiTraceOTel
async def getMaintenanceProcedureOperationParameters(*,
                            maintenance_procedure_id: str = Path(..., description='maintenance procedure id as a parent id of operation'),
                            maintenance_procedure_operation_id: str = Path(..., description='maintenance procedure operation id as a parent id'),
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = MaintenanceProcedureOperationParameterClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.maintenanceProcedureOperationParameters(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getMaintenanceProcedureOperationParameters.__module__}.{getMaintenanceProcedureOperationParameters.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters/{maintenance_procedure_operation_parameter_id}", summary='Get maintenance procedure operation parameter by id',
            response_model=MaintenanceProcedureOperationParameterDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getMaintenanceProcedureOperationParameterById(*,
                                                        maintenance_procedure_id: str = Path(...,
                                                                                             description='maintenance procedure id as a parent id of operation'),
                                                        maintenance_procedure_operation_id: str = Path(...,
                                                                                                       description='maintenance procedure operation id as a parent id'),
                                                        maintenance_procedure_operation_parameter_id: str = Path(...,
                                                                description='maintenance procedure operation parameter id that is used to fetch maintenance procedure operation parameter data'),
                               _=Depends(CustomHttpBearer())):
    """Get a maintenance procedure operation parameter by id
    """
    try:
        client = MaintenanceProcedureOperationParameterClient()
        return client.maintenanceProcedureOperationParameterById(id=maintenance_procedure_operation_parameter_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getMaintenanceProcedureOperationParameterById.__module__}.{getMaintenanceProcedureOperationParameterById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters", summary='Create maintenance procedure operation parameter', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createMaintenanceProcedureOperationParameter(*, _=Depends(CustomHttpBearer()),
                 maintenance_procedure_id: str = Path(..., description='maintenance procedure id as a parent id of operation'),
                 maintenance_procedure_operation_id: str = Path(..., description='maintenance procedure operation id as a parent id'),
                 name: str = Body(..., description='name of maintenance procedure operation parameter', embed=True),
                 unit_id: str = Body(..., description='unit id of maintenance procedure operation parameter', embed=True),
                 min_value: float = Body(..., description='min value of maintenance procedure operation parameter', embed=True),
                 max_value: float = Body(..., description='max value of maintenance procedure operation parameter', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'name': name,
                                             'unit_id': unit_id,
                                             'maintenance_procedure_operation_id': maintenance_procedure_operation_id,
                                             'min_value': min_value,
                                             'max_value': max_value,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters/{maintenance_procedure_operation_parameter_id}", summary='Update maintenance procedure operation parameter', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateMaintenanceProcedureOperationParameter(*, _=Depends(CustomHttpBearer()),
                 maintenance_procedure_id: str = Path(..., description='maintenance procedure id as a parent id of operation'),
                 maintenance_procedure_operation_id: str = Path(..., description='maintenance procedure operation id as a parent id'),
                 maintenance_procedure_operation_parameter_id: str = Path(..., description='maintenance procedure operation parameter id that is used in order to update the maintenance procedure operation parameter'),
                 name: str = Body(..., description='name of name', embed=True),
                 unit_id: str = Body(..., description='unit id of unit id', embed=True),
                 min_value: float = Body(..., description='min value of min value', embed=True),
                 max_value: float = Body(..., description='max value of max value', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_operation_parameter_id': maintenance_procedure_operation_parameter_id,
                                            'name': name,
                                            'unit_id': unit_id,
                                            'maintenance_procedure_operation_id': maintenance_procedure_operation_id,
                                            'min_value': min_value,
                                            'max_value': max_value,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters/{maintenance_procedure_operation_parameter_id}", summary='Partial update maintenance procedure operation parameter', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateMaintenanceProcedureOperationParameter(*, _=Depends(CustomHttpBearer()),
                        maintenance_procedure_id: str = Path(..., description='maintenance procedure id as a parent id of operation'),
                        maintenance_procedure_operation_id: str = Path(..., description='maintenance procedure operation id as a parent id'),
                        maintenance_procedure_operation_parameter_id: str = Path(..., description='maintenance procedure operation parameter id that is used in order to update the maintenance procedure operation parameter'),
                        name: str = Body(..., description='name of name', embed=True),
                        unit_id: str = Body(..., description='unit id of unit id', embed=True),
                        min_value: float = Body(..., description='min value of min value', embed=True),
                        max_value: float = Body(..., description='max value of max value', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_operation_parameter_id': maintenance_procedure_operation_parameter_id,
                                            'name': name,
                                            'unit_id': unit_id,
                                            'maintenance_procedure_operation_id': maintenance_procedure_operation_id,
                                            'min_value': min_value,
                                            'max_value': max_value,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{maintenance_procedure_id}/operations/{maintenance_procedure_operation_id}/parameters/{maintenance_procedure_operation_parameter_id}", summary='Delete a maintenance procedure operation parameters', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteMaintenanceProcedureOperationParameter(*, _=Depends(CustomHttpBearer()),
                 maintenance_procedure_id: str = Path(..., description='maintenance procedure id as a parent id of operation'),
                 maintenance_procedure_operation_id: str = Path(..., description='maintenance procedure operation id as a parent id'),
                 maintenance_procedure_operation_parameter_id: str = Path(..., description='maintenance procedure operation parameter id that is used in order to delete the maintenance procedure operation parameter'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_MAINTENANCE_PROCEDURE_OPERATION_PARAMETER.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'maintenance_procedure_operation_parameter_id': maintenance_procedure_operation_parameter_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}