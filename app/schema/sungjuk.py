from datetime import datetime

from pydantic import BaseModel


class SungjukModel(BaseModel):
    sjno : int
    name: str
    kor: int
    eng: int
    mat: int
    regdate : datetime
