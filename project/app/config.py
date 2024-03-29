import logging
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None


@lru_cache
def get_settings() -> BaseSettings:
    log.info("Loadig config setting from the environment...")
    return Settings()
