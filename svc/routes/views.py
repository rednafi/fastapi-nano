import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from svc.apis.api_a.mainmod import main_func as main_func_a
from svc.apis.api_b.mainmod import main_func as main_func_b
from svc.apis.schemas import RandomNumbers
from svc.core.auth import UserInDB, get_current_user

router = APIRouter()
logger = logging.getLogger("fnano")
CurrentUser = Annotated[UserInDB, Depends(get_current_user)]


@router.get("/")
async def index() -> dict[str, str]:
    return {
        "info": "This is the index page of fastapi-nano. "
        "You probably want to go to 'http://<hostname:port>/docs'.",
    }


@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(
    num: int,
    _auth: CurrentUser,
) -> RandomNumbers:
    result = main_func_a(num)
    logger.info(f"API A: {result}")
    return result


@router.get("/api_b/{num}", tags=["api_b"])
async def view_b(
    num: int,
    _auth: CurrentUser,
) -> RandomNumbers:
    result = main_func_b(num)
    logger.info(f"API B: {result}")
    return result
