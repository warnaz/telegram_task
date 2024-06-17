import asyncio
import datetime

from pyrogram.types import Message
from sqlalchemy import select

from configs.messages import MESSAGES
from src.core.loader import client
from src.database.database import sessionmaker
from src.database.models.user import UserModel, UserStatus


async def run() -> None:
    delay = 10

    async with sessionmaker() as session:
        while True:
            async with session.begin():
                result = await session.execute(select(UserModel))
                users = result.scalars().all()

            for user in users:
                if user.status == UserStatus.ALIVE:
                    await handle_user(user)

            await asyncio.sleep(delay)


async def handle_user(user: UserModel) -> None:
    chat_id = user.username or user.id
    now = datetime.datetime.now().timestamp()
    start = user.created_at.timestamp()
    to_send = [(delay, msg) for delay, msg in MESSAGES if now > (delay + start)]
    if not to_send:
        return

    history = [m async for m in client.get_chat_history(chat_id, limit=50)]
    history.reverse()
    for message in history:
        message: Message
        if not message.outgoing:
            continue
        # slice to_send by last sent message
        for v in to_send:
            delay, msg = v
            if message.text == msg.strip():
                to_send = to_send[to_send.index(v) + 1 :]
                break
    if to_send:
        await client.send_message(chat_id, to_send[0][1])
