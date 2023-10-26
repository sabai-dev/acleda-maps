from fastapi import APIRouter
from .places import place_router

places_router = APIRouter()

places_router.include_router(place_router ,tags=["Places"])

__all__ = ["places_router"]