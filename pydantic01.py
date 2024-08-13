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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('pydantic01:app', reload=True)