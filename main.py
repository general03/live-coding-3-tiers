from contextlib import asynccontextmanager
import sqlite3
from exception import AccessDataError, AppError
from fastapi import FastAPI, Request
from services.product_service import NotFoundProduct, ProductService
from fastapi.responses import JSONResponse

from repositories.sqlite_product_repository import SqliteProductRepository


@asynccontextmanager
async def lifespan(app: FastAPI):
    DATABASE = "ecommerce.db"
    app.state.db = sqlite3.connect(DATABASE)

    yield

    app.state.db.close()


app = FastAPI(lifespan=lifespan)


@app.exception_handler(AccessDataError)
async def sql_error_handler(request: Request, e: AppError):
    return JSONResponse(
        status_code=500, content={"error": str(e), "detail": str(e.__cause__)}
    )


@app.exception_handler(NotFoundProduct)
async def app_error_handler(request: Request, e: AppError):
    return JSONResponse(status_code=400, content={"data": str(e)})


@app.get("/products/{id}")
async def product_infos(id: int):
    repo = SqliteProductRepository(app.state.db)

    product_service = ProductService(repo=repo)
    stock_product = product_service.get_by_id(id)

    return JSONResponse(content={"data": {"stock": stock_product}})
