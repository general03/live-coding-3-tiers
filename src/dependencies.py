import sqlite3

from fastapi import Depends, Request

from src.repositories.ports.abstract_product_repository import AbstractProductRepository
from src.repositories.sqlite_product_repository import SqliteProductRepository
from src.services.product_service import ProductService


def get_database_connection() -> sqlite3.Connection:
    return sqlite3.connect("ecommerce.db", check_same_thread=False)


def get_product_repository(
    db: sqlite3.Connection = Depends(get_database_connection),
) -> AbstractProductRepository:
    return SqliteProductRepository(db)


def get_product_service(
    request: Request, repo: AbstractProductRepository = Depends(get_product_repository)
) -> ProductService:
    request.state.product_service = ProductService(repo=repo)
    return request.state.product_service
