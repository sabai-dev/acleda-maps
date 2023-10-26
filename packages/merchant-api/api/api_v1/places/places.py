from typing import Callable, Optional

from fastapi import APIRouter, Depends, Request, Query
from fastapi.params import Body
from app.controllers import PlaceController
# from app.models.task import TaskPermission
from app.schemas.requests.places import PlaceRequest
from app.schemas.responses.places import PlaceResponse
from core.factory import Factory
from core.fastapi.dependencies.permissions import Permissions

place_router = APIRouter()


# @place.get("/", response_model=list[PlaceResponse])
@place_router.get("/")
async def get_places(
    # merchant_id: str| None=None,
    # query: PlaceRequest = Depends(),
    query: PlaceRequest = Depends(),
    place_controller: PlaceController = Depends(Factory().get_place_controller)
) :
    
    
    return {"name":1}

# @place_router.get("/", response_model=list[PlaceResponse])
# async def get_place_by_name(
#     name: str,
    
# place_controller: PlaceController = Depends(Factory().get_place_controller),
# # #     assert_access: Callable = Depends(Permissions(MerchantPermission.READ)),
# ) -> list[PlaceResponse]:

    
#     places = await place_controller.get_by_place_name(name)
    
#     return places



# @place_router.get("/", response_model=list[PlaceResponse])
# async def get_place_by_lat_lng(
#     lat: float =None,
#     lng: float =None,
#     place_controller: PlaceController = Depends(Factory().get_place_controller),
# ) -> list[PlaceResponse]:
#     places = await place_controller.get_by_place_lat_lng(lat, lng)
#     return places

# @place_router.get("/", response_model=list[PlaceResponse])
# async def get_tasks(
#     request:Request,
#     merchant_id: str=None,
#     place_controller: PlaceController = Depends(Factory().get_place_controller),
#     # assert_access: Callable = Depends(Permissions(TaskPermission.READ)),
# ) -> list[PlaceResponse]:
#     tasks = await place_controller.get_by_merchant_id(merchant_id)

#     # assert_access(tasks)
#     return tasks
