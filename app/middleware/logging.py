from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import logging
import time

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cars_logger")

class LogRequestsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api/cars") and request.method == "GET":
            start_time = time.time()
            response = await call_next(request)
            process_time = time.time() - start_time

            logger.info(
                f"📥 {request.method} {request.url.path} - {response.status_code} - {process_time:.3f}s"
            )
            return response
        else:
            return await call_next(request)
