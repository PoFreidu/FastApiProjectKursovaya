from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from fastapi_users.authentication import CookieTransport

from todo.config import settings

cookie_transport = CookieTransport(cookie_name="ToDo", cookie_max_age=3600)


PUBLIC_KEY = settings.auth_jwt.public_key_path.read_text()

PRIVATE_KEY = settings.auth_jwt.private_key_path.read_text()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=PRIVATE_KEY,
        lifetime_seconds=3600,
        algorithm="RS256",
        public_key=PUBLIC_KEY,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
