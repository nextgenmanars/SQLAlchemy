from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import session, Base, engine
from user import User

app = FastAPI()


# Base.metadata.drop_all(bind=engine)

class Status(BaseModel):
    status: str = "ok"


@app.get("/")
async def status():
    return Status()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user
