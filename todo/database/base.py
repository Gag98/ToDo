import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from todo.config import settings

# Определение базового каталога и создание пути к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Создание базового класса для всех моделей
Base = declarative_base()

# Создание движка базы данных
engine = create_engine(
    settings.db_url,
    connect_args={'check_same_thread': False},
    echo=True
)

# Создание фабрики сессий для взаимодействия с базой данных
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    """Создает и предоставляет сессию базы данных.

    Возвращает:
        generator: Сессия базы данных. Сессия закрывается после использования.
    """
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()