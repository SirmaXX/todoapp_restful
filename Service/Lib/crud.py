from sqlalchemy.orm import Session
import random
from Lib import models, schemas
from Lib.models import User,Todo
import random

#query(Todo).filter_by(owner_id=user_id).order_by(func.random())
#exec(select(User.items)..filter_by(owner_id=user_id)order_by(func.random())).first()


def randomize(list):
  number=random.randint(0, len(list)-1)
  thislist = []
  for item in list:
      thislist.append(item)
     
  lastitem=thislist[number]
  return lastitem.id

 




def get_random_item(db: Session,user_id:int):
    obj = db.query(User).filter_by(id=user_id).first()
    items = obj.items
    if items:
      first_item = items[0]
      sec ={first_item.title,first_item.description,first_item.id,first_item.owner_id}
      return sec
    else:
      return None


    
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


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
def get_items(db: Session):
    items = db.query(Todo).all()
    if not items:
        return {}
    else :
        return items






def create_user_item(db: Session, item: schemas.TodoCreate, user_id: int):
    db_item = Todo(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



def update_user_item(db: Session,id:int  ,item: schemas.TodoCreate,user_id:int):
     todo = db.query(Todo).filter_by(id=id,owner_id=user_id).first()
     if  todo != None:
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