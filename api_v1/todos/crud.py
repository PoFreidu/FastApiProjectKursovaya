"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from todo.database.models import ToDo
from .schemas import ToDoCreate, ToDoUpdate, ToDoPartialUpdate
from fastapi import Request


async def get_todos(session: AsyncSession) -> list[ToDo]:
    stmt = select(ToDo).order_by(ToDo.id)
    result: Result = await session.execute(stmt)
    todos = result.scalars().all()
    return list(todos)


async def get_todo(
    session: AsyncSession,
    todo_id: int,
) -> ToDo | None:
    return await session.get(ToDo, todo_id)


async def create_todo(
    session: AsyncSession,
    todo_in: ToDoCreate,
) -> ToDo | None:
    todo = ToDo(**todo_in.model_dump())
    session.add(todo)
    await session.commit()
    # await session.refresh(todo)
    return todo


async def update_todo(
    session: AsyncSession,
    todo: ToDo,
    todo_update: ToDoUpdate | ToDoPartialUpdate,
    partial: bool = False,
) -> ToDo:
    for name, value in todo_update.model_dump(exclude_unset=partial).items():
        setattr(todo, name, value)
    await session.commit()
    return todo


# async def partial_update_todo(
#     session: AsyncSession,
#     todo: ToDo,
#     todo_update: ToDoPartialUpdate,
# ):
#     for name, value in todo_update.model_dump(exclude_unset=True).items():
#         setattr(todo, name, value)
#     await session.commit()
#     return todo


async def delete_todo(
    session: AsyncSession,
    todo: ToDo,
) -> None:
    await session.delete(todo)
    await session.commit()
