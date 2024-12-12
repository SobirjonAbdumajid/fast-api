from sqlalchemy import text

from database import get_db
from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    birth_date: date  # Use ISO format: "YYYY-MM-DD"
    enrollment_year: int


@app.get("/students")
async def get_students(
        db: Session = Depends(get_db)
):
    stmt = db.execute(text("SELECT * FROM students"))
    mapping_res = stmt.mappings().all()
    return mapping_res


@app.post("/students")
async def create_student(student: Student, db: Session = Depends(get_db)):
    stmt = text("""
        INSERT INTO students (name, age, birth_date, enrollment_year)
        VALUES (:name, :age, :birth_date, :enrollment_year)
        RETURNING student_id
    """)
    try:
        result = db.execute(stmt, {
            "name": student.name,
            "age": student.age,
            "birth_date": student.birth_date,
            "enrollment_year": student.enrollment_year
        })
        db.commit()
        inserted_id = result.scalar()
        return {"student_id": inserted_id, "message": "Student added successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

