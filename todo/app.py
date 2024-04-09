from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount('/templates', StaticFiles(directory='todo/templates'), name='templates')
templates = Jinja2Templates(directory='todo/templates')

from todo.routers import home
