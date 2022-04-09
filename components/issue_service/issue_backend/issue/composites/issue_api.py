from threading import Thread

from sqlalchemy import create_engine
from kombu import Connection

from classic.sql_storage import TransactionContext

from issue.adapters import database, issue_api, message_bus
from issue.application import services


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)

    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issue_repo = database.repositories.IssueRepo(context=context)


class Application:
    issue = services.IssueService(issue_repo=DB.issue_repo)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)


class MessageBusConsumer:
    consumer = message_bus.create_consumer(
        connection=MessageBus.connection,
        issue=Application.issue,
    )

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    issue_api.join_points.join(DB.context)


app = issue_api.create_app(issue=Application.issue)

MessageBusConsumer.declare_scheme()

consumer = Thread(target=MessageBusConsumer.consumer.run, daemon=True)
consumer.start()
