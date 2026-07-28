from fastapi import APIRouter, Depends, Request
from src.api.v1.responses.product_reponse import ProductResponse
from src.dependencies import get_product_service

products_router = APIRouter(
    prefix="/products", dependencies=[Depends(get_product_service)]
)


@products_router.get("/{id}", response_model=ProductResponse)
async def product_infos(id: int, request: Request):
    stock_product = request.state.product_service.get_by_id(id)
    return stock_product
