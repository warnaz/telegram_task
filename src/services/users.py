from pyrogram.types import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import UserModel
from src.database.models.user import UserStatus


async def add_user(
    session: AsyncSession,
    user: User,
) -> None:
    """Add a new user to the database."""
    new_user = UserModel(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        username=user.username,
        status=UserStatus.ALIVE,
    )

    session.add(new_user)
    await session.commit()


async def user_exists(session: AsyncSession, user_id: int) -> bool:
    """Checks if the user is in the database."""
    query = select(UserModel.id).filter_by(id=user_id).limit(1)

    result = await session.execute(query)

    user = result.scalar_one_or_none()
    return bool(user)
