from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config
from app.models import sungjuk, member

engine = create_engine(config.sqlite_url, connect_args={}, echo=True)
SessionLocal = sessionmaker(atocommit=False, autoflush=False, bind=engine)

async def db_startup():
    sungjuk.Base.metadata.create_all(engine)
    member.Base.metadata.create_all(engine)

async def db_shutdown():
    pass