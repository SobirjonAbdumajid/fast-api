from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class BookSchema(BaseModel):
    title: str
    description: str
    quantity: int
    price: str


books = []


@app.post(
    "/book/add",
    status_code=status.HTTP_201_CREATED,
    response_model=BookSchema
)
async def create_book(book: BookSchema):
    books.append(book)
    print(books)
    print(book.json())
    return book


@app.get("/book/{book_id}")
async def read_book():
    return books



