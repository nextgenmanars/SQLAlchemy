from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sqlalchemy

engine = create_engine("postgresql+psycopg2://postgres:12580@localhost/task2_sqlalchemy")
Base = sqlalchemy.orm.declarative_base()
session = Session(bind=engine)
