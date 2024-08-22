"""
Настройки проекта.
"""

from dotenv import load_dotenv
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ApplicationSettings(BaseSettings):
    """
    Настройки для работы с сервером приложения.

    :cvar host: Host сервера.
    :cvar port: Port сервера.
    """
    model_config = SettingsConfigDict(env_prefix='app_')

    host: str
    port: int


class DatabaseSettings(BaseSettings):
    """
    Настройки для работы с базой данных.

    :cvar postgres_url: Url подключения к PostgreSQL.
    """
    postgres_url: PostgresDsn
