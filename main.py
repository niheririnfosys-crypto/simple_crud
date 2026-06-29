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


# 1. The Pydantic Blueprint
class Student(BaseModel):
    id: int
    name: str
    department: str
    contact_number: str
    fathers_name: str
    mothers_name: str


app = FastAPI()


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



# 6. Update an existing student

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student,
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


    student.name = updated_student.name
    student.department = updated_student.department
    student.contact_number = updated_student.contact_number
    student.fathers_name = updated_student.fathers_name
    student.mothers_name = updated_student.mothers_name


    db.commit()
    db.refresh(student)


    return student



# 7. Delete a student

@app.delete("/students/{student_id}")
def delete_student(
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


    db.delete(student)

    db.commit()


    return {
        "message": "Student deleted successfully"
    }