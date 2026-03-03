"""
Authentication middleware for FastAPI.
JWT verification is handled by backend.core.security module.
This middleware can be extended for additional auth checks.
"""
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class AuthMiddleware(BaseHTTPMiddleware):
    """Optional middleware for global auth checks."""

    EXCLUDED_PATHS = ["/health", "/docs", "/openapi.json"]

    async def dispatch(self, request: Request, call_next):
        # Skip auth for excluded paths
        if request.url.path in self.EXCLUDED_PATHS:
            return await call_next(request)

        # Auth is handled per-route via Depends(verify_supabase_token)
        return await call_next(request)
