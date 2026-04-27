import sqlite3
from ports.abstract_product_repository import AbstractProductRepository
from fastapi import HTTPException
from domains.product import Product


class SqliteProductRepository(AbstractProductRepository):
    def get_by_id(self, id: int) -> Product | None:
        try:
            self.cursor.execute("SELECT stock, price FROM products WHERE id = ?", (id,))
            product = self.cursor.fetchone()
            if product:
                return Product(*product)
            return None
        except sqlite3.Error as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))  # Not do this
