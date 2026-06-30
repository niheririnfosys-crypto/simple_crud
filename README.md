# Student Management CRUD API

A lightweight, high-performance RESTful API built with **FastAPI** to manage student records. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations using a real **SQLite database** with **SQLAlchemy ORM**.

The API provides a clean database-driven backend architecture with automatic data validation, persistent storage, and easy testing through **Swagger UI, Bruno, curl, or API clients**.

---

## 🚀 Features

- **SQLite Database Integration** Persistent student data storage using SQLite database.

### Main Dependencies

- **FastAPI**: A modern Python framework used to build the REST API endpoints.
- **Uvicorn**: An ASGI server used to run the FastAPI application.
- **SQLAlchemy**: A database toolkit and ORM library used for database connection management, SQL operations, and mapping Python objects to database tables.
- **Pydantic**: Used for data validation and defining request/response schemas.
- **Starlette**: The underlying web framework component that provides core web functionality for FastAPI.

### SQLAlchemy Database Engine and ORM

SQLAlchemy Engine acts as a bridge between the application and the database. It manages database connections, handles SQL execution, and provides a connection pool for efficient request handling. For SQLite, `check_same_thread=False` allows database connections to work safely with FastAPI request handling. 

SQLAlchemy ORM maps Python classes and objects to database tables and rows, allowing developers to interact with the database using Python code instead of writing raw SQL queries.

- **Complete CRUD Operations**
  - Create new students
  - Read all students
  - Read a student by ID
  - Update existing student information
  - Delete student records

- **Automatic Data Validation** Request and response validation using Pydantic models.

- **Business Logic Validation** Prevents:
  - Duplicate student IDs
  - Duplicate contact numbers

- **FastAPI Dependency Injection** Database sessions are managed safely using FastAPI's dependency system.

- **Interactive API Testing** Supports testing using Swagger UI, Bruno, Browser, and curl.

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

```text
crud_api/
│
├── main.py            # FastAPI routes and CRUD operations
├── database.py        # SQLite database connection and session setup
├── models.py          # SQLAlchemy database models
├── app.db             # SQLite database file (generated automatically)
├── requirements.txt   # Project dependencies
└── .gitignore         # Untracked Git files

🗄️ Database ModelStudent Table Schema:FieldTypeDescriptionidIntegerPrimary keynameStringStudent namedepartmentStringAcademic departmentcontact_numberStringUnique contact numberfathers_nameStringFather's namemothers_nameStringMother's name🔌 API Endpoints1. Get All StudentsMethod: GETURL: /studentsExample Response:JSON[
  {
    "id": 1,
    "name": "Azad",
    "department": "Computer Science",
    "contact_number": "11111",
    "fathers_name": "Akram",
    "mothers_name": "Sabina"
  }
]
2. Get Student By IDMethod: GETURL: /students/{student_id}Example Request: GET /students/1Response:JSON{
  "id": 1,
  "name": "Azad",
  "department": "Computer Science",
  "contact_number": "11111",
  "fathers_name": "Akram",
  "mothers_name": "Sabina"
}
3. Create StudentMethod: POSTURL: /studentsRequest Body:JSON{
  "id": 4,
  "name": "John",
  "department": "Software Engineering",
  "contact_number": "44444",
  "fathers_name": "David",
  "mothers_name": "Maria"
}
Response:JSON{
  "id": 4,
  "name": "John",
  "department": "Software Engineering",
  "contact_number": "44444",
  "fathers_name": "David",
  "mothers_name": "Maria"
}
4. Update StudentMethod: PUTURL: /students/{student_id}Example Request: PUT /students/4Request Body:JSON{
  "name": "John Updated",
  "department": "AI Engineering",
  "contact_number": "44444",
  "fathers_name": "David",
  "mothers_name": "Maria"
}
5. Delete StudentMethod: DELETEURL: /students/{student_id}Example Request: DELETE /students/4Response:JSON{
  "message": "Student deleted successfully"
}
▶️ Running the ProjectCreate a virtual environment:Bashpython -m venv .venv
Activate the environment:Linux/macOS: source .venv/bin/activateWindows: .venv\Scripts\activateInstall dependencies:Bashpip install -r requirements.txt
Run the Uvicorn server:Bashuvicorn main:app --reload
Open Interactive Docs: Navigate to http://127.0.0.1:8000/docs to test via Swagger UI.🧪 Database Checking (CLI)You can inspect the generated persistent records straight from your terminal terminal:Open SQLite CLI:Bashsqlite3 app.db
View generated tables:SQL.tables
Check contents inside the students table:SQLSELECT * FROM students;
Exit SQLite CLI:SQL.quit

📌 Future ImprovementsAdd authentication (JWT)Add user roles & access permissionsIntegrated database version control via Alembic migrationsBreak core components out into distinct routers and Pydantic schemasMigration from SQLite to PostgreSQLContainerization using Docker

👨‍💻 AuthorBuilt with FastAPI + SQLite + SQLAlchemy.