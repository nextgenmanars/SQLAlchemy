from sqlalchemy import Column, Integer, String, MetaData
from database import Base, session, engine

metadata = MetaData()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    date_of_birth = Column(String(20), nullable=False)
    favorites = Column(String(100))



u1 = User(
    first_name="Dmitriy",
    last_name="Yatsenko",
    email="qwert@gmail.com",
    date_of_birth="1999-10-20",
    favorites=""
)

u2 = User(
    first_name="Vasya",
    last_name="Petrov",
    email="adasdvcx@gmail.com",
    date_of_birth="1994-09-10",
    favorites=""
)

u3 = User(
    first_name="Katya",
    last_name="Ivanova",
    email="katyazaychik@gmail.com",
    date_of_birth="1998-01-01",
    favorites=""
)

u4 = User(
    first_name="Alya",
    last_name="Lutyk",
    email="lutyk99@gmail.com",
    date_of_birth="1999-10-20",
    favorites=""
)

u5 = User(
    first_name="Lena",
    last_name="Sokolova",
    email="solnce@gmail.com",
    date_of_birth="2003-08-22",
    favorites=""
)

Base.metadata.create_all(bind=engine)
session.add_all([u1, u2, u3, u4, u5])
session.commit()
