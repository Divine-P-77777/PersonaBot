"""
Text chunking logic.
Splits documents into overlapping chunks for embedding.
"""
from backend.core.config import get_settings


# TODO: Month 2 implementation
def chunk_text(text: str, chunk_size: int = None, chunk_overlap: int = None) -> list[str]:
    """Split text into overlapping chunks."""
    settings = get_settings()
    chunk_size = chunk_size or settings.CHUNK_SIZE
    chunk_overlap = chunk_overlap or settings.CHUNK_OVERLAP
    # TODO: Implement token-based chunking
    return []
