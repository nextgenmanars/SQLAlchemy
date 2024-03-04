from fastapi import FastAPI
from pydantic import BaseModel
from models.database import Base, engine
from sqlalchemy import MetaData
import user, shop, category, product

metadata = MetaData()
app = FastAPI()

# Base.metadata.create_all(bind=engine)


class Status(BaseModel):
    status: str = "ok"


@app.get("/")
async def status():
    return Status()
