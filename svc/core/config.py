from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parent.parent  # svc/
BASE_DIR = ROOT.parent  # ./


class Settings(BaseSettings):
    api_username: str
    api_password: str
    api_secret_key: str
    api_algorithm: str = "HS256"
    api_access_token_expire_minutes: int
    cors_allow_origins: list[str] = [
        "http://localhost",
        "http://localhost:5002",
        "http://127.0.0.1",
        "http://127.0.0.1:5002",
    ]

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
