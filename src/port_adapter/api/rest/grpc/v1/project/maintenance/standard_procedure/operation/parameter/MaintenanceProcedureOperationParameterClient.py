"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.operation.parameter.StandardMaintenanceProcedureOperationParameter import (
    StandardMaintenanceProcedureOperationParameterDescriptor,
)
from src.port_adapter.api.rest.model.response.v1.project.maintenance.standard_procedure.operation.parameter.StandardMaintenanceProcedureOperationParameters import (
    StandardMaintenanceProcedureOperationParameters,
)
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_parameter_app_service_pb2 import (
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersResponse,
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersRequest,
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdRequest,
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdResponse,
    StandardMaintenanceProcedureOperationParameterAppService_newIdRequest,
    StandardMaintenanceProcedureOperationParameterAppService_newIdResponse,
)
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_parameter_app_service_pb2_grpc import (
    StandardMaintenanceProcedureOperationParameterAppServiceStub,
)
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_parameter_app_service_pb2 import (
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdRequest,
)
from src.resource.proto._generated.project.standard_maintenance_procedure_operation_parameter_app_service_pb2 import (
    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdResponse,
)


class StandardMaintenanceProcedureOperationParameterClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_PROJECT_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardMaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                request = (
                    StandardMaintenanceProcedureOperationParameterAppService_newIdRequest()
                )
                response: StandardMaintenanceProcedureOperationParameterAppService_newIdResponse = stub.new_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardMaintenanceProcedureOperationParameterClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureOperationParameters(
        self, resultFrom: int = 0, resultSize: int = 10, orders: List[dict] = None
    ) -> StandardMaintenanceProcedureOperationParameters:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardMaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__}] - grpc call to retrieve standardMaintenanceProcedureOperationParameters from server {self._server}:{self._port}"
                )
                request = StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersRequest(
                    result_from=resultFrom, result_size=resultSize
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersResponse = stub.standard_maintenance_procedure_operation_parameters.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__}] - grpc response: {response}"
                )

                return StandardMaintenanceProcedureOperationParameters(
                    standard_maintenance_procedure_operation_parameters=[
                        self._descriptorByObject(
                            obj=standardMaintenanceProcedureOperationParameter
                        )
                        for standardMaintenanceProcedureOperationParameter in response[
                            0
                        ].standard_maintenance_procedure_operation_parameters
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureOperationParameterById(
        self, id
    ) -> StandardMaintenanceProcedureOperationParameterDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardMaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameterById.__qualname__}] - grpc call to retrieve standardMaintenanceProcedureOperationParameter with standardMaintenanceProcedureOperationParameterId: {id} from server {self._server}:{self._port}"
                )
                response: StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdResponse = stub.standard_maintenance_procedure_operation_parameter_by_id.with_call(
                    StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdRequest(
                        id=id
                    ),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameterById.__qualname__}] - grpc response: {response}"
                )
                standardMaintenanceProcedureOperationParameter = response[
                    0
                ].standard_maintenance_procedure_operation_parameter
                return self._descriptorByObject(
                    obj=standardMaintenanceProcedureOperationParameter
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationId(
        self,
        standardMaintenanceProcedureOperationId: str = None,
        resultFrom: int = 0,
        resultSize: int = 10,
        orders: List[dict] = None,
    ) -> StandardMaintenanceProcedureOperationParameters:
        orders = [] if orders is None else orders
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = StandardMaintenanceProcedureOperationParameterAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__}] - grpc call to retrieve standardMaintenanceProcedureOperationParameters from server {self._server}:{self._port}"
                )
                request = StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdRequest(
                    standard_maintenance_procedure_operation_id=standardMaintenanceProcedureOperationId,
                    result_from=resultFrom,
                    result_size=resultSize,
                )
                [
                    request.orders.add(order_by=o["orderBy"], direction=o["direction"])
                    for o in orders
                ]
                response: StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdResponse = stub.standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParameters.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{StandardMaintenanceProcedureOperationParameterClient.standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationId.__qualname__}] - grpc response: {response}"
                )

                return StandardMaintenanceProcedureOperationParameters(
                    standard_maintenance_procedure_operation_parameters=[
                        self._descriptorByObject(
                            obj=standardMaintenanceProcedureOperationParameter
                        )
                        for standardMaintenanceProcedureOperationParameter in response[
                            0
                        ].standard_maintenance_procedure_operation_parameters
                    ],
                    total_item_count=response[0].total_item_count,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(
        self, obj: Any
    ) -> StandardMaintenanceProcedureOperationParameterDescriptor:
        return StandardMaintenanceProcedureOperationParameterDescriptor(
            id=obj.id,
            name=obj.name,
            unit_id=obj.unit_id,
            standard_maintenance_procedure_operation_id=obj.standard_maintenance_procedure_operation_id,
            min_value=float(obj.min_value),
            max_value=float(obj.max_value),
        )
