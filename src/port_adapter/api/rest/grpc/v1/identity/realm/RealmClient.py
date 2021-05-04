"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.rest.grpc.Client import Client
from src.port_adapter.api.rest.model.response.v1.identity.Realm import RealmDescriptor
from src.port_adapter.api.rest.model.response.v1.identity.Realms import Realms
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.identity.realm_app_service_pb2 import (
    RealmAppService_realmsResponse,
    RealmAppService_realmsRequest,
    RealmAppService_realmByIdRequest,
    RealmAppService_realmByIdResponse,
    RealmAppService_newIdRequest,
    RealmAppService_newIdResponse,
)
from src.resource.proto._generated.identity.realm_app_service_pb2_grpc import (
    RealmAppServiceStub,
)


class RealmClient(Client):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    @OpenTelemetry.grpcTraceOTel
    def newId(self) -> str:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RealmClient.newId.__qualname__}] - grpc call to retrieve realms from server {self._server}:{self._port}"
                )
                request = RealmAppService_newIdRequest()
                response: RealmAppService_newIdResponse = stub.newId.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RealmClient.newId.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RealmClient.newId.__qualname__}] - grpc response: {response}"
                )
                return response[0].id
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def realms(
        self, resultFrom: int = 0, resultSize: int = 10, order: List[dict] = None
    ) -> Realms:
        order = [] if order is None else order
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RealmClient.realms.__qualname__}] - grpc call to retrieve realms from server {self._server}:{self._port}"
                )
                request = RealmAppService_realmsRequest(
                    resultFrom=resultFrom, resultSize=resultSize
                )
                [
                    request.order.add(orderBy=o["orderBy"], direction=o["direction"])
                    for o in order
                ]
                response: RealmAppService_realmsResponse = stub.realms.with_call(
                    request,
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RealmClient.realms.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RealmClient.realms.__qualname__}] - grpc response: {response}"
                )

                return Realms(
                    realms=[
                        self._descriptorByObject(obj=realm)
                        for realm in response[0].realms
                    ],
                    total_item_count=response[0].totalItemCount,
                )
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    @OpenTelemetry.grpcTraceOTel
    def realmById(self, realmId) -> RealmDescriptor:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                logger.debug(
                    f"[{RealmClient.realmById.__qualname__}] - grpc call to retrieve realm with realmId: {realmId} from server {self._server}:{self._port}"
                )
                response: RealmAppService_realmByIdResponse = stub.realmById.with_call(
                    RealmAppService_realmByIdRequest(id=realmId),
                    metadata=(
                        ("token", self.token),
                        (
                            "opentel",
                            AppDi.instance.get(OpenTelemetry).serializedContext(
                                RealmClient.realmById.__qualname__
                            ),
                        ),
                    ),
                )
                logger.debug(
                    f"[{RealmClient.realmById.__qualname__}] - grpc response: {response}"
                )

                return self._descriptorByObject(obj=response[0].realm)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def _descriptorByObject(self, obj: Any) -> RealmDescriptor:
        return RealmDescriptor(id=obj.id, name=obj.name, realm_type=obj.realmType)
