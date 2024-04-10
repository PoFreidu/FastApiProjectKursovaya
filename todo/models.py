from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from todo.database.database import Base, engine, AsyncSession, Depends
from sqlalchemy import Column, String, Integer, Boolean, TIMESTAMP, ForeignKey, JSON
from datetime import datetime


class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    is_complete = Column(Boolean, default=False)

    # Column("id", Integer, primary_key=True),
    # Column("title", String, nullable=False),
    # Column("is_complete", Boolean, default=False),

# class Roles(Base):
#     __tablename__ = 'roles'
#
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("permissions", JSON),


# class Users(Base):
#     __tablename__ = 'users'
#
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("username", String, nullable=False),
#     Column("password", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
#     Column("role_id", Integer, ForeignKey("roles_id")),

Base.metadata.create_all(bind=engine)
