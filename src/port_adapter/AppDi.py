from uuid import uuid4

from injector import Module, Injector, singleton, provider

from src.application.AuthenticationApplicationService import (
    AuthenticationApplicationService,
)
from src.domain_model.authentication.AuthenticationRepository import (
    AuthenticationRepository,
)
from src.domain_model.authentication.AuthenticationService import AuthenticationService
from src.domain_model.OrderService import OrderService
from src.port_adapter.api.rest.cache.RedisCache import RedisCache
from src.port_adapter.api.rest.grpc.v1.identity.auth.AuthClient import AuthClient
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.SimpleProducer import SimpleProducer
from src.port_adapter.messaging.common.TransactionalProducer import (
    TransactionalProducer,
)
from src.port_adapter.messaging.common.kafka.KafkaConsumer import KafkaConsumer
from src.port_adapter.messaging.common.kafka.KafkaProducer import KafkaProducer
from injector import ClassAssistedBuilder

from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry


class AppDi(Module):
    """
    Dependency injection module of the app

    """

    @singleton
    @provider
    def provideSimpleProducer(self) -> SimpleProducer:
        return KafkaProducer.simpleProducer()

    @singleton
    @provider
    def provideTransactionalProducer(self) -> TransactionalProducer:
        return KafkaProducer.transactionalProducer()

    @singleton
    @provider
    def provideConsumer(
        self,
        groupId: str = uuid4(),
        autoCommit: bool = False,
        partitionEof: bool = True,
        autoOffsetReset: str = ConsumerOffsetReset.latest.name,
    ) -> Consumer:
        return KafkaConsumer(
            groupId=groupId,
            autoCommit=autoCommit,
            partitionEof=partitionEof,
            autoOffsetReset=autoOffsetReset,
        )

    # region Repository
    @singleton
    @provider
    def provideAuthenticationRepository(self) -> AuthenticationRepository:
        from src.port_adapter.domain_model.authentication.AuthenticationRepositoryImpl import (
            AuthenticationRepositoryImpl,
        )

        return AuthenticationRepositoryImpl()

    # endregion

    # region Application service
    @singleton
    @provider
    def provideAuthenticationApplicationService(
        self,
    ) -> AuthenticationApplicationService:
        return AuthenticationApplicationService(
            self.__injector__.get(AuthenticationService)
        )

    # endregion

    # region Domain Service
    @singleton
    @provider
    def provideAuthenticationService(self) -> AuthenticationService:
        return AuthenticationService(self.__injector__.get(AuthenticationRepository))

    @singleton
    @provider
    def provideOrderService(self) -> OrderService:
        return OrderService()

    # endregion

    # region Resource
    @singleton
    @provider
    def provideOpenTelemetry(self) -> OpenTelemetry:
        return OpenTelemetry()

    # endregion

    # region Grpc
    @singleton
    @provider
    def provideAuthClient(self) -> AuthClient:
        return AuthClient()

    # endregion

    @singleton
    @provider
    def provideRedisClient(self) -> RedisCache:
        return RedisCache()


class Builder:
    @classmethod
    def buildConsumer(
        cls,
        groupId: str = uuid4(),
        autoCommit: bool = False,
        partitionEof: bool = True,
        autoOffsetReset: str = ConsumerOffsetReset.earliest.name,
    ) -> Consumer:
        builder = instance.get(ClassAssistedBuilder[KafkaConsumer])
        return builder.build(
            groupId=groupId,
            autoCommit=autoCommit,
            partitionEof=partitionEof,
            autoOffsetReset=autoOffsetReset,
        )


instance = Injector([AppDi])
