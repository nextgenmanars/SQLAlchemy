from sqlalchemy import Column, Integer, String
from database import Base

class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer(), primary_key=True)
    shop_name = Column(String(100), nullable=False)
