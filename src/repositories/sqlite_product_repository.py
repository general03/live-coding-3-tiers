import sqlite3

from src.domains.exceptions import AccessDataError
from src.domains.product import Product
from src.repositories.ports.abstract_product_repository import AbstractProductRepository


class SqliteProductRepository(AbstractProductRepository):
    def get_by_id(self, id: int) -> Product | None:
        try:
            self.cursor.execute("SELECT sku, name, price, stock FROM products WHERE id = ?", (id,))
            product = self.cursor.fetchone()
            if product:
                return Product(*product)
            return None
        except sqlite3.Error as e:
            self.db.rollback()
            raise AccessDataError("Access error SQLite") from e

    def get_by_sku(self, sku: str) -> Product | None:
        try:
            self.cursor.execute("SELECT sku, name, price, stock FROM products WHERE sku = ?", (sku,))
            product = self.cursor.fetchone()
            if product:
                return Product(*product)
            return None
        except sqlite3.Error as e:
            self.db.rollback()
            raise AccessDataError("Access error SQLite") from e

    def insert(self, product: Product) -> bool:
        try:
            self.cursor.execute("INSERT INTO products (sku, name, stock, price) VALUES (?, ?, ?, ?)", (product.sku,product.name,product.stock,product.price,))
            product = self.cursor.fetchone()
            self.db.commit()
            return True
        except sqlite3.Error as e:
            self.db.rollback()
            raise AccessDataError("Access error SQLite") from e