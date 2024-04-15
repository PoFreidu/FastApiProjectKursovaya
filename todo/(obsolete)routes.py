from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND

from todo.app import app, templates

# from todo.database.database import get_db
from todo.database.models import ToDo
from todo.config import settings


# @app.get('/')
# async def home(request: Request, db_local_session: Session = Depends(get_db)):
#     todos = db_local_session.query(ToDo).all()
#     return templates.TemplateResponse('html/index.html',
#                                       {"request": request,
#                                        "app_name": settings.app_name,
#                                        "todo_list": todos}
#                                       )


# @app.get('/edit/')
# def edit(request: Request, db_local_session: Session = Depends(get_db)):
#     todos = db_local_session.query(ToDo).all()
#     return templates.TemplateResponse('html/edit.html1',
#                                       # {"request": request,
#                                       # "app_name": settings.app_name,
#                                       # "todo_list": todos}
#                                       )


# @app.post('/add')
# async def add(title: str = Form(...), db_local_session: Session = Depends(get_db)):
#     new_todo = ToDo(title=title)
#     db_local_session.add(new_todo)
#     db_local_session.commit()
#
#     url = app.url_path_for('home')
#     return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


# @app.get("/edit/{todo_id}")
# async def rename(request: Request, todo_id: int, db_local_session: Session = Depends(get_db)):
#     todo = db_local_session.query(ToDo).filter(ToDo.id == todo_id).first()
#     return templates.TemplateResponse("html/edit.html1", {"request": request, "todo": todo})
#
#
# @app.post('/edit/{todo_id}')
# async def rename(todo_id: int, title: str = Form(...), db_local_session: Session = Depends(get_db)):
#     todo = db_local_session.query(ToDo).filter(ToDo.id == todo_id).scalar()
#     todo.title = title
#     db_local_session.commit()
#
#     url = app.url_path_for('home')
#     return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)
#
#
# @app.get('/update/{todo_id}')
# async def update(todo_id: int, db_local_session: Session = Depends(get_db)):
#     todo = db_local_session.query(ToDo).filter(ToDo.id == todo_id).first()
#     todo.is_complete = not todo.is_complete
#     db_local_session.commit()
#
#     url = app.url_path_for('home')
#     return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
# url1 = app.url_path_for('edit')
# if 'home' in url:
#     return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
# elif 'edit' in url:
#     return RedirectResponse(url=url1, status_code=HTTP_302_FOUND)


# @app.get('/delete/{todo_id}')
# async def delete(todo_id: int, db_local_session: Session = Depends(get_db)):
#     todo = db_local_session.query(ToDo).filter(ToDo.id == todo_id).first()
#     db_local_session.delete(todo)
#     db_local_session.commit()
#
#     url = app.url_path_for('home')
#     return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
