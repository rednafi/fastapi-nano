import os

from dotenv import load_dotenv

load_dotenv()

api_username = os.environ.get("API_USERNAME")
api_password = os.environ.get("API_PASSWORD")
