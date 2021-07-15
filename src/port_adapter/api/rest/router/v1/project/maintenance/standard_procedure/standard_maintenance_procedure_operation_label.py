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
from src.port_adapter.api.rest.grpc.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureOperationLabelClient import StandardMaintenanceProcedureOperationLabelClient
from src.port_adapter.api.rest.helper.RequestIdGenerator import RequestIdGenerator
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureOperationLabels import StandardMaintenanceProcedureOperationLabels
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.StandardMaintenanceProcedureOperationLabel import StandardMaintenanceProcedureOperationLabelDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.identity.authz import CustomAuthorization
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all standard maintenance procedure operation label(s)', response_model=StandardMaintenanceProcedureOperationLabels)
@OpenTelemetry.fastApiTraceOTel
async def getStandardMaintenanceProcedureOperationLabels(
    *,
    result_from: int = Query(0, description='Starting offset for fetching data'),
    result_size: int = Query(10, description='Item count to be fetched'),
    orders: str = Query('', description='e.g. id:asc,email:desc'),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    try:
        client = StandardMaintenanceProcedureOperationLabelClient()
        orderService = AppDi.instance.get(OrderService)
        orders = orderService.orderStringToListOfDict(order)
        return client.standardMaintenanceProcedureOperationLabels(resultFrom=result_from, resultSize=result_size, orders=orders)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getStandardMaintenanceProcedureOperationLabels.__module__}.{getStandardMaintenanceProcedureOperationLabels.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)

@router.get(path="/{standard_maintenance_procedure_operation_label_id}", summary='Get standard maintenance procedure operation label by id',
            response_model=StandardMaintenanceProcedureOperationLabelDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getStandardMaintenanceProcedureOperationLabelById(
    *,
    standard_maintenance_procedure_operation_label_id: str = Path(
        ...,
        description='standard maintenance procedure operation label id that is used to fetch standard maintenance procedure operation label data',
    ),
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
):
    """Get a standard maintenance procedure operation label by id
    """
    try:
        client = StandardMaintenanceProcedureOperationLabelClient()
        return client.standardMaintenanceProcedureOperationLabelById(id=standard_maintenance_procedure_operation_label_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getStandardMaintenanceProcedureOperationLabelById.__module__}.{getStandardMaintenanceProcedureOperationLabelById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create standard maintenance procedure operation label', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createStandardMaintenanceProcedureOperationLabel(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
        label: str = Body(..., description='label of standard maintenance procedure operation label', embed=True),
        generate_alert: int = Body(..., description='generate alert of standard maintenance procedure operation label', embed=True),
        standard_maintenance_procedure_operation_id: str = Body(..., description='standard maintenance procedure operation id of standard maintenance procedure operation label', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    client = StandardMaintenanceProcedureOperationLabelClient()
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'standard_maintenance_procedure_operation_label_id': client.newId(),
                                             'label': label,
                                             'generate_alert': generate_alert,
                                             'standard_maintenance_procedure_operation_id': standard_maintenance_procedure_operation_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{standard_maintenance_procedure_operation_label_id}", summary='Update standard maintenance procedure operation label', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateStandardMaintenanceProcedureOperationLabel(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_maintenance_procedure_operation_label_id: str = Path(..., description='standard maintenance procedure operation label id that is used in order to update the standard maintenance procedure operation label'),
        label: str = Body(..., description='label of standard maintenance procedure operation label', embed=True),
        generate_alert: int = Body(..., description='generate alert of standard maintenance procedure operation label', embed=True),
        standard_maintenance_procedure_operation_id: str = Body(..., description='standard maintenance procedure operation id of standard maintenance procedure operation label', embed=True),                 
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_maintenance_procedure_operation_label_id': standard_maintenance_procedure_operation_label_id,
                                            'label': label,
                                            'generate_alert': generate_alert,
                                            'standard_maintenance_procedure_operation_id': standard_maintenance_procedure_operation_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{standard_maintenance_procedure_operation_label_id}", summary='Partial update standard maintenance procedure operation label', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateStandardMaintenanceProcedureOperationLabel(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_maintenance_procedure_operation_label_id: str = Path(..., description='standard maintenance procedure operation label id that is used in order to update the standard maintenance procedure operation label'),
        label: str = Body(None, description='label of standard maintenance procedure operation label', embed=True),
        generate_alert: int = Body(None, description='generate alert of standard maintenance procedure operation label', embed=True),
        standard_maintenance_procedure_operation_id: str = Body(None, description='standard maintenance procedure operation id of standard maintenance procedure operation label', embed=True),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_maintenance_procedure_operation_label_id': standard_maintenance_procedure_operation_label_id,
                                            'label': label,
                                            'generate_alert': generate_alert,
                                            'standard_maintenance_procedure_operation_id': standard_maintenance_procedure_operation_id,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{standard_maintenance_procedure_operation_label_id}", summary='Delete a standard maintenance procedure operation labels', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteStandardMaintenanceProcedureOperationLabel(*,
    _=Depends(CustomHttpBearer()),
    _1=Depends(CustomAuthorization()),
    standard_maintenance_procedure_operation_label_id: str = Path(
        ..., description='standard maintenance procedure operation label id that is used in order to delete the standard maintenance procedure operation label'
    ),
):
    reqId = RequestIdGenerator.generateId()
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_STANDARD_MAINTENANCE_PROCEDURE_OPERATION_LABEL.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'standard_maintenance_procedure_operation_label_id': standard_maintenance_procedure_operation_label_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
