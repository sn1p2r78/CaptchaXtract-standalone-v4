from fastapi import APIRouter
from src.statistics import get_statistics
from src.auth import create_api_key
import sqlite3

DB_PATH = "statistics.db"

admin_router = APIRouter()

@admin_router.get("/stats")
async def stats():
    """Retrieve system statistics."""
    return get_statistics()

@admin_router.post("/api-key")
async def generate_api_key(role: str = "user"):
    """Generate a new API key."""
    return {"api_key": create_api_key(role=role)}

@admin_router.get("/api-keys")
async def list_api_keys():
    """List all API keys."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT key, rolE FROM p_keys")
    keys = cursor.fetchall()
    conn.close()
    return {"api_keys": keys}