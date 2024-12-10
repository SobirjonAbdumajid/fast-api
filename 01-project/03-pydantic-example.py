from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class BookSchema(BaseModel):
    title: str
    description: str
    quantity: int
    price: str


@app.post(
    "/book/add",
    status_code=status.HTTP_201_CREATED,
    response_model=BookSchema
)
async def create_book(book: BookSchema):
    return book

