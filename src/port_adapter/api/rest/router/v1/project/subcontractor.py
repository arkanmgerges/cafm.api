"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
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
from src.port_adapter.api.rest.grpc.v1.project.subcontractor.SubcontractorClient import SubcontractorClient
from src.port_adapter.api.rest.model.response.v1.project.Subcontractors import Subcontractors
from src.port_adapter.api.rest.model.response.v1.project.Subcontractor import SubcontractorDescriptor
from src.port_adapter.api.rest.router.v1.identity.auth import CustomHttpBearer
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry

router = APIRouter()


@router.get(path="", summary='Get all subcontractors', response_model=Subcontractors)
@OpenTelemetry.fastApiTraceOTel
async def getSubcontractors(*,
                            result_from: int = Query(0, description='Starting offset for fetching data'),
                            result_size: int = Query(10, description='Item count to be fetched'),
                            order: str = Query('', description='e.g. id:asc,email:desc'),
                            _=Depends(CustomHttpBearer())):
    try:
        client = SubcontractorClient()
        orderService = AppDi.instance.get(OrderService)
        order = orderService.orderStringToListOfDict(order)
        return client.subcontractors(resultFrom=result_from, resultSize=result_size, order=order)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getSubcontractors.__module__}.{getSubcontractors.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.get(path="/{subcontractors_id}", summary='Get subcontractors by id',
            response_model=SubcontractorDescriptor)
@OpenTelemetry.fastApiTraceOTel
async def getSubcontractorById(*, subcontractors_id: str = Path(...,
                                                                description='Subcontractor id that is used to fetch subcontractor data'),
                               _=Depends(CustomHttpBearer())):
    """Get a Subcontractor by id
    """
    try:
        client = SubcontractorClient()
        return client.subcontractorById(id=subcontractors_id)
    except grpc.RpcError as e:
        if e.code() == StatusCode.PERMISSION_DENIED:
            return Response(content=str(e), status_code=HTTP_403_FORBIDDEN)
        if e.code() == StatusCode.NOT_FOUND:
            return Response(content=str(e), status_code=HTTP_404_NOT_FOUND)
        else:
            logger.error(
                f'[{getSubcontractorById.__module__}.{getSubcontractorById.__qualname__}] - error response e: {e}')
            return Response(content=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        logger.info(e)


@router.post("", summary='Create a subcontractors', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def create(*, _=Depends(CustomHttpBearer()),
                 company_name: str = Body(..., description='subcontractor name', embed=True),
                 website_url: str = Body(..., description='The website url of the subcontractor', embed=True),
                 contact_person: str = Body(..., description='The contact person of the subcontractor', embed=True),
                 email: str = Body(..., description='Email of the subcontractor', embed=True),
                 phone_number: str = Body(..., description='Phone number of the subcontractor', embed=True),
                 address_one: str = Body(..., description='subcontractor first address', embed=True),
                 address_two: str = Body(..., description='subcontractor second address', embed=True), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.CREATE_SUBCONTRACTOR.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'company_name': company_name,
                                             'website_url': website_url,
                                             'contact_person': contact_person,
                                             'email': email,
                                             'phone_number': phone_number,
                                             'address_one': address_one,
                                             'address_two': address_two, }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.put("/{subcontractors_id}", summary='Update a subcontractors', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def update(*, _=Depends(CustomHttpBearer()),
                 subcontractors_id: str = Path(...,
                                               description='Subcontractor id that is used in order to update the subcontractor'),
                 company_name: str = Body(..., description='subcontractor name', embed=True),
                 website_url: str = Body(..., description='The website url of the subcontractor', embed=True),
                 contact_person: str = Body(..., description='The contact person of the subcontractor', embed=True),
                 email: str = Body(..., description='Email of the subcontractor', embed=True),
                 phone_number: str = Body(..., description='Phone number of the subcontractor', embed=True),
                 address_one: str = Body(..., description='subcontractor first address', embed=True),
                 address_two: str = Body(..., description='subcontractor second address', embed=True),
                 ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_SUBCONTRACTOR.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'id': subcontractors_id,
                                             'company_name': company_name,
                                             'website_url': website_url,
                                             'contact_person': contact_person,
                                             'email': email,
                                             'phone_number': phone_number,
                                             'address_one': address_one,
                                             'address_two': address_two, }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.patch("/{subcontractors_id}", summary='Partial update a subcontractors', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def partialUpdate(*, _=Depends(CustomHttpBearer()),
                        subcontractors_id: str = Path(...,
                                                      description='Subcontractor id that is used in order to update the subcontractor'),
                        company_name: str = Body(None, description='subcontractor name', embed=True),
                        website_url: str = Body(None, description='The website url of the subcontractor', embed=True),
                        contact_person: str = Body(None, description='The contact person of the subcontractor',
                                                   embed=True),
                        email: str = Body(None, description='Email of the subcontractor', embed=True),
                        phone_number: str = Body(None, description='Phone number of the subcontractor', embed=True),
                        address_one: str = Body(None, description='subcontractor first address', embed=True),
                        address_two: str = Body(None, description='subcontractor second address', embed=True)):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.UPDATE_SUBCONTRACTOR.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'id': subcontractors_id,
                                             'company_name': company_name,
                                             'website_url': website_url,
                                             'contact_person': contact_person,
                                             'email': email,
                                             'phone_number': phone_number,
                                             'address_one': address_one,
                                             'address_two': address_two, }),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{subcontractors_id}", summary='Delete a subcontractors', status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def delete(*, _=Depends(CustomHttpBearer()),
                 subcontractors_id: str = Path(...,
                                               description='Subcontractor id that is used in order to delete the subcontractor'), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.DELETE_SUBCONTRACTOR.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps(
                                            {'id': subcontractors_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.post("/{subcontractors_id}/assign_to_oraganization", summary='Assign a subcontractor to a oraganization',
             status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def assign(*, _=Depends(CustomHttpBearer()),
                 subcontractors_id: str = Path(...,
                                               description='Subcontractor id that is used in order to assign a oraganization'),
                 oraganization_id: str = Body(..., description='Oraganization id that is need to be assigned',
                                              embed=True), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(obj=ProjectCommand(id=reqId, name=CommandConstant.ASSIGN_SUBCONTRACTOR_TO_ORGANIZATION.value,
                                        metadata=json.dumps({"token": Client.token}),
                                        data=json.dumps({'id': subcontractors_id,
                                                         'org_id': oraganization_id}),
                                        external=[]),
                     schema=ProjectCommand.get_schema())
    return {"request_id": reqId}


@router.delete("/{subcontractors_id}/assign_to_oraganization", summary='Unassign a subcontractor to a oraganization',
               status_code=status.HTTP_200_OK)
@OpenTelemetry.fastApiTraceOTel
async def revoke(*, _=Depends(CustomHttpBearer()),
                 subcontractors_id: str = Path(...,
                                               description='Subcontractor id that is used in order to assign a oraganization'),
                 oraganization_id: str = Body(..., description='Oraganization id that is need to be assigned',
                                              embed=True), ):
    reqId = str(uuid4())
    producer = AppDi.instance.get(SimpleProducer)
    from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
    producer.produce(
        obj=ProjectCommand(id=reqId, name=CommandConstant.REVOKE_ASSIGNMENT_SUBCONTRACTOR_TO_ORGANIZATION.value,
                           metadata=json.dumps({"token": Client.token}),
                           data=json.dumps({'id': subcontractors_id,
                                            'org_id': oraganization_id}),
                           external=[]),
        schema=ProjectCommand.get_schema())
    return {"request_id": reqId}
