from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.core.config import get_settings

settings = get_settings()


def chunk_text(text: str, chunk_size: int = None, chunk_overlap: int = None) -> list[str]:
    """Split text into overlapping chunks using RecursiveCharacterTextSplitter."""
    chunk_size = chunk_size or settings.CHUNK_SIZE
    chunk_overlap = chunk_overlap or settings.CHUNK_OVERLAP

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    return splitter.split_text(text)
