from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()

DATABASE = "ecommerce.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

@app.get("/products/{id}")
async def product_infos(id: int):
    # Requête SQL brute au milieu de la route
    repo = SqliteProductRepository()
    product = repo.get_by_id(id)

    if not product:
        raise HTTPException(status_code=404, detail="Produit introuvable")

    if product.stock == 0:
        raise HTTPException(status_code=400, detail="Stock insuffisant")

    return {"status": "success", "total": product.price}


# domains/product.py
from dataclasses import dataclass

@dataclass
class Product:
    stock: int 
    price: float

# ports/abstract_product_repository.py
from abc import ABC, abstractmethod 
class AbstractProductRepository(ABC):

    @abstractmethod
    def get_by_id(self, id: int)-> Product | None:
        pass

# repositories/sqlite_product_repository.py
class SqliteProductRepository(AbstractProductRepository):

    def get_by_id(self, id: int) -> Product | None:
        try:
            cursor.execute("SELECT stock, price FROM products WHERE id = ?", (id,))
            product = cursor.fetchone()
            if product:
                return Product(*product)
            return None
        except sqlite3.Error as e:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(e))