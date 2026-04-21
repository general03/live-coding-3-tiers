import sqlite3
from ports.abstract_product_repository import AbstractProductRepository, cursor, conn
from fastapi import HTTPException
from domains.product import Product


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
            raise HTTPException(status_code=500, detail=str(e))  # Not do this
