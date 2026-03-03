from pydantic import BaseModel
from typing import Optional


class ChatMessage(BaseModel):
    """Schema for a chat message."""
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    """Schema for a chat response."""
    response: str
    session_id: str
    sources: list[str] = []
