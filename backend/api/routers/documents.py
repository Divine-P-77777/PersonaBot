from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from backend.core.security import get_current_user_id
from backend.rag.ingestion import ingest_document

router = APIRouter()


@router.post("/{bot_id}/upload")
async def upload_document(
    bot_id: str,
    file: UploadFile = File(...),
    # user_id: str = Depends(get_current_user_id), # Disabled for initial Postman check if needed
):
    """
    Upload a document for a bot (PDF).
    Triggers OCR, chunking, and Nomic embedding generation.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported for now.")

    try:
        content = await file.read()
        num_chunks = await ingest_document(bot_id, file.filename, content)
        
        return {
            "status": "ingested",
            "bot_id": bot_id,
            "filename": file.filename,
            "chunks": num_chunks,
            "method": "EasyOCR"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")


@router.get("/{bot_id}")
async def list_documents(bot_id: str):
    """List all documents for a bot."""
    # TODO: Implement document metadata retrieval from Supabase
    return {"bot_id": bot_id, "documents": []}
