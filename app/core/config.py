from dataclasses import dataclass
from os import environ
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


@dataclass
class BaseConfig:
    """Common configurations."""

    HOST: Optional[str] = environ.get("HOST")

    @staticmethod
    def typecast(variable, target_type):
        if variable is not None:
            return target_type(variable)


@dataclass
class DevConfig(BaseConfig):
    """Development configurations."""

    API_USERNAME: Optional[str] = environ.get("DEV.API_USERNAME")
    API_PASSWORD: Optional[str] = environ.get("DEV.API_PASSWORD")


@dataclass
class ProdConfig(BaseConfig):
    """Production configurations."""

    API_USERNAME: Optional[str] = environ.get("PROD.API_USERNAME")
    API_PASSWORD: Optional[str] = environ.get("PROD.API_PASSWORD")


class Config:
    """Configuration factory class."""

    def __init__(self, env: Optional[str]):
        self.env = env

    def __call__(self):
        if self.env == "dev":
            return DevConfig()

        elif self.env == "prod":
            return ProdConfig()


config = Config(env=environ.get("ENVIRONMENT"))()
