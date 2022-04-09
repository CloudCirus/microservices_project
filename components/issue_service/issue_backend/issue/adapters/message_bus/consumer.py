from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from issue.application import services
from .scheme import broker_scheme


def create_consumer(
        connection: Connection, issue: services.IssueService
) -> KombuConsumer:
    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        issue.create_issue_from_rabbitmq,
        "IssueQ",
    )

    return consumer
