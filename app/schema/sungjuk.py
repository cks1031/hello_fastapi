from datetime import datetime

from pydantic import BaseModel


class NewSungjukModel(BaseModel):
    name: str
    kor: int
    eng: int
    mat: int

class SungjukModel(NewSungjukModel):
    sjno : int
    regdate : datetime
