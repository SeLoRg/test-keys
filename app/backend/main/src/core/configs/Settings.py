from app.backend.main.src.core.configs.Postgres import Postgres
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    postgres: Postgres = Postgres()

    model_config = SettingsConfigDict(extra="ignore")


settings = Settings()
