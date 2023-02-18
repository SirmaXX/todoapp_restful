from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from Routers.users import usersroute
from Routers.todos import todosroute
from Lib import crud, models, schemas
from Lib.models import SessionLocal, engine


app = FastAPI()

app.include_router(usersroute, prefix="/users")
app.include_router(todosroute, prefix="/todos")

#https://fastapi.tiangolo.com/tutorial/first-steps/#openapi
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response




