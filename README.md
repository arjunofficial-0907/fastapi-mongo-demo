# FastAPI + MongoDB REST API Demo  
A clean, modular, and production-ready REST API built with **FastAPI**, **Motor (async MongoDB driver)**, and **Pydantic v2**.  
This demo includes CRUD endpoints, BasicAuth authentication, proper validations, and a Postman collection for instant testing.

---

## 🚀 Features

✅ **Async CRUD** for each collection  
✅ **FastAPI** with modular routers  
✅ **MongoDB (Motor)** async client  
✅ **Basic Authentication** (username/password with SHA-256 hashing)  
✅ **Pydantic v2** models + ObjectId handling  
✅ **Environment-based config** (`.env`)  
✅ **Proper error responses** and validations  
✅ **Postman Collection** included  
✅ **Clean folder structure** for easy extension  

---
2️⃣ Create and activate a virtual environment

python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure .env

cp .env.example .env

MONGO_URI=mongodb://localhost:27017
MONGO_DB_NAME=demo_db
BASIC_AUTH_USERNAME=admin
BASIC_AUTH_PASSWORD_HASH=your_sha256_hash_here

▶️ Running the API

uvicorn app.main:app --reload
