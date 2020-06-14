from typing import Optional

from pydantic import BaseSettings, Field


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # This variable will be loaded from the .env file. However, if there is a
    # shell environment variable having the same name, that will take precedence.

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configurations."""

    API_USERNAME: Optional[str] = Field(None, env="DEV_API_USERNAME")
    API_PASSWORD: Optional[str] = Field(None, env="DEV_API_PASSWORD")


class ProdConfig(GlobalConfig):
    """Production configurations."""

    API_USERNAME: Optional[str] = Field(None, env="PROD_API_USERNAME")
    API_PASSWORD: Optional[str] = Field(None, env="PROD_API_PASSWORD")


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


config = FactoryConfig(GlobalConfig().ENV_STATE)()
# print(config.__repr__())
