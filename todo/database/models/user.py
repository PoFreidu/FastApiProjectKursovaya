from datetime import datetime, timezone

from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import db_engine
from .base import Base

if TYPE_CHECKING:
    from .profile import Profile


# class User(Base):
#     username: Mapped[str] = mapped_column(String(36), unique=True)
#
#     profile: Mapped["Profile"] = relationship(back_populates="user")


class User(SQLAlchemyBaseUserTable[int], Base):
    username: Mapped[str] = mapped_column(
        String(72),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(length=320),
        unique=True,
        index=True,
        nullable=False,
    )
    # registered_at: Mapped[TIMESTAMP] = mapped_column(
    #     TIMESTAMP,
    #     default=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
    #     nullable=False,
    # )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
    )

    profile: Mapped["Profile"] = relationship(back_populates="user")


# async def get_user_db(self) -> AsyncSession:
#     session = self.scoped_session_dependency()
#     yield SQLAlchemyUserDatabase(
#         session,
#         User,
#     )


async def get_user_db(
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
):
    yield SQLAlchemyUserDatabase(session, User)
