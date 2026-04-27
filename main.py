from contextlib import asynccontextmanager
import sqlite3
from fastapi import FastAPI, HTTPException
from services.product_service import NotFoundProduct, ProductService


@asynccontextmanager
async def lifespan(app: FastAPI):
    DATABASE = "ecommerce.db"
    app.state.db = sqlite3.connect(DATABASE)

    yield

    app.state.db.close()


app = FastAPI(lifespan=lifespan)

from repositories.sqlite_product_repository import SqliteProductRepository


@app.get("/products/{id}")
async def product_infos(id: int):
    repo = SqliteProductRepository(app.state.db)

    try:
        product_service = ProductService(repo=repo)
        stock_product = product_service.get_by_id(id)

    except NotFoundProduct as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"status": "success", "stock": stock_product}
