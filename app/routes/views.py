from fastapi import APIRouter
from app.api_a.mainmod import func_main as func_main_a
from app.api_b.mainmod import func_main as func_main_b

router = APIRouter()


@router.get("/api-a/{num}", tags=["users"])
async def views_a(num: int):
    return func_main_a(num)


@router.get("/api-b/{num}", tags=["users"])
async def views_a(num: int):
    return func_main_b(num)
