"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import List

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.RealmApplicationService import RealmApplicationService
from src.domain_model.TokenService import TokenService
from src.domain_model.realm.Realm import Realm
from src.domain_model.resource.exception.RealmDoesNotExistException import RealmDoesNotExistException
from src.resource.logging.logger import logger
from src.resource.proto._generated.realm_app_service_pb2 import RealmAppService_realmByNameResponse, \
    RealmAppService_realmsResponse, RealmAppService_realmByIdResponse
from src.resource.proto._generated.realm_app_service_pb2_grpc import RealmAppServiceServicer


class RealmAppServiceListener(RealmAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()
        
    def __str__(self):
        return self.__class__.__name__

    def realmByName(self, request, context):
        try:
            realmAppService: RealmApplicationService = AppDi.instance.get(RealmApplicationService)
            realm: Realm = realmAppService.realmByName(name=request.name)
            response = RealmAppService_realmByNameResponse()
            response.realm.id = realm.id()
            response.realm.name = realm.name()
            return response
        except RealmDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Realm does not exist')
            return RealmAppService_realmByNameResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.RealmResponse()
        
    def realms(self, request, context):
        try:
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize > 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            ownedRealms = claims['realm'] if 'realm' in claims else []
            logger.debug(f'[{RealmAppServiceListener.realms.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t ownedRealms {ownedRealms}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}')
            realmAppService: RealmApplicationService = AppDi.instance.get(RealmApplicationService)

            realms: List[Realm] = realmAppService.realms(ownedRealms=ownedRealms, resultFrom=request.resultFrom,
                                                     resultSize=resultSize)
            response = RealmAppService_realmsResponse()
            for realm in realms:
                response.realms.add(id=realm.id(), name=realm.name())
            logger.debug(f'[{RealmAppServiceListener.realms.__qualname__}] - response: {response}')
            return RealmAppService_realmsResponse(realms=response.realms)
        except RealmDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No realms found')
            return RealmAppService_realmByNameResponse()

    def realmById(self, request, context):
        try:
            realmAppService: RealmApplicationService = AppDi.instance.get(RealmApplicationService)
            realm: Realm = realmAppService.realmById(id=request.id)
            logger.debug(f'[{RealmAppServiceListener.realmById.__qualname__}] - response: {realm}')
            response = RealmAppService_realmByIdResponse()
            response.realm.id = realm.id()
            response.realm.name = realm.name()
            return response
        except RealmDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Realm does not exist')
            return RealmAppService_realmByIdResponse()