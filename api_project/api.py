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


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user


@app.get("/users")
async def get_users():
    users = session.query(User).all()
    return users


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: str
    favorites: str


@app.post("/users")
async def create_user(user_data: CreateUser):
    new_user = User(first_name=user_data.first_name, last_name=user_data.last_name,
                    email=user_data.email, date_of_birth=user_data.date_of_birth, favorites=user_data.favorites)
    session.add(new_user)
    session.commit()
    return {"message": "User created successfully"}
