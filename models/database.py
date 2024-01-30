from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy

engine = create_engine("postgresql+psycopg2://nextgenman:12345678@database:5432/postgres_db")
Base = sqlalchemy.orm.declarative_base()
session = Session(bind=engine)
