from abc import ABC, abstractmethod

from domains.product import Product


class AbstractProductRepository(ABC):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.cursor = db.cursor()

    @abstractmethod
    def get_by_id(self, id: int) -> Product | None:
        pass
