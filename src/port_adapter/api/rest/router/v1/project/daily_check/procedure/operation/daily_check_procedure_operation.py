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
from src.port_adapter.api.rest.grpc.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperationClient import DailyCheckProcedureOperationClient
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperations import DailyCheckProcedureOperations
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperation import DailyCheckProcedureOperationDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.api.rest.router.v1.project.daily_check.procedure.operation.DailyCheckProcedureOperationType import \
    DailyCheckProcedureOperationType
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()



@router.get(path="/by_daily_check_procedure_id/{daily_check_procedure_id}", summary='Get all daily check procedure operation by daily check procedure id', response_model=DailyCheckProcedureOperations)
@OpenTelemetry.fastApiTraceOTel
async def getDailyCheckProcedureOperationsByDailyCheckProcedureId(*,
                            daily_check_procedure_id: str = Path(..., description='daily check procedure id that is used to fetch daily check procedure operation data'),
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = DailyCheckProcedureOperationClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.dailyCheckProcedureOperationsByDailyCheckProcedureId(dailyCheckProcedureId=daily_check_procedure_id, resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getDailyCheckProcedureOperationsByDailyCheckProcedureId.__module__}.{getDailyCheckProcedureOperationsByDailyCheckProcedureId.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{daily_check_procedure_id}/operations/{daily_check_procedure_operation_id}", summary='Get daily check procedure operation by id',
            response_model=DailyCheckProcedureOperationDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getDailyCheckProcedureOperationById(*,
                                              daily_check_procedure_id: str = Path(...,
                                                                                   description='daily check procedure id as a parent id'),
                                              daily_check_procedure_operation_id: str = Path(...,
                                                                description='daily check procedure operation id that is used to fetch daily check procedure operation data'),
                               _=Depends(CustomHttpBearer())):
    """Get a daily check procedure operation by id
    """
    try:
        client = DailyCheckProcedureOperationClient()
        return client.dailyCheckProcedureOperationById(id=daily_check_procedure_operation_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getDailyCheckProcedureOperationById.__module__}.{getDailyCheckProcedureOperationById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("/{daily_check_procedure_id}/operations", summary='Create daily check procedure operation', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createDailyCheckProcedureOperation(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of daily check procedure operation', embed=True),
                 description: str = Body(..., description='description of daily check procedure operation', embed=True),
                 type: DailyCheckProcedureOperationType = Body(..., description='type of daily check procedure operation', embed=True),
                 daily_check_procedure_id: str = Path(..., description='daily check procedure id of daily check procedure operation', embed=True),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_DAILY_CHECK_PROCEDURE_OPERATION.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'name': name,
                                             'description': description,
                                             'type': type,
                                             'daily_check_procedure_id': daily_check_procedure_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{daily_check_procedure_id}/operations/{daily_check_procedure_operation_id}", summary='Update daily check procedure operation', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateDailyCheckProcedureOperation(*, _=Depends(CustomHttpBearer()),
                 daily_check_procedure_operation_id: str = Path(..., description='daily check procedure operation id that is used in order to update the daily check procedure operation'),
                 name: str = Body(..., description='name of name', embed=True),
                 description: str = Body(..., description='description of description', embed=True),
                 type: DailyCheckProcedureOperationType = Body(..., description='type of type', embed=True),
                 daily_check_procedure_id: str = Path(..., description='daily check procedure id of daily check procedure id'),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_DAILY_CHECK_PROCEDURE_OPERATION.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_operation_id': daily_check_procedure_operation_id,
                                            'name': name,
                                            'description': description,
                                            'type': type,
                                            'daily_check_procedure_id': daily_check_procedure_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{daily_check_procedure_id}/operations/{daily_check_procedure_operation_id}", summary='Partial update daily check procedure operation', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateDailyCheckProcedureOperation(*, _=Depends(CustomHttpBearer()),
                        daily_check_procedure_id: str = Path(..., description='daily check procedure id of daily check procedure id'),
                        daily_check_procedure_operation_id: str = Path(..., description='daily check procedure operation id that is used in order to update the daily check procedure operation'),
                        name: str = Body(..., description='name of name', embed=True),
                        description: str = Body(..., description='description of description', embed=True),
                        type: DailyCheckProcedureOperationType = Body(..., description='type of type', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_DAILY_CHECK_PROCEDURE_OPERATION.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_operation_id': daily_check_procedure_operation_id,
                                            'name': name,
                                            'description': description,
                                            'type': type,
                                            'daily_check_procedure_id': daily_check_procedure_id,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{daily_check_procedure_id}/operations/{daily_check_procedure_operation_id}", summary='Delete a daily check procedure operations', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteDailyCheckProcedureOperation(*, _=Depends(CustomHttpBearer()),
                                             daily_check_procedure_id: str = Path(...,
                                                                                  description='daily check procedure id of daily check procedure id'),
                 daily_check_procedure_operation_id: str = Path(..., description='daily check procedure operation id that is used in order to delete the daily check procedure operation'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_DAILY_CHECK_PROCEDURE_OPERATION.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_operation_id': daily_check_procedure_operation_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
