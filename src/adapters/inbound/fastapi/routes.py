from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.adapters.inbound.fastapi.dependencies import get_product_service
from src.adapters.inbound.services.product_service import ProductService

product_router = APIRouter(prefix="/products", tags=["products"])


@product_router.get("/{id}")
async def product_infos(
    id: int, product_service: ProductService = Depends(get_product_service)
):
    stock_product = product_service.get_by_id(id)

    return JSONResponse(content={"data": {"stock": stock_product}})
