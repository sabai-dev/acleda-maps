from pydantic import BaseModel, constr, validator, Field
from typing import Optional
import re

class PlaceRequest(BaseModel):
    name: constr(min_length=3, max_length=256) | None
    merchant_id: str=constr(min_length=3, max_length=256)| None
    lat: float | None
    lng: float | None


    @validator('name')
    def merchant_name_must_not_contain_special_characters(cls, v):
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Merchant name must not contain special characters")
        if len(v) < 3:
            raise ValueError("String must be at least 3 characters long")
        return v

    @validator('merchant_id')
    def outlet_name_must_not_contain_special_characters(cls, v):
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Merchant ID must not contain special characters")
        return v
    
    @validator('lat')
    def validate_latitude(cls, v):
        if v < -180.0 or v > 180.0:
            raise ValueError('Latitude must be between -180 and 180 degrees.')
        return v

    @validator('lng')
    def validate_longitude(cls, v):
        if v < -90.0 or v > 90.0:
            raise ValueError('Longitude must be between -90 and 90 degrees.')
        return v
    
    # class Config:
    #         from_attributes = True