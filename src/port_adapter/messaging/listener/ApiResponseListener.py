"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
import signal
import threading

import redis
from confluent_kafka.cimpl import KafkaError
from redis.client import Redis

import src.port_adapter.AppDi as AppDi
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.TransactionalProducer import (
    TransactionalProducer,
)
from src.port_adapter.messaging.listener.CacheType import CacheType
from src.resource.logging.LogProcessor import LogProcessor
from src.resource.logging.logger import logger


class ApiResponseListener:
    def __init__(self):
        self._handlers = []
        self._creatorServiceName = os.getenv("CAFM_API_SERVICE_NAME", "cafm.api")
        self._topicResponseTtl = os.getenv(
            "CAFM_API_REDIS_RSP_TOPIC_TTL_IN_SECONDS", 3600
        )
        signal.signal(signal.SIGINT, self.interruptExecution)
        signal.signal(signal.SIGTERM, self.interruptExecution)

        try:
            self._cache: Redis = redis.Redis(
                host=os.getenv("CAFM_API_REDIS_HOST", "localhost"),
                port=os.getenv("CAFM_API_REDIS_PORT", 6379),
            )
            self._cacheResponseKeyPrefix = os.getenv(
                "CAFM_API_REDIS_RSP_KEY_PREFIX", "cafm.api.rsp"
            )
        except Exception as e:
            raise Exception(
                f"[{ApiResponseListener.__init__.__qualname__}] Could not connect to the redis, message: {e}"
            )

    def interruptExecution(self, _signum, _frame):
        raise SystemExit()

    def run(self):
        consumer: Consumer = AppDi.Builder.buildConsumer(
            groupId=os.getenv(
                "CAFM_API_CONSUMER_GROUP_API_RSP_NAME", "cafm.api.consumer-group.rsp"
            ),
            autoCommit=False,
            partitionEof=True,
            autoOffsetReset=ConsumerOffsetReset.earliest.name,
        )

        # Subscribe
        consumer.subscribe([os.getenv("CAFM_API_RESPONSE_TOPIC", "cafm.api.rsp")])

        # Producer
        producer: TransactionalProducer = AppDi.instance.get(TransactionalProducer)
        producer.initTransaction()
        producer.beginTransaction()

        try:
            while True:
                try:
                    msg = consumer.poll(timeout=1.0)
                    if msg is None:
                        continue
                except Exception as _e:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        logger.info(
                            f"[{ApiResponseListener.run.__qualname__}] - msg reached partition eof: {msg.error()}"
                        )
                    else:
                        logger.error(msg.error())
                else:
                    # Proper message
                    logger.info(
                        f"[{ApiResponseListener.run.__qualname__}] - topic: {msg.topic()}, partition: {msg.partition()}, offset: {msg.offset()} with key: {str(msg.key())}"
                    )
                    logger.info(f"value: {msg.value()}")

                    try:
                        msgData = msg.value()
                        logger.debug(
                            f"[{ApiResponseListener.run.__qualname__}] - setting to redis msgData: {msgData}"
                        )
                        cacheKey = (
                            f'{self._cacheResponseKeyPrefix}:{msgData["command_id"]}'
                        )
                        splitCommand = msgData["command_id"].split(":")
                        if len(splitCommand) == 1:
                            self._cache.setex(
                                cacheKey,
                                self._topicResponseTtl,
                                json.dumps(
                                    {
                                        "command_id": msgData["command_id"],
                                        "command_name": msgData["command_name"],
                                        "metadata": json.loads(msgData["metadata"]),
                                        "data": json.loads(msgData["data"]),
                                        "creator_service_name": msgData[
                                            "creator_service_name"
                                        ],
                                        "success": msgData["success"],
                                    }
                                ).encode("utf-8"),
                            )
                            if not (self._cache.exists(cacheKey)):
                                raise Exception(
                                    f'[{ApiResponseListener.run.__qualname__}] - Redis key id: {msgData["command_id"]} does not exist after setting it'
                                )
                        else:
                            cacheType = CacheType.valueToEnum(splitCommand[0])
                            if cacheType == CacheType.LIST:
                                self._cache.lpush(
                                    cacheKey,
                                    json.dumps(
                                        {
                                            "command_id": msgData["command_id"],
                                            "command_name": msgData["command_name"],
                                            "metadata": json.loads(msgData["metadata"]),
                                            "data": json.loads(msgData["data"]),
                                            "creator_service_name": msgData[
                                                "creator_service_name"
                                            ],
                                            "success": msgData["success"],
                                        }
                                    ).encode("utf-8"),
                                )
                                self._cache.expire(cacheKey, self._topicResponseTtl)
                                if not (self._cache.exists(cacheKey)):
                                    raise Exception(
                                        f'[{ApiResponseListener.run.__qualname__}] - Redis key id: {msgData["command_id"]} does not exist after setting it'
                                    )
                            else:
                                raise Exception(
                                    f'[{ApiResponseListener.run.__qualname__}] - Redis unknown key type: {msgData["command_id"]}'
                                )

                        # Send the consumer's position to transaction to commit
                        # them along with the transaction, committing both
                        # input and outputs in the same transaction is what provides EOS.
                        producer.sendOffsetsToTransaction(consumer)
                        producer.commitTransaction()

                        producer.beginTransaction()
                    except Exception as e:
                        logger.error(e)

                # sleep(3)
        except KeyboardInterrupt:
            logger.info(f"[{ApiResponseListener.run.__qualname__}] - Aborted by user")
        except SystemExit:
            logger.info(
                f"[{ApiResponseListener.run.__qualname__}] - Shutting down the process"
            )
        finally:
            producer.abortTransaction()
            # Close down consumer to commit final offsets.
            consumer.close()

# region Logger
import src.resource.Di as Di
logProcessor = Di.instance.get(LogProcessor)
thread = threading.Thread(target=logProcessor.start)
thread.start()
# endregion
ApiResponseListener().run()
