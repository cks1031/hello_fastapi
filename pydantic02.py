from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

# 회원정보를 이용한 CRUD
# userid, passwd, name, email, regdate

# 회원정보 모델 정의
class Member(BaseModel):
    userid : str
    passwd : str
    name : str
    email : str
    regdate : datetime

member_db: List[Member] = []

app = FastAPI()

# 기본 페이지
@app.get('/')
def index():
    return 'Hello, pydantic!! - Member!!'

# 회원 데이터 조회
@app.get('/member',response_model=List[Member])
def member():
    return member_db

# 회원 데이터 추가
@app.post('/member',response_model=Member)
def memberok(mb: Member):
    member_db.append(mb)
    return mb

# 회원데이터 상세 조회 - 이름으로 조회
@app.get('/member/{userid}',response_model=Member)
def memberok(userid: str):
    memberone = Member(userid='none', passwd='none', name='none', email='none' ,regdate='1970-01-01T00:00:00.000Z')
    for mb in member_db:
        if mb.userid == userid:
            memberone = mb
    return memberone

# 회원데이터 삭제
@app.delete('/member/{userid}',response_model=Member)
def memberdel(userid: str):
    memberone = Member(userid='none', passwd='none', name='none', email='none' ,regdate='1970-01-01T00:00:00.000Z')
    for idx, mb in enumerate(member_db):
        if mb.userid == userid:
            memberone = member_db.pop(idx)
    return memberone

# 회원데이터 수정
@app.put('/member',response_model=Member)
def membermod(one: Member):
    putone = Member(userid='none', passwd='none', name='none', email='none' ,regdate='1970-01-01T00:00:00.000Z')
    for idx, mb in enumerate(member_db):
        if mb.userid == one.userid:
            member_db[idx] = one
            putone = one
    return putone

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('pydantic02:app', reload=True)