from fastapi import Depends
from fastapi.responses import JSONResponse

from src.dependencies import get_product_service
from src.main import app
from src.services.product_service import ProductService


@app.get("/products/{id}")
async def product_infos(
    id: int, product_service: ProductService = Depends(get_product_service)
):
    stock_product = product_service.get_by_id(id)

    return JSONResponse(content={"data": {"stock": stock_product}})
