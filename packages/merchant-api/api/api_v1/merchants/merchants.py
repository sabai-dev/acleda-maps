from typing import Callable
from fastapi import APIRouter, Depends, Request

# from app.controllers import MerchantController
# from app.models.merchant import MerchantPermission
# from app.schemas.requests.merchants import MerchantCreate
from app.schemas.responses.merchants import MerchantResponse
# from core.factory import Factory
# from core.fastapi.dependencies.permissions import Permissions

merchant = APIRouter()

@merchant.get("/", response_model=list[MerchantResponse])
async def get_merchants(
# #     request: Request,
# #     merchant_controller: MerchantController = Depends(Factory().get_merchant_controller),
# #     assert_access: Callable = Depends(Permissions(MerchantPermission.READ)),
) -> list[MerchantResponse]:
    merchants = [] #await merchant_controller.get_by_author_id(request.user.id)

    # assert_access(merchants)
    return merchants

@merchant.post("/", status_code=201)
async def register_merchant(
#     register_merchant_request: RegisterMerchantRequest,
#     auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> MerchantResponse:
#     return await auth_controller.register(
#         email=register_user_request.email,
#         password=register_user_request.password,
#         username=register_user_request.username,
#     )
    return {}



