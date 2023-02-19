

from fastapi import APIRouter,Depends, Request,HTTPException
from flask import jsonify
from sqlalchemy.orm import Session
import json
from Lib.schemas import User,UserCreate,Todo,TodoCreate
from Lib import crud
from Lib.models import SessionLocal



usersroute = APIRouter(responses={404: {"description": "Not found"}})



# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()





@usersroute.get("/", response_model=list[User])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users



@usersroute.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)




@usersroute.delete("/delete/{id}" ,description=" kullanıcınun bilgilerini silen  fonksiyon ")
async def del_user(req: Request,id:int,db: Session = Depends(get_db)):
   return crud.deleteuser(db,id)
     



@usersroute.put("/update/{id}",description=" kullanıcının bilgilerini editleyen  fonksiyon ")
async def update_user(user1:UserCreate,id:int,db: Session = Depends(get_db)):
    return crud.updateuser(db,user1,id)
 

#todolist bölümü


@usersroute.get("/{user_id}/random/items", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_random_item(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@usersroute.get("/{user_id}/items", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@usersroute.post("/{user_id}/items/", response_model=Todo)
def create_item_for_user(
    user_id: int, item: TodoCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@usersroute.put("/{user_id}/{item_id}/update")
def update_item_for_user(
item: TodoCreate, item_id:int, user_id: int, db: Session = Depends(get_db)
):
    return crud.update_user_item(db=db, item=item,id=item_id,user_id=user_id)



@usersroute.delete("/{user_id}/{item_id}")
def delete_item_for_user(
  item_id:int, user_id: int, db: Session = Depends(get_db)
):
    return crud.delete_user_item(db=db, id=item_id,user_id=user_id)
    





