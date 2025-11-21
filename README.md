# Coupon-Management
Coupon Management System for e-commerce assignment
Project Overview

This project is a Simple Coupon Management System for an e-commerce use case.

. Allows creating coupons with various eligibility rules.

. Provides an API to return the best coupon for a given user and cart input.

. Uses in-memory storage (no database required for this assignment).

. Supports FLAT and PERCENT discount types with optional maximum discount limit.

. Eligibility rules include: first order only, minimum cart value, allowed categories, excluded categories, minimum item count.

Example: If a user is placing their first order and the cart contains electronics and fashion items, the system will return the best applicable coupon.

Tech Stack

Language: Python 3.14

Framework: FastAPI (for building APIs)

Data Validation: Pydantic

Server: Uvicorn (ASGI server to run FastAPI)
