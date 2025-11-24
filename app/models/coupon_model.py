from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount = Column(Integer)
    expiry = Column(String)
