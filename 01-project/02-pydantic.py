from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: str
    price: float
    stock: int


banana = Product(
    title="Banana",
    description=",",
    price=100,
    stock=3
)

print(banana.model_dump())
