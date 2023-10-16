from pydantic import UUID4, BaseModel, Field


class MerchantResponse(BaseModel):
    name: str = Field(..., example="Sabaicode")
    uuid: UUID4 = Field(..., example="a3b8f042-1e16-4f0a-a8f0-421e16df0a2f")

    class Config:
        from_attributes = True
