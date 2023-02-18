from sqlalchemy.orm import Session

from Lib import models, schemas
from Lib.models import User,Todo

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def deleteuser(db: Session,id:int):
    user = db.query(User).filter_by(id=id).first()
    if  user != None:
      db.delete( user)
      db.commit()
    else :
        return {}
        

def updateuser(db: Session,user1,id:int):
     user =get_user(db,id)
     if user != None:
      db.query(User).filter_by(id=id).update(
      dict(email=user1.email, hashed_password=user1.password))
      db.commit()
      return True
     else :
      return False





#-------------------------------------------------        
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.TodoCreate, user_id: int):
    db_item = Todo(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



def update_user_item(db: Session,id:int  ,item: schemas.TodoCreate,user_id:int):
     user =get_user(db,id)
     if user != None:
      db.query(Todo).filter_by(id=id,owner_id=user_id).update(
      dict(title=item.title, description=item.description))
      db.commit()
      return True
     else :
      return False



def delete_user_item(db: Session,id:int,user_id:int):
    todo = db.query(Todo).filter_by(id=id,owner_id=user_id).first()
    if  todo != None:
      db.delete( todo)
      db.commit()
    else :
        return {}