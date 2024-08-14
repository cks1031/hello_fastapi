from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base


class Sungjuk(Base):
    __tablename__ = 'sungjuk'

    sjno = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    kor = Column(Integer)
    eng = Column(Integer)
    mat = Column(Integer)
    regdate = Column(DateTime, default=datetime.now)
