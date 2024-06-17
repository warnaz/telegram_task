from enum import Enum

from sqlalchemy.orm import Mapped

from src.database.models.base import Base, big_int_pk, created_at, updated_at


class UserStatus(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"
    FINISHED = "finished"


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[big_int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    status: Mapped[UserStatus]

    status_updated_at: Mapped[updated_at]
    created_at: Mapped[created_at]
