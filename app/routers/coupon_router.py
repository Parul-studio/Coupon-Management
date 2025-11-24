from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.coupon_model import Coupon
from app.schemas.coupon_schema import CouponCreate, CouponResponse

router = APIRouter(prefix="/coupon", tags=["Coupons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Coupon
@router.post("/", response_model=CouponResponse)
def create_coupon(coupon: CouponCreate, db: Session = Depends(get_db)):
    db_coupon = Coupon(code=coupon.code, discount=coupon.discount, expiry=coupon.expiry)
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

# Get All Coupons
@router.get("/", response_model=list[CouponResponse])
def get_all_coupons(db: Session = Depends(get_db)):
    return db.query(Coupon).all()

# Get Single Coupon by ID
@router.get("/{coupon_id}", response_model=CouponResponse)
def get_coupon(coupon_id: int, db: Session = Depends(get_db)):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon

# Update Coupon
@router.put("/{coupon_id}", response_model=CouponResponse)
def update_coupon(coupon_id: int, updated: CouponCreate, db: Session = Depends(get_db)):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    coupon.code = updated.code
    coupon.discount = updated.discount
    coupon.expiry = updated.expiry

    db.commit()
    db.refresh(coupon)
    return coupon

# Delete Coupon
@router.delete("/{coupon_id}")
def delete_coupon(coupon_id: int, db: Session = Depends(get_db)):
    coupon = db.query(Coupon).filter(Coupon.id == coupon_id).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    db.delete(coupon)
    db.commit()
    return {"message": "Coupon deleted successfully"}

# Best Coupon (max discount)
@router.get("/best", response_model=CouponResponse)
def best_coupon(db: Session = Depends(get_db)):
    coupon = db.query(Coupon).order_by(Coupon.discount.desc()).first()
    if not coupon:
        raise HTTPException(status_code=404, detail="No coupons found")
    return coupon
