from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class BookSchema(BaseModel):
    title: str
    description: str
    quantity: int
    price: str
    created_at: datetime = datetime.now().strftime("%Y-%m-%d")


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


@app.put(
    "/book/{book_id}",
    status_code=status.HTTP_201_CREATED
)
async def update_book(book_id: int, updated_book: BookSchema):
    books[book_id] = updated_book


@app.delete(
    "/book/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(book_id: int):
    del books[book_id]
