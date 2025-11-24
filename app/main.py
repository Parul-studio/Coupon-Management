from fastapi import FastAPI
from app.routers.coupon_router import router
from app.database.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Coupon Management API is running!"}
