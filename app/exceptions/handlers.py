from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom import NotFoundError, DuplicateEntryError

def register_exception_handlers(app):
    @app.exception_handler(NotFoundError)
    async def not_found_exception_handler(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=404,
            content={"data": None, "status": 404, "message": exc.detail},
        )

    @app.exception_handler(DuplicateEntryError)
    async def duplicate_entry_handler(request: Request, exc: DuplicateEntryError):
        return JSONResponse(
            status_code=409,
            content={"data": None, "status": 409, "message": exc.detail},
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"data": None, "status": 500, "message": "Error interno del servidor"},
        )
