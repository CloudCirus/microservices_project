import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    _user = os.getenv("DB_USER", "admin")
    _password = os.getenv("DB_PASSWORD", "password")
    _host = os.getenv("DB_HOST", "localhost")
    _port = os.getenv("DB_PORT", "5432")
    _database = os.getenv("DB", "books")

    DB_URL: str = f"postgresql+psycopg2://{_user}:{_password}@{_host}:{_port}/{_database}"
