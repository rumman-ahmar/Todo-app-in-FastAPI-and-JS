from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create sqlite engine instance
engine = create_engine("sqlite:///database/todo.db")

# Create declaritive base meta instance
Base = declarative_base()

# Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


def init_db():
    Base.metadata.create_all(engine)


def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
