import os


class Settings:
    _user = os.getenv("RABBITMQ_USER", "admin")
    _password = os.getenv("RABBITMQ_PASSWORD", "password")
    _host = os.getenv("RABBITMQ_HOST", "localhost")
    _port = os.getenv("RABBITMQ_PORT", "5672")

    BROKER_URL = f"amqp://{_user}:{_password}@{_host}:{_port}"
