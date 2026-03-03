"""
Similarity search using pgvector.
All queries filter by bot_id for multi-tenant safety.
"""


# TODO: Month 2 implementation
async def retrieve_similar_chunks(bot_id: str, query_embedding: list[float], top_k: int = 5) -> list[dict]:
    """Retrieve top-K similar chunks for a bot using pgvector."""
    # MUST include: WHERE bot_id = ?
    pass
