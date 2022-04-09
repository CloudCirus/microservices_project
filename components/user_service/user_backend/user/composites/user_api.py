from kombu import Connection
from sqlalchemy import create_engine

from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext

from user.adapters import database, message_bus, user_api
from user.application import services


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)

    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    user_repo = database.repositories.UserRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
        messages_params={
            "create_issue": {
                "exchange": "ApiEx",
                "routing_key": "issue",
            }
        },
    )


class Application:
    user = services.UserService(
        user_repo=DB.user_repo,
        publisher=MessageBus.publisher
    )


class Aspects:
    services.join_points.join(MessageBus.publisher, DB.context)
    user_api.join_points.join(DB.context)


app = user_api.create_app(user=Application.user)
