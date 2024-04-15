from typing import Any

from fastapi import APIRouter, Request, Depends, Form

from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse

from api_v1.todos.views import create_todo
from todo.database.models import db_engine, ToDo

# from starlette.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Pages"])

templates = Jinja2Templates(directory="templates")


# @router.get("/base")
# async def get_base_page(request: Request):
#     return templates.TemplateResponse(
#         "base.html",
#         {"request": request},
#     )


@router.get("/base")
async def get_base_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/create")
async def create_todo_page(request: Request, create=Depends(create_todo)):
    return templates.TemplateResponse(
        "index.html", {"request": request, "create": create}
    )


# {todo_in}
# Я наконец-то сделал этот чёртов запрос!!!
