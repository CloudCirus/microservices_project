from classic.http_api import App

from book.application import services
from . import controllers


def create_app(book: services.BookService) -> App:
    app = App(prefix="/api")
    app.register(controllers.Books(service=book))
    return app
