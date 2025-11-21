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

How to Run

## How to Run

### Prerequisites
- Python 3.14 installed
- pip available

### Setup Steps
1. Clone the repository:

git clone <your-repo-link>
cd coupon-management

Install dependencies:
pip install fastapi uvicorn pydantic

Start the Service
uvicorn main:app --reload
Open your browser: http://127.0.0.1:8000/docs

Test the endpoints:

  .POST /create-coupon → To create coupons

  .GET /coupons → To list all coupons

  .POST /best-coupon → To get the best applicable coupon

 How to Run Tests
 # Navigate to project folder
cd coupon-management

# Run all tests
pytest
Output will show test results (pass/fail) and any errors.

You can also use pytest -v for detailed output.

AI Usage Note

AI (ChatGPT) was used only for guidance:

Planning project structure

Designing APIs

Understanding eligibility rules

Creating README content

Example prompts used:

“Help me design a coupon management system API in FastAPI”

“Generate sample README for a coupon management project”

“Explain best coupon selection logic in a coupon system”

Additional Notes

Uses in-memory storage; no real database required.

Best coupon selection logic:

Highest discount → Earliest expiry → Lexicographically smallest code (if tie occurs)

Optional eligibility attributes are ignored if not provided.

Hard-coded demo login user
Email: hire-me@anshumat.org
Password: HireMe@2025!
