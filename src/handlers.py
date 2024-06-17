from pyrogram import Client, filters
from pyrogram.types import Message, User

from src.database.database import sessionmaker
from src.services.users import add_user, user_exists


def register_client_handlers(client: Client) -> None:
    client.on_message(filters.private)(handle_message)


async def handle_message(client: Client, message: Message):
    if not message.from_user:
        return

    user: User = message.from_user

    async with sessionmaker() as session:
        if not await user_exists(session, message.from_user.id):
            await add_user(session=session, user=user)
    print("User added to the database.")
