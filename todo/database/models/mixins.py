from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

from todo.database.models import User


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(self) -> Mapped[int]:
        return mapped_column(ForeignKey("users.id"), unique=self._user_id_unique, nullable=self._user_id_nullable)

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship("User", back_populates=self._user_back_populates)
