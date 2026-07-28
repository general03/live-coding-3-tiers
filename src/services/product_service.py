from src.domains.exceptions import NotFoundProduct
from src.domains.product import Product


class ProductService:
    def __init__(self, repo):
        self.repo = repo

    def get_by_id(self, id: int) -> Product:
        product = self.repo.get_by_id(id)

        if not product:
            raise NotFoundProduct("Produit introuvable")

        if product.stock == 0:
            raise NotFoundProduct("Stock insuffisant")

        return product
