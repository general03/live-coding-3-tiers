from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1.exceptions import app_error_handler, sql_error_handler
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


# TODO : need to import this fake router (it is not a right practice)
# See the router fastapi video to do this better
from src.api.v1.products import *
