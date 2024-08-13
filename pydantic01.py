from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


# pydantic
# 데이터 유효성 검사 및 직렬화/역직렬화 지원 도구
# docs.pydantic.dev
# pip install pydantic

# 성적 모델 정의
class Sungjuk(BaseModel):
    name: str
    kor: int
    eng: int
    mat: int

# 성적 데이터 저장용 변수
sungjuk_db: List[Sungjuk] = []

app = FastAPI()

@app.get('/')
def index():
    return 'Hello pydantic!!'

# 성적 데이터 조회
# response_model : 응답데이터 형식 지정
# 이를 통해 클라이언트는 서버가 어떤 종류의 데이터를 응답으로 보내는지 알수 있음
@app.get('/sj', response_model=List[Sungjuk])
def sj_readall():
    return sungjuk_db

# 성적 데이터 추가
# FastAPI swagger UI 이용 : http://127.0.0.1:8000/docs
# 클라이언트가 요청시 성적데이터는 json으로 구성되어야 함
@app.post('/sjadd', response_model=Sungjuk)
def sj_create(sj: Sungjuk):
    # sj = Sungjuk('혜교', 99,98,99).json()

    sungjuk_db.append(sj)
    return sj

# 샘플 성적데이터 추가 : 3건의 기본 데이터
@app.get('/sjadd', response_model=Sungjuk)
def sj_create():
    sj = Sungjuk(name='혜교', kor=99,eng=98,mat=99)
    sungjuk_db.append(sj)

    sj = Sungjuk(name='라라', kor=59,eng=68,mat=76)
    sungjuk_db.append(sj)

    sj = Sungjuk(name='누누', kor=29,eng=38,mat=49)
    sungjuk_db.append(sj)
    return sj

# 성적데이터 상세 조회  - 이름으로 조회
@app.get('/sjone/{name}',response_model=Sungjuk)
def sjone(name: str):
    findone = Sungjuk(name='none',kor=00,eng=00,mat=00)
    for sj in sungjuk_db:
        if sj.name == name:
            findone = sj
    return findone

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('pydantic01:app', reload=True)