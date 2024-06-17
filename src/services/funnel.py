import asyncio
import datetime

from pyrogram.types import Message
from sqlalchemy import select

from configs.messages import MESSAGES, FunnelMessage
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
                    status = await handle_user(user)
                    if status:
                        user.status = status
                        async with session.begin():
                            await session.commit()

            await asyncio.sleep(delay)


async def handle_user(user: UserModel) -> UserStatus | None:
    chat_id = user.username or user.id
    now = datetime.datetime.now().timestamp()

    to_send: list[FunnelMessage] = []

    start = user.created_at.timestamp()
    for v in MESSAGES:
        if now > (start + v.delay):
            to_send.append(v)
        start += v.delay

    if not to_send:
        return UserStatus.FINISHED

    history: list[Message] = [
        m async for m in client.get_chat_history(chat_id, limit=50)
    ]
    history.reverse()

    for message in history:
        if message.outgoing:
            # slice to_send by last sent message
            for i, v in enumerate(to_send):
                for trigger_phrase in v.triggers + (v.text, "прекрасно", "ожидать"):
                    if trigger_phrase.lower() in message.text.lower():
                        if v.trigger_action == "break":
                            return UserStatus.FINISHED
                        else:
                            to_send = to_send[i + 1 :]
                            break
    if not to_send:
        return UserStatus.FINISHED
    else:
        await client.send_message(chat_id, to_send[0][1])
