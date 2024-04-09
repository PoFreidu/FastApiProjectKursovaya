import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from todo.config import settings

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'db')
if not os.path.exists(db_path):
    os.makedirs(db_path)

Base = declarative_base()

engine = create_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)


def get_db():
    db_local_session = LocalSession()
    try:
        yield db_local_session
    finally:
        db_local_session.close()


LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
