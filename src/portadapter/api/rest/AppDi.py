from injector import Module, Injector, singleton, provider

from src.portadapter.messaging.Producer import Producer
from src.portadapter.messaging.kafka.KafkaProducer import KafkaProducer


class AppDi(Module):
    """
    Dependency injection module of the app

    """

    # region Application Service
    @singleton
    @provider
    def provideProducer(self) -> Producer:
        return KafkaProducer()


instance = Injector([AppDi])
