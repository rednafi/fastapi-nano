import secrets
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.apis.{{cookiecutter.api_a}}.mainmod import main_func as main_func_a
from app.apis.{{cookiecutter.api_b}}.mainmod import main_func as main_func_b
from app.core.config import config

router = APIRouter()
security = HTTPBasic()


def authorize(credentials: HTTPBasicCredentials = Depends(security)) -> bool:
    correct_username = secrets.compare_digest(credentials.username, config.API_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, config.API_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True


@router.get("/{{cookiecutter.api_a}}/{num}", tags=["api_a"])
async def views(num: int, auth=Depends(authorize)) -> Dict[str, int]:
    if auth is True:
        return main_func_a(num)


@router.get("/{{cookiecutter.api_b}}/{num}", tags=["api_b"])
async def views(num: int, auth=Depends(authorize)) -> Dict[str, int]:
    if auth is True:
        return main_func_b(num)
