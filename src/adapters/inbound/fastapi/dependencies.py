import sqlite3

from fastapi.params import Depends

from src.adapters.inbound.services.product_service import ProductService
from src.adapters.outbound.repositories.sqlite_product_repository import (
    SqliteProductRepository,
)
from src.ports.abstract_product_repository import AbstractProductRepository


def get_database_connection() -> sqlite3.Connection:
    return sqlite3.connect("ecommerce.db", check_same_thread=False)


def get_product_repository(
    db: sqlite3.Connection = Depends(get_database_connection),
) -> AbstractProductRepository:
    return SqliteProductRepository(db)


def get_product_service(
    repo: AbstractProductRepository = Depends(get_product_repository),
) -> ProductService:
    return ProductService(repo=repo)
