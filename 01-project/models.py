from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    enrollment_year = Column(Integer, nullable=False)
