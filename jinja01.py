from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, select
from sqlalchemy.orm import declarative_base, Session


sqlite_url = 'sqlite:///app/clouds2024.db'
engine = create_engine(sqlite_url, connect_args={}, echo=True)

Base = declarative_base()

class Zipcode(Base):
    __tablename__ = 'zipcode'

    zipcode = Column(String, index=True)
    sido = Column(String)
    gugun = Column(String)
    dong = Column(String)
    ri = Column(String)
    bunji = Column(String)
    seq = Column(String, primary_key=True)

app = FastAPI()
@app.get('/')
def index():
    return 'Hello, jinja2!!'

@app.get('/zipcode/{dong}')
def zipcode(dong: str):
    result = ''

    # sessionmaker 없이 DB 객체 직접 생성
    with Session(engine) as sess:
        stmt = select(Zipcode).where(Zipcode.dong.like(f'{dong}'))
        rows = sess.scalars(stmt)

        for row in rows:
            result += f'{row.zipcode} {row.sido} {row.gugun} {row.dong}'

    return f'{result}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('jinja01:app', reload=True)