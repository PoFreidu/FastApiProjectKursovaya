import os

from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import create_engine, Boolean, String
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, DeclarativeBase, Mapped, mapped_column, declared_attr

from todo.config import settings


# Base = declarative_base()

# engine = create_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)

# class Base(DeclarativeBase):
#     pass


# class User(SQLAlchemyBaseUserTable[int], Base):
#     email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
#     hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
#     is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
#     is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


# engine = create_async_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)
# LocalSession = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)


# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
#     async with LocalSession() as db_local_session:
#         yield db_local_session
#
#
# async def get_user_db(db_local_session: AsyncSession = Depends(get_async_db)):
#     yield SQLAlchemyUserDatabase(db_local_session, User)

# async def get_db():
#     db_local_session = LocalSession()
#     try:
#         yield db_local_session
#     finally:
#         db_local_session.close()


# LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
