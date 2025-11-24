from pydantic import BaseModel

class CouponCreate(BaseModel):
    code: str
    discount: int
    expiry: str

class CouponResponse(CouponCreate):
    id: int

    class Config:
        orm_mode = True
