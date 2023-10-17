from fastapi import APIRouter
from .merchants import merchant_router

v1_router = APIRouter()

# Registering individual routers from the endpoints
v1_router.include_router(merchant_router, prefix="/merchants", tags=["merchants"])
# v1_router.include_router(tasks_router, prefix="/tasks")
# v1_router.include_router(users_router, prefix="/users")

__all__ = ["v1_router"]