from pydantic import BaseModel


class ProductQuery(BaseModel):
    name: str
    price: float
