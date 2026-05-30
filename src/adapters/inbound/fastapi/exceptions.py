from fastapi import Request
from fastapi.responses import JSONResponse

from src.domains.exceptions import AppError


async def sql_error_handler(request: Request, e: AppError):
    return JSONResponse(
        status_code=500, content={"error": str(e), "detail": str(e.__cause__)}
    )


async def app_error_handler(request: Request, e: AppError):
    return JSONResponse(status_code=400, content={"data": str(e)})
