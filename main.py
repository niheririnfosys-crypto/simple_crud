from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, StudentDB


Base.metadata.create_all(bind=engine)
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
# 1. The Pydantic Blueprint (Inherits from BaseModel)
class Student(BaseModel):
    id: int
    name: str
    department: str
    contact_number: str
    fathers_name:str
    mothers_name:str

app = FastAPI()

# 2. Mock Database 
# students = {
#     1: Student(id=1, name="Azad", department="Computer Science", contact_number="11111", fathers_name="Akram",mothers_name="Sabina" ),
#     2: Student(id=2, name="Alice", department="Data Science", contact_number="22222", fathers_name="Clinton", mothers_name="Winslet"),
#     3: Student(id=3, name="Bob", department="Electrical Engineering", contact_number="33333", fathers_name="Zim",mothers_name="Katti")
# }


# 3. Get all students
@app.get("/students")
def get_all_students(
    db: Session = Depends(get_db)
):

    students = db.query(StudentDB).all()

    return students


# 4. Get a student by ID

@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()


    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    return student

# 5. Create a new student 
@app.post("/students")
def save_student(
    student: Student,
    db: Session = Depends(get_db)
):

    existing = db.query(StudentDB).filter(
        StudentDB.id == student.id
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )


    new_student = StudentDB(
        id=student.id,
        name=student.name,
        department=student.department,
        contact_number=student.contact_number,
        fathers_name=student.fathers_name,
        mothers_name=student.mothers_name
    )


    db.add(new_student)
    db.commit()
    db.refresh(new_student)


    return new_student

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