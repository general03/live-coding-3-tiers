from pydantic import BaseModel


class ProductResponse(BaseModel):
    name: str
    stock: int
    price: float
