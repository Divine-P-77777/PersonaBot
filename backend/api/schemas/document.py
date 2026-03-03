from pydantic import BaseModel
from typing import Optional


class DocumentResponse(BaseModel):
    """Schema for document response."""
    id: str
    bot_id: str
    file_name: str
    metadata: Optional[dict] = None
    created_at: str
