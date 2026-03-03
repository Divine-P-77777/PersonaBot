from pydantic import BaseModel
from typing import Optional


class BotCreate(BaseModel):
    """Schema for creating a new bot."""
    name: str
    description: Optional[str] = None
    persona_config: Optional[dict] = None


class BotUpdate(BaseModel):
    """Schema for updating a bot."""
    name: Optional[str] = None
    description: Optional[str] = None
    persona_config: Optional[dict] = None


class BotResponse(BaseModel):
    """Schema for bot response."""
    id: str
    owner_id: str
    name: str
    description: Optional[str] = None
    persona_config: Optional[dict] = None
    created_at: str
