from pydantic import BaseModel


class StudentSchema(BaseModel):
    name: str
    age: int
