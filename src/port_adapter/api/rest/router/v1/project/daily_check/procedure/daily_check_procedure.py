"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json
from typing import Optional
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
from src.port_adapter.api.rest.grpc.v1.project.daily_check.procedure.DailyCheckProcedureClient import DailyCheckProcedureClient
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedures import DailyCheckProcedures
from src.port_adapter.api.rest.model.response.v1.project.daily_check.procedure.DailyCheckProcedure import DailyCheckProcedureDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all daily check procedure(s)', response_model=DailyCheckProcedures)
@OpenTelemetry.fastApiTraceOTel
async def getDailyCheckProcedures(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = DailyCheckProcedureClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.dailyCheckProcedures(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getDailyCheckProcedures.__module__}.{getDailyCheckProcedures.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{daily_check_procedure_id}", summary='Get daily check procedure by id',
            response_model=DailyCheckProcedureDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getDailyCheckProcedureById(*, daily_check_procedure_id: str = Path(...,
                                                                description='daily check procedure id that is used to fetch daily check procedure data'),
                               _=Depends(CustomHttpBearer())):
    """Get a daily check procedure by id
    """
    try:
        client = DailyCheckProcedureClient()
        return client.dailyCheckProcedureById(id=daily_check_procedure_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getDailyCheckProcedureById.__module__}.{getDailyCheckProcedureById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create daily check procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def createDailyCheckProcedure(*, _=Depends(CustomHttpBearer()),
                 name: str = Body(..., description='name of daily check procedure', embed=True),
                 description: str = Body(..., description='description of daily check procedure', embed=True),
                 equipment_id: Optional[str] = Body(description='equipment id of daily check procedure', embed=True, default=None),
                 equipment_category_group_id: Optional[str] = Body(description='equipment category group id of daily check procedure', embed=True, default=None),
                ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_DAILY_CHECK_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {
                                             'name': name,
                                             'description': description,
                                             'equipment_id': equipment_id,
                                             'equipment_category_group_id': equipment_category_group_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{daily_check_procedure_id}", summary='Update daily check procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def updateDailyCheckProcedure(*, _=Depends(CustomHttpBearer()),
                 daily_check_procedure_id: str = Path(..., description='daily check procedure id that is used in order to update the daily check procedure'),
                 name: str = Body(..., description='name of name', embed=True),
                 description: str = Body(..., description='description of description', embed=True),
                 equipment_id: Optional[str] = Body(default=None, description='equipment id of equipment id', embed=True),
                 equipment_category_group_id: Optional[str] = Body(default=None, description='equipment category group id of equipment category group id', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_DAILY_CHECK_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_id': daily_check_procedure_id,
                                            'name': name,
                                            'description': description,
                                            'equipment_id': equipment_id,
                                            'equipment_category_group_id': equipment_category_group_id,
                                             }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{daily_check_procedure_id}", summary='Partial update daily check procedure', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdateDailyCheckProcedure(*, _=Depends(CustomHttpBearer()),
                        daily_check_procedure_id: str = Path(..., description='daily check procedure id that is used in order to update the daily check procedure'),
                        name: str = Body(..., description='name of name', embed=True),
                        description: str = Body(..., description='description of description', embed=True),
                        equipment_id: str = Body(..., description='equipment id of equipment id', embed=True),
                        equipment_category_group_id: str = Body(..., description='equipment category group id of equipment category group id', embed=True),
                        ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_DAILY_CHECK_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_id': daily_check_procedure_id,
                                            'name': name,
                                            'description': description,
                                            'equipment_id': equipment_id,
                                            'equipment_category_group_id': equipment_category_group_id,
                                            }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{daily_check_procedure_id}", summary='Delete a daily check procedures', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def deleteDailyCheckProcedure(*, _=Depends(CustomHttpBearer()),
                 daily_check_procedure_id: str = Path(..., description='daily check procedure id that is used in order to delete the daily check procedure'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_DAILY_CHECK_PROCEDURE.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'daily_check_procedure_id': daily_check_procedure_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}