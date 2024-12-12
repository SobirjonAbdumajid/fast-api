from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
import models
from models import Student


from database import get_db, engine

from sqlalchemy import insert
stmt = insert(engine).values(name='John', age=244, birth_date="2023-01-01", enrollment_year=2005)

app = FastAPI()

@app.get("/students")
async def get_students(
        db: Session = Depends(get_db)
):
    stmt = db.execute(text("SELECT * FROM students"))
    mapping_res = stmt.mappings().all()
    return mapping_res


@app.post("/students")
async def create_student(student: Student, db: Session = Depends(get_db)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student