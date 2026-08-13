from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, Request
from src.api.v1.queries.product_query import ProductQuery
from src.api.v1.responses.product_reponse import ProductResponse
from src.dependencies import get_product_service

products_router = APIRouter(
    prefix="/products", dependencies=[Depends(get_product_service)]
)


@products_router.get("/search", response_model=ProductResponse)
async def search_product(sku: Annotated[str, Query(min_length=5)], request: Request):
    stock_product = request.state.product_service.get_by_sku(sku)
    return stock_product


@products_router.get("/{id}", response_model=ProductResponse)
async def product_infos(id: Annotated[int, Path(gt=0)], request: Request):
    stock_product = request.state.product_service.get_by_id(id)
    return stock_product


@products_router.post("/")
async def create_product(product: ProductQuery, request: Request):
    response_creation = request.state.product_service.create(product.name, product.price)
    return "Product created" if response_creation else ""
