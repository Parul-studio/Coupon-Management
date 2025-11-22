### **Coupon Management System**
# **Project Overview**

This project is a Simple Coupon Management System built for an e-commerce use case.
It supports:

Creating coupons with multiple eligibility rules

Returning the best coupon for a given user + cart

In-memory storage (no database needed)

FLAT and PERCENT discounts with optional maximum discount limits

Eligibility rules such as:

First order only

Minimum cart value

Allowed / excluded categories

Minimum item count

**Example:**
If the user is placing their first order and the cart contains electronics + fashion items, the system selects the best applicable coupon.

# **Tech Stack**

**.**Language: Python 3.14

**.**Framework: FastAPI

**.**Data Validation: Pydantic

**.**Server: Uvicorn (ASGI server)

# **How to Run**
**Prerequisites**

Python 3.14 installed

pip available

# **Setup Steps**
**1. Clone the repository**

git clone <your-repo-url>
cd coupon-management

**2. Install dependencies**

pip install fastapi uvicorn pydantic

**3. Start the service**

uvicorn main:app --reload

**4. Open API Docs**

Open browser:

http://127.0.0.1:8000/docs

# **Available Endpoints**

**.**POST /create-coupon → Create a new coupon

**.**GET /coupons → List all stored coupons

**.**POST /best-coupon → Returns the best applicable coupon

# **How to Run Tests**


**1. Navigate to project folder**
cd coupon-management

**2. Run all tests**
pytest

**3. For detailed output**
pytest -v

AI Usage Note

# **AI (ChatGPT) was used only for guidance in:**

**.**Planning the project structure

**.**Designing APIs

**.**Understanding eligibility rules

**.**Writing README content

**Example prompts used**

**.**“Help me design a coupon management system API in FastAPI”

**.**“Generate sample README for a coupon management project”

**.**“Explain best coupon selection logic in a coupon system”

# **Additional Notes**

**.**Uses in-memory storage (no real database)

**.**Best coupon selection logic:

**1.**Highest discount

**2.**Earliest expiry

**3.**Lexicographically smallest code (if tie)

**.**Optional eligibility attributes are ignored if not provided

**.**Required demo login (must exist in deployed version):

**.**Email: hire-me@anshumat.org

**.**Password: HireMe@2025!
