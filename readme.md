# 🛒 E-Commerce Backend API (FastAPI)

This project is a **backend REST API for an E-Commerce application** built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It covers core e-commerce functionalities such as **user management, product management, cart & cart items, order calculation, authentication, and debit card generation**.

The project is ideal for **freshers / backend developers** to demonstrate real-world backend logic using Python.

---

## 🚀 Features

* User Registration & Login (Password hashing with Argon2)
* Product Management (Create & List products)
* Cart Management (One cart per user)
* Cart Items (Add products to cart with quantity handling)
* Order Summary (Calculate total price from cart)
* Debit Card Generator (Card number, CVV, PIN)
* PostgreSQL Database Integration
* Clean project structure (models, schemas, CRUD, database)

---

## 🧱 Tech Stack

* **Backend Framework:** FastAPI
* **Language:** Python 3
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Security:** Argon2 Password Hashing
* **Server:** Uvicorn

---

## 📁 Project Structure

```
.
├── main.py          # API routes
├── crud.py          # Business logic
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
├── database.py      # Database connection
├── pass_hash.py     # Password hashing & verification
├── card.py          # Card number, CVV, PIN generator
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ecom-backend-fastapi.git
cd ecom-backend-fastapi
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic argon2-cffi
```

### 4️⃣ Configure Database

Update `DATABASE_URL` in **database.py**:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/ecomm"
```

Make sure PostgreSQL is running and the database exists.

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints Overview

### 👤 User

* `POST /user` → Create user
* `GET /user` → Get users
* `POST /login` → User login

### 📦 Product

* `POST /products/` → Add product
* `GET /products/` → List products

### 🛒 Cart

* `POST /user/cart` → Create cart
* `POST /user/{user_id}/cart/{cart_id}/item` → Add item to cart

### 📄 Order

* `GET /user/{user_id}/order` → View order & total amount

### 💳 Debit Card

* `GET /user/{user_id}/card` → Generate debit card

---

## 🔐 Security Notes

* Passwords are hashed using **Argon2**
* Authentication logic is basic (no JWT yet)
* Security improvements can be added later (JWT, OAuth, Role-based access)

---

## 🎯 Learning Outcomes

* REST API design using FastAPI
* Database modeling with SQLAlchemy
* Handling relationships (User → Cart → CartItem → Product)
* Password hashing & verification
* Clean backend project structure

---

## 📌 Future Improvements

* JWT Authentication
* Order table & payment status
* Admin panel
* Product categories
* Pagination & filtering
* API rate limiting

---

## 👨‍💻 Author

**Swapnil Sarpate**
Python Backend Developer (Fresher)

---

⭐ If you like this project, don’t forget to **star** the repository!
