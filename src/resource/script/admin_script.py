"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import sys

sys.path.append("../../../")

import os

import click
from confluent_kafka.avro import CachedSchemaRegistryClient
from confluent_kafka.admin import AdminClient, NewTopic

from src.port_adapter.messaging.common.model.ApiCommand import ApiCommand
from src.port_adapter.messaging.common.model.ApiResponse import ApiResponse


@click.group()
def cli():
    pass


@cli.command(help='Initialize kafka topics and schema registries')
def init_kafka_topics_and_schemas():
    # Create topics
    topics = ['cafm.api.cmd', 'cafm.api.rsp']
    newTopics = [NewTopic(topic, num_partitions=int(os.getenv('KAFKA_PARTITIONS_COUNT_PER_TOPIC', 1)), replication_factor=1) for topic in topics]
    admin = AdminClient({'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', '')})
    fs = admin.create_topics(newTopics)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            click.echo(click.style("Topic {} created".format(topic), fg='green'))
        except Exception as e:
            click.echo(click.style(f'Failed to create topic {topic}: {e}', fg='red'))

    # Create schemas
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    schemas = [{'name': 'cafm.api.Command', 'schema': ApiCommand.get_schema()},
               {'name': 'cafm.api.Response', 'schema': ApiResponse.get_schema()}]
    [c.register(schema['name'], schema['schema']) for schema in schemas]


@cli.command(help='Drop kafka topics and schema registries')
def drop_kafka_topics_and_schemas():
    # Delete topics
    topics = ['cafm.api.cmd', 'cafm.api.rsp']
    admin = AdminClient({'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', '')})
    fs = admin.delete_topics(topics, operation_timeout=30)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            click.echo(click.style("Topic {} deleted".format(topic), fg='green'))
        except Exception as e:
            click.echo(click.style(f'Failed to delete topic {topic}: {e}', fg='red'))

    # Delete schemas
    schemas = ['cafm.api.Command', 'cafm.api.Response']
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    [c.delete_subject(schema) for schema in schemas]


if __name__ == '__main__':
    cli()
