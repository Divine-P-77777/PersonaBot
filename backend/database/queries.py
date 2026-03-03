"""
Database query helpers.
All queries enforce multi-tenant isolation via bot_id filtering.
"""


# TODO: Implement query functions
# Every query MUST include WHERE bot_id = ? for multi-tenant safety.

async def get_bots_by_owner(owner_id: str):
    """Get all bots owned by a user."""
    pass


async def get_bot_by_id(bot_id: str):
    """Get a single bot by ID."""
    pass


async def get_documents_by_bot(bot_id: str):
    """Get all documents for a bot."""
    pass


async def search_embeddings(bot_id: str, query_embedding: list, top_k: int = 5):
    """Similarity search in document_embeddings filtered by bot_id."""
    pass
