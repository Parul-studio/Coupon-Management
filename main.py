from fastapi import FastAPI
from app.routers.coupon_router import router
from app.database.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include coupon router
app.include_router(router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Coupon Management API is running!"}
