# 🎟️ Coupon Management System (FastAPI)

A complete REST API project built using **FastAPI**, **SQLite**, and **SQLAlchemy**.  
This application allows you to **create, read, update, delete, and fetch the best coupon** based on maximum discount.

This project follows industry-level folder structuring with `routers`, `schemas`, `models`, and `database` modules.

---

## 🚀 Features

- Create a new coupon  
- Get all coupons  
- Get a coupon by ID  
- Update a coupon  
- Delete a coupon  
- Fetch the *best coupon* (max discount)
- SQLite local database support  
- Clean & modular FastAPI structure  

---

## 🛠️ Tech Stack

- **Python**  
- **FastAPI**  
- **SQLite**  
- **SQLAlchemy**  
- **Pydantic**  
- **Uvicorn**  

---

## 📂 Folder Structure

```
Coupon-Management/
│── main.py
│
├── app/
│   ├── database/
│   │    ├── __init__.py
│   │    └── db.py
│   │
│   ├── models/
│   │    ├── __init__.py
│   │    └── coupon_model.py
│   │
│   ├── schemas/
│   │    ├── __init__.py
│   │    └── coupon_schema.py
│   │
│   ├── routers/
│        ├── __init__.py
│        └── coupon_router.py
│
└── README.md
```

---

## ▶️ How to Run This Project

### **1️⃣ Clone the Repository**
```bash
git clone <your-github-repo-url>
```

### **2️⃣ Go Inside Project Folder**
```bash
cd Coupon-Management
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Start the Server**
```bash
uvicorn main:app --reload
```

### **5️⃣ Open Swagger Documentation**
```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

### ➤ **Create Coupon**
```
POST /coupons/
```
Example Body:
```json
{
  "code": "DIWALI50",
  "discount": 50,
  "is_active": true
}
```

---

### ➤ **Get All Coupons**
```
GET /coupons/
```

---

### ➤ **Get Coupon By ID**
```
GET /coupons/{coupon_id}
```

---

### ➤ **Update Coupon**
```
PUT /coupons/{coupon_id}
```

---

### ➤ **Delete Coupon**
```
DELETE /coupons/{coupon_id}
```

---

### ➤ **Get Best Coupon**
```
GET /coupons/best
```

---

## 🗄️ Database Structure (SQLite)

**Table Name:** `coupons`

| Column      | Type      | Description           |
|-------------|-----------|-----------------------|
| id          | Integer   | Primary Key           |
| code        | Text      | Unique coupon code    |
| discount    | Integer   | Discount percentage   |
| is_active   | Boolean   | Coupon status         |

---

## 📸 Screenshots

### ▶ Swagger UI

![Swagger Screenshot](images/swagger.png)


### ▶ SQLite Database Table

![Database Screenshot](images/database.png)


---

## 📝 Conclusion

This project is part of an internship assignment and demonstrates  
**API development, database integration, folder structuring, and documentation skills** using FastAPI.

---

## 🔮 Future Improvements

- JWT Authentication  
- Pagination  
- Search coupons  
- Coupon expiry date  
- React frontend integration  

---

## 👩‍💻 Author

**Parul Gautam**  
FastAPI Developer • Backend Enthusiast 🚀

