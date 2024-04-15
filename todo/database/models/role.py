from datetime import datetime, timezone
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean, TIMESTAMP, ForeignKey, JSON, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .profile import Profile


class Role(Base):
    name: Mapped[str] = mapped_column(
        String(72),
        unique=True,
        nullable=False,
    )
    Column("permissions", JSON)
