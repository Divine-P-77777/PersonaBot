from pydantic import BaseModel
from typing import Optional


class UserProfile(BaseModel):
    """Schema for user profile."""
    id: str
    email: str
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
