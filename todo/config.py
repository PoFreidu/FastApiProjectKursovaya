import os

from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
BASE_DIR_URL = os.path.dirname(os.path.abspath(__name__))

db_path = os.path.join(BASE_DIR_URL, 'todo', 'database', 'db')
if not os.path.exists(db_path):
    os.makedirs(db_path)


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_path: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    algorithm: str = 'RS256'


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    app_name: str = os.getenv('NAME_APP')
    db_url: str = os.getenv('SQLALCHEMY_DATABASE_URL')
    # db_echo: bool = False
    db_echo: bool = True

    auth_jwt: AuthJWT = AuthJWT()

    class Config:
        env_file: str = '../.env'


settings = Settings()
