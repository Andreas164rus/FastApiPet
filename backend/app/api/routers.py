from fastapi import APIRouter

from app.api.endpoints import (
    user_router, task_router
)

main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(task_router, prefix='/task', tags=['task'])
