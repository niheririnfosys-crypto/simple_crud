from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. The Pydantic Blueprint (Inherits from BaseModel)
class Student(BaseModel):
    id: int
    name: str
    department: str
    contact_number: str

app = FastAPI()

# 2. Mock Database 
students = {
    1: Student(id=1, name="Niher", department="Computer Science", contact_number="11111"),
    2: Student(id=2, name="Alice", department="Data Science", contact_number="22222"),
    3: Student(id=3, name="Bob", department="Electrical Engineering", contact_number="33333")
}

# 3. Get all students
@app.get("/students")
def get_all_students():
    # Pydantic objects can be returned directly, FastAPI handles the conversion!
    return list(students.values())
#4. Get a student by ID


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

# 5. Create a new student 
@app.post("/students")
def save_student(student: Student):
    if student.id in students:
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    
    elif student.contact_number in [stdnt.contact_number for stdnt in students.values()]:
        raise HTTPException(status_code=400, detail="Student with this contact number already exists")
    
    students[student.id] = student
    return student

#6. Update an existing student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Ensure the ID in the path matches the ID in the body
    if student_id != updated_student.id:
        raise HTTPException(status_code=400, detail="ID in path and body do not match")
    
    # Check for duplicate contact number
    for stdnt in students.values():
        if stdnt.contact_number == updated_student.contact_number and stdnt.id != student_id:
            raise HTTPException(status_code=400, detail="Student with this contact number already exists")
    
    students[student_id] = updated_student
    return updated_student
#7. Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted successfully", "student": deleted_student}