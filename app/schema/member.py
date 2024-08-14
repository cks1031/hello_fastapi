from datetime import datetime

from pydantic import BaseModel


class NewMemberModel(BaseModel):
    userid : str
    passwd : str
    name : str
    email : str

class MemberModel(NewMemberModel):
    mno : int
    regdate : datetime