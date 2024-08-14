from typing import List, Optional

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.dbfactory import get_db
from app.models.member import Member
from app.schema.member import MemberModel, NewMemberModel

member_router = APIRouter()

# @member_router.get('/')
# def index():
#     return 'Hello, member_router!!'

@member_router.get('/', response_model=List[MemberModel])
def list(db: Session = Depends(get_db)):
    members = db.query(Member).all()
    return members

@member_router.post('/', response_model=NewMemberModel)
def add_member(mb: NewMemberModel, db: Session = Depends(get_db)):
    mb = Member(**dict(mb))
    db.add(mb)
    db.commit()
    db.refresh(mb)
    return mb

@member_router.get('/{mno}', response_model=Optional[MemberModel])
def readone_member(mno: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mno).first()
    return member

@member_router.delete('/{mno}', response_model=Optional[MemberModel])
def delete_member(mno: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mno).first()
    if member:
        db.delete(member)
        db.commit()
    return member

@member_router.put('/update', response_model=Optional[MemberModel])
def update_member(mb: MemberModel, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.mno == mb.mno).first()
    if member:
        for key, val in mb.dict().items():
            setattr(member, key, val)
            db.commit()
            db.refresh(member)
    return member
