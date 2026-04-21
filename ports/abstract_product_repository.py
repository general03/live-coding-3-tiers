import sqlite3
from abc import ABC, abstractmethod

from domains.product import Product


DATABASE = "ecommerce.db"
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


class AbstractProductRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Product | None:
        pass
