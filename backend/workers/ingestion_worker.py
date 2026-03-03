"""
Background worker for document ingestion.
TODO: Process uploaded documents asynchronously.
"""


async def process_document(bot_id: str, document_id: str):
    """Background task to process an uploaded document."""
    # 1. Download file from Supabase Storage
    # 2. Extract text (PDF, DOCX, Image+OCR)
    # 3. Clean and chunk text
    # 4. Generate embeddings
    # 5. Store chunks + embeddings in database
    pass
