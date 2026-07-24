from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1.exceptions import app_error_handler, sql_error_handler
from src.api.v1.products import products_router
from src.dependencies import get_database_connection
from src.domains.exceptions import AccessDataError
from src.services.product_service import NotFoundProduct


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = get_database_connection()

    yield

    db.close()


error_handler = {AccessDataError: sql_error_handler, NotFoundProduct: app_error_handler}

app = FastAPI(lifespan=lifespan, exception_handlers=error_handler)

app.include_router(products_router)
