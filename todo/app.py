from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi_users import fastapi_users, FastAPIUsers

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from api_v1 import router as router_v1
from api_v1.auth.auth import auth_backend
from api_v1.auth.manager import get_user_manager
from api_v1.auth.schemas import UserRead, UserCreate, UserUpdate
from todo.config import settings
from todo.database.models import User

from ui.pages.router import router as router_pages


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(router=router_pages)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.mount("/static", StaticFiles(directory="ui/static"), name="static")
# app.mount("/templates", StaticFiles(directory="ui/templates"), name="templates")
# app.mount("/templates", StaticFiles(directory="todo/templates"), name="templates")
# templates = Jinja2Templates(directory="todo/templates")
# templates = Jinja2Templates(directory="ui/templates")

# from todo.routes import home

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email or user.username}"
