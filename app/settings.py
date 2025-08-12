from dotenv import dotenv_values
from pydantic_settings import BaseSettings, SettingsConfigDict


env = dotenv_values()


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str


class RedisSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    REDIS_HOST: str
    REDIS_PORT: int


db_settings = DatabaseSettings()
redis_settings = RedisSettings()
