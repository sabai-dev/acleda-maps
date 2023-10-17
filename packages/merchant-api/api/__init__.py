from fastapi import APIRouter
from .api_v1 import v1_router as api_v1_router  # Importing the router from api_v1

router = APIRouter()
router.include_router(api_v1_router, prefix="/v1")  # Registering the v1 router with a "/v1" prefix

__all__ = ["router"]