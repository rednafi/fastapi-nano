import os

from dotenv import load_dotenv

load_dotenv("./.env")

ENV_STATE = os.environ["ENV_STATE"]

# Base configs.
HOST = os.environ["HOST"]


# Prod configs.
if ENV_STATE == "prod":
    API_USERNAME = os.environ["PROD_API_USERNAME"]
    API_PASSWORD = os.environ["PROD_API_PASSWORD"]


# Dev configs.
else:
    API_USERNAME = os.environ["DEV_API_USERNAME"]
    API_PASSWORD = os.environ["DEV_API_PASSWORD"]


# Auth configs.
API_SECRET_KEY = os.environ["API_SECRET_KEY"]
API_ALGORITHM = os.environ["API_ALGORITHM"]
API_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.environ["API_ACCESS_TOKEN_EXPIRE_MINUTES"]
)  # infinity
