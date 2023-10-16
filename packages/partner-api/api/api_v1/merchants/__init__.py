from fastapi import APIRouter
from .merchants import merchant

merchant_router = APIRouter()

merchant_router.include_router(merchant, tags=["Merchants"])

__all__ = ["merchant_router"]