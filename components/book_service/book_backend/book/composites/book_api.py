from kombu import Connection
from sqlalchemy import create_engine

from classic.sql_storage import TransactionContext
from classic.messaging_kombu import KombuPublisher

from book.adapters import database, book_api, message_bus
from book.application import services


class Settings:
    db = database.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)

    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    book_repo = database.repositories.BookRepo(context=context)


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
    book = services.BookService(
        book_repo=DB.book_repo,
        publisher=MessageBus.publisher
    )


class Aspects:
    services.join_points.join(MessageBus.publisher, DB.context)
    book_api.join_points.join(DB.context)


app = book_api.create_app(book=Application.book)
