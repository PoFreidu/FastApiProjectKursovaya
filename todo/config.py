import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'db')
if not os.path.exists(db_path):
    os.makedirs(db_path)


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    app_name: str = os.getenv('NAME_APP')
    db_url: str = os.getenv('SQLALCHEMY_DATABASE_URL')
    # db_echo: bool = False
    db_echo: bool = True

    class Config:
        env_file: str = '../.env'


settings = Settings()
