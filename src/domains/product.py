from dataclasses import dataclass


@dataclass
class Product:
    name: str
    stock: int
    price: float
