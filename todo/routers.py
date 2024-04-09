from fastapi import Request, Depends
from sqlalchemy.orm import Session
from todo.app import app, templates
from todo.database.database import get_db
from todo.models import ToDo
from todo.config import settings


@app.get('/')
def home(request: Request, db_local_session: Session = Depends(get_db)):
    todos = db_local_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {"request": request,
                                       "app_name": settings.app_name,
                                       "todo_list": todos}
                                      )

