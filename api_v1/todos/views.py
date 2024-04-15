from typing import List

from fastapi import APIRouter, status, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse

# from starlette.templating.Jinja2Templates import TemplateResponse

# from todo.app import templates
from todo.database.models.db_engine import db_engine

# from ui.pages.router import templates
from . import crud
from .schemas import ToDo, ToDoCreate, ToDoUpdate, ToDoPartialUpdate
from .dependencies import todo_by_id

router = APIRouter(tags=["ToDo"])


# prefix="/todos",
@router.get("/", response_model=list[ToDo])
async def get_todos(
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
):
    return await crud.get_todos(session=session)


@router.post("/post", response_model=ToDo, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_in: ToDoCreate,
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
):
    return await crud.create_todo(session=session, todo_in=todo_in)


# response_class=HTMLResponse,
# request: Request
# templates.TemplateResponse("index.html", {"request": request}))


@router.get("/{todo_id}/", response_model=ToDo)
async def get_todo(
    todo: ToDo = Depends(todo_by_id),
):
    return todo


@router.put("/{todo_id}/")
async def update_todo(
    todo_update: ToDoUpdate,
    todo: ToDo = Depends(todo_by_id),
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
):
    return await crud.update_todo(session=session, todo=todo, todo_update=todo_update)


@router.patch("/{todo_id}/")
async def partial_update_todo(
    todo_update: ToDoPartialUpdate,
    todo: ToDo = Depends(todo_by_id),
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
):
    return await crud.update_todo(
        session=session, todo=todo, todo_update=todo_update, partial=True
    )


@router.delete("/{todo_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo: ToDo = Depends(todo_by_id),
    session: AsyncSession = Depends(db_engine.scoped_session_dependency),
) -> None:
    return await crud.delete_todo(session=session, todo=todo)
