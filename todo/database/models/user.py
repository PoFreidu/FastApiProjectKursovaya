from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from todo.database.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(36), unique=True)
