from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных
DATABASE_URL = "sqlite:///./sql_source/py_test.db"

# Создание движка
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание базового класса для моделей
Base = declarative_base()

# Определение модели User
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)