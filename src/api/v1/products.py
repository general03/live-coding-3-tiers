from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from src.dependencies import get_product_service

products_router = APIRouter(
    prefix="/products", dependencies=[Depends(get_product_service)]
)


@products_router.get("/{id}", deprecated=True)
async def product_infos(id: int, request: Request):
    stock_product = request.state.product_service.get_by_id(id)

    return JSONResponse(content={"data": {"stock": stock_product}})
