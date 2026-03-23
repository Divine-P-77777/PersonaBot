import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.core.config import get_settings

settings = get_settings()


class NomicEmbeddings:
    """Nomic V2 Embedding wrapper using HuggingFace."""

    def __init__(self):
        # Nomic V2-MoE needs trust_remote_code=True
        self.client = HuggingFaceEmbeddings(
            model_name="nomic-ai/nomic-embed-text-v2-moe",
            model_kwargs={"trust_remote_code": True},
            # Nomic V2 multi-stage embedding might need specific prefixes 
            # for search/clustering as per their docs
            encode_kwargs={"normalize_embeddings": True}
        )

    def embed_query(self, text: str) -> list[float]:
        """Embed search query with prefix."""
        # Nomic V2 usually expects "search_query: " prefix for queries
        return self.client.embed_query(f"search_query: {text}")

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed document chunks with prefix."""
        # Nomic V2 usually expects "search_document: " prefix for documents
        prefixed_texts = [f"search_document: {t}" for t in texts]
        return self.client.embed_documents(prefixed_texts)


_embeddings_instance = None


def get_embeddings():
    """Get or create embeddings instance singleton."""
    global _embeddings_instance
    if _embeddings_instance is None:
        _embeddings_instance = NomicEmbeddings()
    return _embeddings_instance
