# from typing import Annotated
#
# from fastapi import Depends, FastAPI, HTTPException, Query
# from sqlmodel import Field, Session, SQLModel, create_engine, select
#
#
# class Hero(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str = Field(index=True)
#     age: int | None = Field(default=None, index=True)
#     secret_name: str
#
#
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
#
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)
#
#
#
# def get_session():
#     with Session(engine) as session:
#         yield session
#
#
# SessionDep = Annotated[Session, Depends(get_session)]
#
# app = FastAPI()
#
#
#
#
# @app.post("/heroes/")
# def create_hero(hero: Hero, session: SessionDep) -> Hero:
#     session.add(hero)
#     session.commit()
#     session.refresh(hero)
#     return hero
#
#
# @app.get("/heroes/")
# def read_heroes(
#     session: SessionDep,
#     offset: int = 0,
#     limit: Annotated[int, Query(le=100)] = 100,
# ) -> list[Hero]:
#     heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
#     return heroes
#
#


from typing import Annotated
from datetime import date

from fastapi import Depends, FastAPI, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


# Define the SQLModel for the "students" table
class Student(SQLModel, table=True):
    student_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int
    birth_date: date
    enrollment_year: int


# PostgreSQL database connection configuration
engine = create_engine("postgresql+psycopg2://postgres:onamotam@localhost:5432/main_task_database")


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.post("/students/")
def create_student(student: Student, session: SessionDep) -> Student:
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@app.get("/students/")
def read_students(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Student]:
    students = session.exec(select(Student).offset(offset).limit(limit)).all()
    return students

