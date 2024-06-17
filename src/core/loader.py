from pyrogram import Client

from src.core.config import settings

client = Client(
    name="userbot",
    api_id=settings.TELEGRAM_API_ID,
    api_hash=settings.TELEGRAM_API_HASH,
)
