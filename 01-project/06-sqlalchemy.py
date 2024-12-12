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
    birth_date: date
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
        db.execute(stmt, {
            "name": student.name,
            "age": student.age,
            "birth_date": student.birth_date,
            "enrollment_year": student.enrollment_year
        })
        db.commit()
        # inserted_id = result.scalar()
        return {"message": "Student added successfully"}
    except Exception as e:
        # db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    stmt = text("""
        UPDATE students
        SET name = :name, age = :age, birth_date = :birth_date, enrollment_year = :enrollment_year
        WHERE student_id = :student_id
    """)
    try:
        db.execute(stmt, {**student.dict(), "student_id": student_id})
        return {"message": "Student updated successfully"}
    except Exception as e:
        db.rollback()
        return HTTPException(status_code=400, detail=str(e))
    finally:
        db.commit()
        db.close()


# @app.put("/students/{student_id}")
# async def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
#     stmt = text("""
#         UPDATE students
#         SET name = :name, age = :age, birth_date = :birth_date, enrollment_year = :enrollment_year
#         WHERE student_id = :student_id
#     """)
#     try:
#         result = db.execute(stmt, {**student.dict(), "student_id": student_id})
#         if result.rowcount == 0:
#             raise HTTPException(status_code=404, detail="Student not found")
#         db.commit()
#         return {"message": "Student updated successfully"}
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=400, detail=str(e))
