# Student Management CRUD API

A lightweight, high-performance RESTful API built with **FastAPI** to manage student records. This project demonstrates full CRUD (Create, Read, Update, Delete) capabilities using an in-memory data store, specifically optimized for seamless execution and testing directly via **URL Path & Query Parameters** (without requiring complex request bodies).

## 🚀 Features

- **In-Memory Database**: Blazing fast state management using native Python dictionaries.
- **Robust Data Validation**: Automatic type validation leveraging FastAPI's underlying parsing system.
- **Strict Business Logic**: Preventative checks against duplicate data (e.g., matching IDs or clashing contact numbers).
- **Pure URL Interaction**: No JSON payloads required—perfect for quick browser testing, curl commands, or lightweight API clients like Bruno.

---

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI server)
- **Data Modeling**: Pydantic
- **Testing Client**: Bruno / Web Browser

---

## 📂 Code Overview (`main.py`)

Below is the complete implementation used in this project:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. The Data Blueprint
class Student(BaseModel):
    id: int
    name: str
    department: str
    contact_number: str

app = FastAPI()

# 2. In-Memory Mock Database
students = {
    1: Student(id=1, name="Niher", department="Computer Science", contact_number="11111"),
    2: Student(id=2, name="Alice", department="Data Science", contact_number="22222")
}

# 3. READ: Get All Students
@app.get("/students")
def get_all_students():
    return list(students.values())

# 4. READ: Get Single Student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

# 5. CREATE: Add New Student entirely via URL Query Parameters
@app.post("/students/create")
def create_student_url(id: int, name: str, department: str, contact_number: str):
    if id in students:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    if contact_number in [s.contact_number for s in students.values()]:
        raise HTTPException(status_code=400, detail="Contact number already exists")
        
    new_student = Student(id=id, name=name, department=department, contact_number=contact_number)
    students[id] = new_student
    return {"message": "Created successfully", "student": new_student}

# 6. UPDATE: Modify Student entirely via URL (Path + Query Parameters)
@app.put("/students/update/{student_id}")
def update_student_url(student_id: int, name: str, department: str, contact_number: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    for s in students.values():
        if s.contact_number == contact_number and s.id != student_id:
            raise HTTPException(status_code=400, detail="Contact number belongs to someone else")
            
    updated_student = Student(id=student_id, name=name, department=department, contact_number=contact_number)
    students[student_id] = updated_student
    return {"message": "Updated successfully", "student": updated_student}

# 7. DELETE: Remove Student entirely via URL Path Parameter
@app.delete("/students/delete/{student_id}")
def delete_student_url(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
        
    deleted = students.pop(student_id)
    return {"message": f"Student '{deleted.name}' deleted successfully"}
