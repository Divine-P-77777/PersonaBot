"""
Database connection manager.
Handles Supabase and SQLAlchemy connections.
"""
from supabase import create_client, Client

from backend.core.config import get_settings

_supabase_client: Client | None = None


def get_supabase_client() -> Client:
    """Get or create Supabase client singleton."""
    global _supabase_client
    if _supabase_client is None:
        settings = get_settings()
        _supabase_client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_ANON_KEY,
        )
    return _supabase_client
