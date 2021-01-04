"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import sys
#
# sys.path.append("../../../")
# sys.path.append("/app")

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
    requiredTopics = ['cafm.api.cmd', 'cafm.api.rsp']
    click.echo(click.style(f"Initializing kafka topics and schema registries", fg='green'))
    newTopics = []
    admin = AdminClient({'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', '')})
    installedTopics = admin.list_topics().topics.keys()

    for requiredTopic in requiredTopics:
        if requiredTopic not in installedTopics:
            newTopics.append(NewTopic(requiredTopic, num_partitions=int(os.getenv('KAFKA_PARTITIONS_COUNT_PER_TOPIC', 1)), replication_factor=1))
    if len(newTopics) > 0:
        fs = admin.create_topics(newTopics)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                click.echo(click.style("Topic {} created".format(topic), fg='green'))
            except Exception as e:
                click.echo(click.style(f'Failed to create topic {topic}: {e}', fg='red'))

    # Create schemas
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    requiredSchemas = [{'name': 'cafm.api.Command', 'schema': ApiCommand.get_schema()},
               {'name': 'cafm.api.Response', 'schema': ApiResponse.get_schema()}]
    newSchemas = []
    for requiredSchema in requiredSchemas:
        click.echo(click.style(f'Verify if schema {requiredSchema["name"]} is available', fg='green'))
        r = c.get_latest_schema(subject=f'{requiredSchema["name"]}')
        if r[0] is None:
            click.echo(click.style(f'Schema {requiredSchema["name"]} will be created', fg='green'))
            newSchemas.append(requiredSchema)
    [c.register(schema['name'], schema['schema']) for schema in newSchemas]


@cli.command(help='Drop kafka topics and schema registries')
def drop_kafka_topics_and_schemas():
    # Delete topics
    topics = ['cafm.api.cmd', 'cafm.api.rsp']
    click.echo(click.style(f"Dropping kafka topics and schema registries", fg='green'))
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
