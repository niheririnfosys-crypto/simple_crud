# Student Management CRUD API

A lightweight, high-performance RESTful API built with **FastAPI** to manage student records. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations using a real **SQLite database** with **SQLAlchemy ORM**.

The API provides a clean database-driven backend architecture with automatic data validation, persistent storage, and easy testing through **Swagger UI, Bruno, curl, or API clients**.

---

## 🚀 Features

- **SQLite Database Integration**  
  Persistent student data storage using SQLite database.

- **SQLAlchemy ORM**
  Database interaction through SQLAlchemy models instead of direct SQL queries.

- **Complete CRUD Operations**
  - Create new students
  - Read all students
  - Read a student by ID
  - Update existing student information
  - Delete student records

- **Automatic Data Validation**
  Request and response validation using Pydantic models.

- **Business Logic Validation**
  Prevents:
  - Duplicate student IDs
  - Duplicate contact numbers

- **FastAPI Dependency Injection**
  Database sessions are managed safely using FastAPI's dependency system.

- **Interactive API Testing**
  Supports testing using:
  - Swagger UI
  - Bruno
  - Browser
  - curl

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Server**: Uvicorn (ASGI Server)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing Client**: Bruno / Swagger UI

---

## 📂 Project Structure
crud_api/
│
├── main.py # FastAPI routes and CRUD operations
│
├── database.py # SQLite database connection and session setup
│
├── models.py # SQLAlchemy database models
│
├── app.db # SQLite database file
│
├── requirements.txt
│
└── .gitignore


---

## 🗄️ Database Model

Student table:

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | String | Student name |
| department | String | Academic department |
| contact_number | String | Unique contact number |
| fathers_name | String | Father's name |
| mothers_name | String | Mother's name |

---

## 🔌 API Endpoints

### 1. Get All Students


GET /students


Example response:

```json
[
  {
    "id": 1,
    "name": "Azad",
    "department": "Computer Science",
    "contact_number": "11111",
    "fathers_name": "Akram",
    "mothers_name": "Sabina"
  }
]
2. Get Student By ID
GET /students/{student_id}

Example:

GET /students/1

Response:

{
  "id":1,
  "name":"Azad",
  "department":"Computer Science",
  "contact_number":"11111",
  "fathers_name":"Akram",
  "mothers_name":"Sabina"
}
3. Create Student
POST /students

Request body:

{
  "id":4,
  "name":"John",
  "department":"Software Engineering",
  "contact_number":"44444",
  "fathers_name":"David",
  "mothers_name":"Maria"
}

Response:

{
  "id":4,
  "name":"John",
  "department":"Software Engineering",
  "contact_number":"44444",
  "fathers_name":"David",
  "mothers_name":"Maria"
}
4. Update Student
PUT /students/{student_id}

Example:

PUT /students/4

Request:

{
  "id":4,
  "name":"John Updated",
  "department":"AI Engineering",
  "contact_number":"44444",
  "fathers_name":"David",
  "mothers_name":"Maria"
}
5. Delete Student
DELETE /students/{student_id}

Example:

DELETE /students/4

Response:

{
  "message":"Student deleted successfully"
}
▶️ Running the Project

Create virtual environment:

python -m venv .venv

Activate:

Linux:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs
🧪 Database Checking

Open SQLite:

sqlite3 app.db

View tables:

.tables

Check students:

SELECT * FROM students;

Exit:

.quit

📌 Future Improvements

Possible next improvements:

Add authentication (JWT)
Add user roles
Add Alembic database migrations
Separate routers and schemas
PostgreSQL migration
Docker deployment
Cloud deployment

👨‍💻 Author

Built with FastAPI + SQLite + SQLAlchemy


