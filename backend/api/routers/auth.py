from fastapi import APIRouter, Depends

from backend.core.security import verify_supabase_token

router = APIRouter()


@router.get("/me")
async def get_current_user(payload: dict = Depends(verify_supabase_token)):
    """Get current authenticated user info."""
    return {
        "user_id": payload.get("sub"),
        "email": payload.get("email"),
        "role": payload.get("role"),
    }
