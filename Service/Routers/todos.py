

from fastapi import APIRouter,Depends, Request,HTTPException
from flask import jsonify
from sqlalchemy.orm import Session
import json
from Lib.models import SessionLocal
from Lib.schemas import UserCreate,TodoCreate,Todo
from Lib.crud import get_users,get_user_by_email,get_user, create_user,create_user_item,get_items

todosroute = APIRouter(responses={404: {"description": "Not found"}})




# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



