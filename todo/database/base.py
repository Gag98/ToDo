import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from todo.config import settings

# Define the base directory and create the database path
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Create a base class for all models
Base = declarative_base()

# Creating a database engine
engine = create_engine(
    settings.db_url,
    connect_args={'check_same_thread': False},
    echo=True
)

# Create a session factory to interact with the database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """Creates and provides a database session.

    Возвращает:
        generator: Сессия базы данных. Сессия закрывается после использования.
    """
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()

