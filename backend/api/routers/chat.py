from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from backend.core.security import get_current_user_id

router = APIRouter()


@router.post("/{bot_id}")
async def chat_with_bot(
    bot_id: str,
    user_id: str = Depends(get_current_user_id),
):
    """Send a message and receive a streaming response from a bot."""
    # TODO: Implement RAG retrieval + LLM streaming via SSE
    async def generate():
        yield "data: Bot response placeholder\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


@router.get("/{bot_id}/history")
async def get_chat_history(
    bot_id: str,
    user_id: str = Depends(get_current_user_id),
):
    """Get chat history for a bot session."""
    # TODO: Implement chat history retrieval
    return {"bot_id": bot_id, "history": []}
