from classic.http_api import App

from . import controllers
from book.application import services


def create_app(book: services.BookService) -> App:
    app = App(prefix="/api")
    app.register(controllers.Books(service=book))
    return app
