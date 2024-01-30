from fastapi import FastAPI
from database import Base, engine
from models import user, shop
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

class Status(BaseModel):
    status: str = "ok"


@app.get("/")
async def status():
    return Status()
