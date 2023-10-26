from pydantic import UUID4, BaseModel, Field
from typing import Optional

class PlaceResponse(BaseModel):
    name: Optional[str] = Field(..., example="Brown IFL")
    merchant_id: Optional[str] = Field(..., example="10047668")
    lat: Optional[float] = Field(..., example="11.579923621307662")
    lng: Optional[float] = Field(..., example="104.93031242987828")
    url: Optional[str]= Field(..., example="http://images.google.com/img.jpg")
    class Config:
        from_attributes = True
