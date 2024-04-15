from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.todos import crud
from todo.database.models import db_engine, ToDo


async def todo_by_id(
    todo_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
) -> ToDo:
    todo = await crud.get_todo(session=session, todo_id=todo_id)
    if todo is not None:
        return todo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
