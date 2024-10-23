import os
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Tuple


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class EngineConfig(BaseModel):
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 5


class DBConfig(BaseModel):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int


def get_env_file_paths(*file_names: str) -> Tuple[str, ...]:
    directory = os.path.dirname(os.path.abspath(__file__))
    env_file_paths = tuple(os.path.join(directory, "../../", file_name) for file_name in file_names)
    return env_file_paths


class Settings(BaseSettings):
    db_config: DBConfig
    engine_config: EngineConfig = EngineConfig()
    run_config: RunConfig = RunConfig()
    model_config = SettingsConfigDict(
        env_file=get_env_file_paths(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__"
    )


settings = Settings()


def get_db_url() -> str:
    config: DBConfig = settings.db_config
    return (f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD}@"
            f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}")
