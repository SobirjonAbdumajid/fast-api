from pydantic import BaseModel


class Product(BaseModel):
    title: str
    description: str
    price: tuple[int, float]
    stock: int


banana1 = Product(
    title="Banana",
    description=",",
    price=[100, 2],
    stock=3
)

banana2 = Product(
    title="Banana",
    description="Text",
    price=[100, 20.1],
    stock=3
)

print(banana1 == banana2)
print(banana1.model_dump())
