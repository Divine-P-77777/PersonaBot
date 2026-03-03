from fastapi import APIRouter

router = APIRouter()


@router.post("/{bot_id}/start")
async def start_voice_session(bot_id: str):
    """Start a live voice session with a bot."""
    # TODO: Implement WebRTC signaling + voice pipeline
    return {"message": "Voice session endpoint", "bot_id": bot_id}


@router.post("/{bot_id}/stop")
async def stop_voice_session(bot_id: str):
    """Stop an active voice session."""
    # TODO: Implement session teardown
    return {"message": "Voice session stopped", "bot_id": bot_id}
