from fastapi import APIRouter, Depends, UploadFile, File

from backend.core.security import get_current_user_id

router = APIRouter()


@router.post("/{bot_id}/upload")
async def upload_document(
    bot_id: str,
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user_id),
):
    """Upload a document for a bot (PDF, DOCX, Image)."""
    # TODO: Implement document upload + ingestion trigger
    return {
        "message": "Document uploaded",
        "bot_id": bot_id,
        "filename": file.filename,
    }


@router.get("/{bot_id}")
async def list_documents(bot_id: str):
    """List all documents for a bot."""
    # TODO: Implement document listing
    return {"bot_id": bot_id, "documents": []}


@router.delete("/{bot_id}/{document_id}")
async def delete_document(
    bot_id: str,
    document_id: str,
    user_id: str = Depends(get_current_user_id),
):
    """Delete a document from a bot."""
    # TODO: Implement document deletion
    return {"message": "Document deleted", "document_id": document_id}
