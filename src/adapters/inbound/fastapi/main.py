from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.adapters.inbound.fastapi.dependencies import get_database_connection
from src.adapters.inbound.fastapi.exceptions import app_error_handler, sql_error_handler
from src.adapters.inbound.fastapi.routes import product_router
from src.domains.exceptions import AccessDataError, NotFoundProduct


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = get_database_connection()

    yield

    db.close()


exception_handlers = {
    AccessDataError: sql_error_handler,
    NotFoundProduct: app_error_handler,
}

app = FastAPI(lifespan=lifespan, exception_handlers=exception_handlers)
app.include_router(product_router)
