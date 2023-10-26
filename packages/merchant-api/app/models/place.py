from enum import Enum
from uuid import uuid4
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, String, Float, DateTime, Integer, VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from core.database import Base
from core.database.mixins import TimestampMixin
from core.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)




class Place(Base, TimestampMixin):
    __tablename__ = "places"
    id= Column(BigInteger, primary_key=True, autoincrement=True)   
    name = Column(VARCHAR(255), nullable=False) # name added by user
    merchant_id = Column(VARCHAR(25), nullable=False) # outlet_id/merchant_id(POS) or partner_id(KHQR)
    logo_url = Column(VARCHAR(255))
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    # created_at = Column(DateTime, default=datetime.now)
    # updated_at = Column(DateTime, default=datetime.now)
     

    
    


   
