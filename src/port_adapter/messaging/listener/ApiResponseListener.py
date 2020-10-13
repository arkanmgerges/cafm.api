"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import os
import signal

import redis
from confluent_kafka.cimpl import KafkaError
from redis.client import Redis

import src.port_adapter.AppDi as AppDi
from src.port_adapter.messaging.common.Consumer import Consumer
from src.port_adapter.messaging.common.ConsumerOffsetReset import ConsumerOffsetReset
from src.port_adapter.messaging.common.TransactionalProducer import TransactionalProducer
from src.resource.logging.logger import logger


class ApiResponseListener:
    def __init__(self):
        self._handlers = []
        self._creatorServiceName = os.getenv('CAFM_API_SERVICE_NAME', 'cafm.api')
        self._topicResponseTtl = os.getenv('CAFM_API_REDIS_RSP_TOPIC_TTL_IN_SECONDS', 3600)
        signal.signal(signal.SIGINT, self.interruptExecution)
        signal.signal(signal.SIGTERM, self.interruptExecution)

        try:
            self._cache: Redis = redis.Redis(host=os.getenv('CAFM_API_REDIS_HOST', 'localhost'),
                                             port=os.getenv('CAFM_API_REDIS_PORT', 6379))
            self._cacheResponseKeyPrefix = os.getenv('CAFM_API_REDIS_RSP_KEY_PREFIX', 'cafm.api.rsp.')
        except Exception as e:
            raise Exception(
                f'[{ApiResponseListener.__init__.__qualname__}] Could not connect to the redis, message: {e}')

    def interruptExecution(self, _signum, _frame):
        raise SystemExit()

    def run(self):
        consumer: Consumer = AppDi.Builder.buildConsumer(
            groupId=os.getenv('CAFM_API_CONSUMER_GROUP_API_RSP_NAME', 'cafm.api.consumer-group.rsp'),
            autoCommit=False, partitionEof=True,
            autoOffsetReset=ConsumerOffsetReset.earliest.name)

        # Subscribe
        consumer.subscribe([os.getenv('CAFM_API_RESPONSE_TOPIC', 'cafm.api.rsp')])

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
                            f'[{ApiResponseListener.run.__qualname__}] - msg reached partition eof: {msg.error()}')
                    else:
                        logger.error(msg.error())
                else:
                    # Proper message
                    logger.info(
                        f'[{ApiResponseListener.run.__qualname__}] - topic: {msg.topic()}, partition: {msg.partition()}, offset: {msg.offset()} with key: {str(msg.key())}')
                    logger.info(f'value: {msg.value()}')

                    try:
                        msgData = msg.value()

                        logger.debug(f'[{ApiResponseListener.run.__qualname__}] - setting to redis msgData: {msgData}')
                        self._cache.setex(f'{self._cacheResponseKeyPrefix}{msgData["commandId"]}',
                                          self._topicResponseTtl,
                                          json.dumps({
                                              "commandId": msgData['commandId'],
                                              "commandName": msgData['commandName'],
                                              "metadata": json.loads(msgData['metadata']),
                                              "data": json.loads(msgData['data']),
                                              "creatorServiceName": msgData['creatorServiceName'],
                                              "success": msgData['success']
                                          }).encode('utf-8'))

                        if not (self._cache.exists(f'{self._cacheResponseKeyPrefix}{msgData["commandId"]}')):
                            raise Exception(
                                f'[{ApiResponseListener.run.__qualname__}] - Redis key id: {msgData["commandId"]} does not exist after setting it')
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
            logger.info(f'[{ApiResponseListener.run.__qualname__}] - Aborted by user')
        except SystemExit:
            logger.info(f'[{ApiResponseListener.run.__qualname__}] - Shutting down the process')
        finally:
            producer.abortTransaction()
            # Close down consumer to commit final offsets.
            consumer.close()


ApiResponseListener().run()