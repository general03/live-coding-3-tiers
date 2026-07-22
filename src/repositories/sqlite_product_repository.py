import sqlite3

from src.domains.exceptions import AccessDataError
from src.domains.product import Product
from src.repositories.ports.abstract_product_repository import AbstractProductRepository


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
            raise AccessDataError("Access error SQLite") from e
