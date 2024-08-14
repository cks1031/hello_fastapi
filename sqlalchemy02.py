# 회원정보를 이용한 SQL CRUD
# mno, userid, passwd, name, email, regdate
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DATETIME, Sequence, func
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# 데이터베이스 설정
sqlite_url = 'sqlite:///python.db'
engine = create_engine(sqlite_url,
                       connect_args={'check_same_thread': False}, echo=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델 정의
Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, Sequence('seq_member'), primary_key=True, index=True)
    userid = Column(String, index=True)
    passwd = Column(String)
    name = Column(String)
    email = Column(String)
    regdate = Column(DATETIME(timezone=True), server_default=func.now())

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() # 데이터베이스 세션 객체 생성
    try:
        yield db # yield : 파이썬 제너레이터 객체
        # 함수가 호출될 때 비로소 객체를 반환(넘김)
    finally:
        db.close() # 데이터베이스 세션 닫음 (DB 연결해제, 리소스 반환)

# pydantic 모델
class MemberModel(BaseModel):
    mno : int
    userid : str
    passwd : str
    name : str
    email : str
    regdate : datetime

# FastAPI 메인
app = FastAPI()

# 기본페이지
@app.get('/')
def index():
    return 'Hello, sqlalchmey - member!!'

# 회원 조회
@app.get('/member',response_model=List[MemberModel])
def read_member(db: Session = Depends(get_db)):
    members = db.query(Member).all()
    return members

# 회원 추가
@app.post('/member', response_model=MemberModel)
def add_member(mb: MemberModel, db: Session = Depends(get_db)):
    mb = Member(**dict(mb))
    db.add(mb)
    db.commit()
    db.refresh(mb)
    return mb

# 회원 상세 조회 - 회원번호로 조회
@app.get('/member/{mno}', response_model=Optional[MemberModel])
def readone_member(mno: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mno).first()
    return member

# 회원 삭제 - 회원번호로 조회
# 먼저, 삭제할 회원 데이터가 있는지 확인한 후 삭제 실행
@app.delete('/member/{mno}', response_model=Optional[MemberModel])
def delete_member(mno: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mno).first()
    if member:
        db.delete(member)
        db.commit()
    return member

# 회원 수정 - 회원번호로 조회
@app.put('/member', response_model=Optional[MemberModel])
def update_member(mb: MemberModel, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mb.mno).first()
    if member:
        for key, val in mb.dict().items():
            setattr(member, key, val)
            db.commit()
            db.refresh(member)
    return member

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('sqlalchemy02:app', reload=True)