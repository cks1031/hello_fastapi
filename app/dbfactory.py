from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config

engine = create_engine(config.sqlite_url, connect_args={}, echo=True)
SessionLocal = sessionmaker(atocommit=False, autoflush=False, bind=engine)

def db_startup():
    pass