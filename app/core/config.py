import os

from dotenv import load_dotenv

load_dotenv("./.env")


API_USERNAME = os.environ["API_USERNAME"]
API_PASSWORD = os.environ["API_PASSWORD"]

# Auth configs.
API_SECRET_KEY = os.environ["API_SECRET_KEY"]
API_ALGORITHM = os.environ["API_ALGORITHM"]
API_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.environ["API_ACCESS_TOKEN_EXPIRE_MINUTES"]
)  # infinity
