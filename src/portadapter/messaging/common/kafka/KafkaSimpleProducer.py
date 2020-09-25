import os
from uuid import uuid4

from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import record_subject_name_strategy
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer

from src.portadapter.messaging.common.SimpleProducer import SimpleProducer
from src.portadapter.messaging.common.kafka.KafkaDeliveryReport import KafkaDeliveryReport
from src.portadapter.messaging.common.model.MessageBase import MessageBase

MESSAGE_SCHEMA_REGISTRY_URL = os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')


class KafkaSimpleProducer(SimpleProducer):
    def __init__(self, schemaRegistry=None):
        self._schemaRegistry = schemaRegistry
        self._deliveryReport = KafkaDeliveryReport.deliveryReport

    def produce(self, obj: MessageBase, schema: dict):
        avroSerializer = AvroSerializer(
            str(schema),
            self._schemaRegistry,
            obj.toMap,
            conf={'subject.name.strategy': record_subject_name_strategy,
                  'auto.register.schemas': False}
        )
        producerConf = {'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', ''),
                        'key.serializer': StringSerializer('utf_8'),
                        'value.serializer': avroSerializer}
        producer = SerializingProducer(producerConf)
        producer.poll(0.0)
        producer.produce(topic=obj.topic(), key=str(uuid4()), value=obj,
                         on_delivery=self._deliveryReport)
        producer.flush()

