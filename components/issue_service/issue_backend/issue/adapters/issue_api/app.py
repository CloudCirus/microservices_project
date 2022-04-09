from classic.http_api import App

from . import controllers
from issue.application import services


def create_app(issue: services.IssueService) -> App:
    app = App(prefix="/api")
    app.register(controllers.Issues(service=issue))
    return app
