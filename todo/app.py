from contextlib import asynccontextmanager

from fastapi import FastAPI

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from todo.database import Base
from todo.database.models import db_engine
from api_v1 import router as router_v1
from todo.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_engine.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

app.mount('/templates', StaticFiles(directory='todo/templates'), name='templates')
templates = Jinja2Templates(directory='todo/templates')

# from todo.routes import home
