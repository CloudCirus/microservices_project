from user.application import services

from . import controllers
from classic.http_api import App


def create_app(user: services.UserService) -> App:
    app = App(prefix="/api")
    app.register(controllers.Users(service=user))
    return app
